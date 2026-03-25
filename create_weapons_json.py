import json, os

BASE = os.path.expanduser("~/dev/portfolio/eldenring-sim")

weapons = [
  {
    "id": "ruins_gs", "name": "Trümmergroßschwert", "nameEN": "Ruins Greatsword",
    "category": "colossal_sword", "isSomber": True, "isDLC": False,
    "icon": "☄️", "weight": 23.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 124, "mag": 37, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 303, "mag": 90, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 1.4, "dex": 0.0, "int": 0.45, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 50, "dex": 0, "int": 16, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Wave of Destruction",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "grafted_gs", "name": "Großschwert der Verpflanzung", "nameEN": "Grafted Blade Greatsword",
    "category": "colossal_sword", "isSomber": True, "isDLC": False,
    "icon": "🦁", "weight": 21.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 162, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 396, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.9, "dex": 0.45, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 40, "dex": 14, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Oath of Vengeance",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "guts_gs", "name": "Das Großschwert (Guts)", "nameEN": "Greatsword",
    "category": "colossal_sword", "isSomber": False, "isDLC": False,
    "icon": "🗡️", "weight": 23.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 164, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 400, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.8, "dex": 0.2, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 31, "dex": 12, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "War Cry",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "meteoric_gs", "name": "Uraltes Meteor-Erzgroßschwert", "nameEN": "Meteoric Ore Blade",
    "category": "colossal_sword", "isSomber": True, "isDLC": False,
    "icon": "⚡", "weight": 22.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 145, "mag": 45, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 340, "mag": 105, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 1.0, "dex": 0.0, "int": 0.0, "fai": 0.0, "arc": 0.9},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 35, "dex": 0, "int": 0, "fai": 0, "arc": 19},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Gravitas",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "radahn_gs", "name": "Großschwert der Sternengeißel", "nameEN": "Starscourge Greatsword",
    "category": "colossal_sword", "isSomber": True, "isDLC": False,
    "icon": "🌌", "weight": 20.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 129, "mag": 85, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 316, "mag": 200, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.9, "dex": 0.3, "int": 0.4, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 38, "dex": 12, "int": 15, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Starcaller Cry",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "godslayer_gs", "name": "Großschwert der Gottestöterin", "nameEN": "Godslayer's Greatsword",
    "category": "colossal_sword", "isSomber": True, "isDLC": False,
    "icon": "🔥", "weight": 17.5, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 119, "mag": 0, "fire": 77, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 291, "mag": 0, "fire": 188, "light": 0, "holy": 0},
    "scaling":    {"str": 0.3, "dex": 0.9, "int": 0.0, "fai": 0.7, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 20, "dex": 22, "int": 0, "fai": 20, "arc": 0},
    "supportedAffinities": ["standard"],
    "defaultSkill": "The Queen's Black Flame",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "giant_crusher", "name": "Riesenbrecher", "nameEN": "Giant-Crusher",
    "category": "colossal_weapon", "isSomber": False, "isDLC": False,
    "icon": "🔨", "weight": 26.5, "physDmgType": "Strike", "critical": 100,
    "baseDamage": {"phys": 155, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 380, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 1.0, "dex": 0.0, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 60, "dex": 0, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Endure",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "prelate_crozier", "name": "Inferno-Stab des Prälaten", "nameEN": "Prelate's Inferno Crozier",
    "category": "colossal_weapon", "isSomber": False, "isDLC": False,
    "icon": "👹", "weight": 23.5, "physDmgType": "Strike", "critical": 100,
    "baseDamage": {"phys": 156, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 382, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.9, "dex": 0.2, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 45, "dex": 8, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Prelate's Charge",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "great_club", "name": "Große Keule", "nameEN": "Great Club",
    "category": "colossal_weapon", "isSomber": False, "isDLC": False,
    "icon": "🪵", "weight": 17.0, "physDmgType": "Strike", "critical": 100,
    "baseDamage": {"phys": 154, "mag": 0, "fire": 0, "light": 0, "holy": 46},
    "maxDamage":  {"phys": 377, "mag": 0, "fire": 0, "light": 0, "holy": 110},
    "scaling":    {"str": 0.9, "dex": 0.0, "int": 0.0, "fai": 0.4, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 35, "dex": 0, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Endure",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "claymore", "name": "Claymore", "nameEN": "Claymore",
    "category": "greatsword", "isSomber": False, "isDLC": False,
    "icon": "⚔️", "weight": 9.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 138, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 338, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.6, "dex": 0.6, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 16, "dex": 13, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Lion's Claw",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "blasphemous", "name": "Blasphemische Klinge", "nameEN": "Blasphemous Blade",
    "category": "greatsword", "isSomber": True, "isDLC": False,
    "icon": "🐍", "weight": 13.5, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 121, "mag": 0, "fire": 78, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 296, "mag": 0, "fire": 191, "light": 0, "holy": 0},
    "scaling":    {"str": 0.4, "dex": 0.4, "int": 0.0, "fai": 0.9, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 22, "dex": 15, "int": 0, "fai": 21, "arc": 0},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Taker's Flames",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "rivers_blood", "name": "Blutige Ströme", "nameEN": "Rivers of Blood",
    "category": "katana", "isSomber": True, "isDLC": False,
    "icon": "🩸", "weight": 6.5, "physDmgType": "Slash", "critical": 100,
    "baseDamage": {"phys": 76, "mag": 0, "fire": 76, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 186, "mag": 0, "fire": 186, "light": 0, "holy": 0},
    "scaling":    {"str": 0.3, "dex": 0.9, "int": 0.0, "fai": 0.0, "arc": 0.9},
    "passive":    {"bleed": 89, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 12, "dex": 18, "int": 0, "fai": 0, "arc": 20},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Corpse Piler",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "moonveil", "name": "Mondschleier", "nameEN": "Moonveil",
    "category": "katana", "isSomber": True, "isDLC": False,
    "icon": "🌙", "weight": 6.5, "physDmgType": "Slash", "critical": 100,
    "baseDamage": {"phys": 73, "mag": 87, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 178, "mag": 213, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.2, "dex": 0.8, "int": 0.9, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 12, "dex": 18, "int": 23, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Transient Moonlight",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
]

output = {
  "meta": {
    "schema": "eldenring_sim_v2",
    "patchTag": "1.16.1",
    "approximationLevel": "estimated",
    "note": "AR berechnung ist eine Näherung. Keine exakten Regulation-Paramdaten."
  },
  "weapons": weapons
}

out_path = f"{BASE}/docs/data/weapons_full.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✅ weapons_full.json geschrieben – {len(weapons)} Waffen")
print(f"   Pfad: {out_path}")
