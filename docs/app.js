let db = null;
const el = (id) => document.getElementById(id);

function sumBase(dmg){
  return (dmg.phys||0)+(dmg.mag||0)+(dmg.fire||0)+(dmg.ligh||0)+(dmg.holy||0);
}

function meetsReq(req, stats, twoHand){
  const strEff = twoHand ? Math.floor(stats.str * 1.5) : stats.str;
  return (
    strEff >= req.str &&
    stats.dex >= req.dex &&
    stats.int >= req.int &&
    stats.fth >= req.fth &&
    stats.arc >= req.arc
  );
}

function readStats(){
  return {
    str: Number(el("statStr").value||0),
    dex: Number(el("statDex").value||0),
    int: Number(el("statInt").value||0),
    fth: Number(el("statFth").value||0),
    arc: Number(el("statArc").value||0),
  };
}

function render(){
  if (!db) return;

  const wid = el("weaponSelect").value;
  const weapon = db.weapons.find(w => w.id === wid);
  if (!weapon) return;

  const stats = readStats();
  const twoHand = el("twoHand").checked;
  const ok = meetsReq(weapon.requirements, stats, twoHand);

  const upgrade = Number(el("upgradeLevel").value||0);
  const affinity = el("affinitySelect").value;

  const path = weapon.upgrade_path || "unknown";
  const reinforceRow =
    (db.reinforce_tables?.[path]?.[String(upgrade)]) ||
    { base_mult: 1.0, scaling_mult: 1.0 };

  const affinityRule =
    (db.affinity_rules || []).find(a => a.affinity === affinity) ||
    { base_mult: {phys:1,mag:1,fire:1,ligh:1,holy:1} };

  const base0 = weapon.base_damage_plus0;
  const baseAdj = {
    phys: Math.round(base0.phys * reinforceRow.base_mult * (affinityRule.base_mult.phys||1)),
    mag:  Math.round(base0.mag  * reinforceRow.base_mult * (affinityRule.base_mult.mag||1)),
    fire: Math.round(base0.fire * reinforceRow.base_mult * (affinityRule.base_mult.fire||1)),
    ligh: Math.round(base0.ligh * reinforceRow.base_mult * (affinityRule.base_mult.ligh||1)),
    holy: Math.round(base0.holy * reinforceRow.base_mult * (affinityRule.base_mult.holy||1)),
  };

  const reqLine = `REQ STR ${weapon.requirements.str} / DEX ${weapon.requirements.dex} / INT ${weapon.requirements.int} / FTH ${weapon.requirements.fth} / ARC ${weapon.requirements.arc}`;
  const grade = weapon.scaling_grade_display;
  const gradeLine = `Scaling (Display): STR ${grade.str} / DEX ${grade.dex} / INT ${grade.int} / FTH ${grade.fth} / ARC ${grade.arc}`;

  el("details").innerHTML = `
    <div><strong>${weapon.name}</strong></div>
    <div class="muted">${weapon.weapon_class} • ${weapon.upgrade_path} • Weight ${weapon.weight}</div>
    <div class="mono" style="margin-top:8px">${reqLine}</div>
    <div class="mono">${gradeLine}</div>
    <div style="margin-top:8px">${ok ? '<span class="ok">Requirements erfüllt</span>' : '<span class="bad">Requirements NICHT erfüllt</span>'}</div>
  `;

  el("calc").innerHTML = `
    <div class="mono">Upgrade: +${upgrade} (path: ${path}) • Affinity: ${affinity}</div>
    <div style="margin-top:8px"><strong>Base (adjusted, placeholder tables):</strong></div>
    <div class="mono">Phys ${baseAdj.phys} | Mag ${baseAdj.mag} | Fire ${baseAdj.fire} | Ligh ${baseAdj.ligh} | Holy ${baseAdj.holy}</div>
    <div style="margin-top:8px"><strong>Total Base AR (no scaling yet):</strong> ${sumBase(baseAdj)}</div>
  `;
}

async function init(){
  const full = await fetch("./data/weapons_full.json").then(r=>r.json());
  db = full;

  const ws = el("weaponSelect");
  ws.innerHTML = "";
  for (const w of db.weapons){
    const opt = document.createElement("option");
    opt.value = w.id;
    opt.textContent = `${w.name} (${w.weapon_class})`;
    ws.appendChild(opt);
  }

  const as = el("affinitySelect");
  as.innerHTML = "";
  for (const a of (db.affinity_rules || [])){
    const opt = document.createElement("option");
    opt.value = a.affinity;
    opt.textContent = a.affinity;
    as.appendChild(opt);
  }

  ["weaponSelect","upgradeLevel","affinitySelect","statStr","statDex","statInt","statFth","statArc","twoHand"]
    .forEach(id => el(id).addEventListener("input", render));

  render();
}

init().catch(err=>{
  el("details").innerHTML = `<pre class="mono">Load error: ${String(err)}</pre>`;
});
