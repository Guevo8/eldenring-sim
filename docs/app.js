let db = null;
const el = (id) => document.getElementById(id);

const GRADE_BASE = { S: 1.1, A: 1.0, B: 0.9, C: 0.75, D: 0.55, E: 0.4, "-": 0 };

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

function evalCurve(curves, grade, stat){
  const pts = curves?.[grade] || curves?.default || [];
  if (!pts.length) return 0;
  if (stat <= pts[0].stat) return pts[0].mult;
  for (let i = 1; i < pts.length; i++){
    const prev = pts[i-1];
    const curr = pts[i];
    if (stat <= curr.stat){
      const span = (curr.stat - prev.stat) || 1;
      const t = (stat - prev.stat) / span;
      return prev.mult + t * (curr.mult - prev.mult);
    }
  }
  return pts[pts.length-1].mult;
}

function buildScaling(baseAdj, weapon, stats, twoHand, reinforceRow, affinityRule){
  const curves = db?.scaling_curves || {};
  const req = weapon.requirements;
  const grade = weapon.scaling_grade_display;

  const scaling = {phys:0,mag:0,fire:0,ligh:0,holy:0};
  const total = {};

  const statKeys = ["str","dex","int","fth","arc"];
  for (const sk of statKeys){
    const gradeLetter = grade?.[sk] || "-";
    const baseCoeff = GRADE_BASE[gradeLetter] ?? 0;
    if (baseCoeff === 0) continue;

    const statValueRaw = stats[sk] || 0;
    const statValue = (sk === "str" && twoHand) ? Math.floor(statValueRaw * 1.5) : statValueRaw;
    const curveVal = evalCurve(curves, gradeLetter, statValue);
    const mult = (affinityRule.scaling_mult?.[sk] || 1) * (reinforceRow.scaling_mult || 1);
    const meets = statValue >= (req[sk] || 0);
    const penalty = meets ? 1.0 : Math.max(0, (statValue / Math.max(req[sk] || 1, 1)) * 0.5);
    const statScale = baseCoeff * curveVal * mult * penalty;

    for (const dmgType of Object.keys(scaling)){
      const baseForType = baseAdj[dmgType] || 0;
      scaling[dmgType] += baseForType * statScale;
    }
  }

  for (const dmgType of Object.keys(baseAdj)){
    total[dmgType] = Math.round(baseAdj[dmgType] + (scaling[dmgType] || 0));
    scaling[dmgType] = Math.round(scaling[dmgType] || 0);
  }

  return { scaling, total };
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
    { base_mult: {phys:1,mag:1,fire:1,ligh:1,holy:1}, scaling_mult: {str:1,dex:1,int:1,fth:1,arc:1} };

  const base0 = weapon.base_damage_plus0;
  const baseAdj = {
    phys: Math.round(base0.phys * reinforceRow.base_mult * (affinityRule.base_mult.phys||1)),
    mag:  Math.round(base0.mag  * reinforceRow.base_mult * (affinityRule.base_mult.mag||1)),
    fire: Math.round(base0.fire * reinforceRow.base_mult * (affinityRule.base_mult.fire||1)),
    ligh: Math.round(base0.ligh * reinforceRow.base_mult * (affinityRule.base_mult.ligh||1)),
    holy: Math.round(base0.holy * reinforceRow.base_mult * (affinityRule.base_mult.holy||1)),
  };
  const scaling = buildScaling(baseAdj, weapon, stats, twoHand, reinforceRow, affinityRule);

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
    <div style="margin-top:8px"><strong>Base (reinforce + affinity):</strong></div>
    <div class="mono">Phys ${baseAdj.phys} | Mag ${baseAdj.mag} | Fire ${baseAdj.fire} | Ligh ${baseAdj.ligh} | Holy ${baseAdj.holy}</div>
    <div style="margin-top:8px"><strong>Scaling contribution (curves + affinity + upgrade):</strong></div>
    <div class="mono">Phys ${scaling.scaling.phys} | Mag ${scaling.scaling.mag} | Fire ${scaling.scaling.fire} | Ligh ${scaling.scaling.ligh} | Holy ${scaling.scaling.holy}</div>
    <div style="margin-top:8px"><strong>Total AR:</strong></div>
    <div class="mono">Phys ${scaling.total.phys} | Mag ${scaling.total.mag} | Fire ${scaling.total.fire} | Ligh ${scaling.total.ligh} | Holy ${scaling.total.holy}</div>
    <div style="margin-top:8px"><strong>Sum:</strong> ${sumBase(scaling.total)}</div>
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
