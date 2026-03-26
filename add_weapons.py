import json, os

BASE = os.path.expanduser("~/dev/portfolio/eldenring-sim")
path = f"{BASE}/docs/data/weapons_full.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

new_weapons = [
  # ── NORMAL +25 ──────────────────────────────────────────────
  {
    "id": "zweihander", "name": "Zweihänder", "nameEN": "Zweihander",
    "category": "colossal_sword", "isSomber": False, "isDLC": False,
    "icon": "🗡️", "weight": 15.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 148, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 345, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.55, "dex": 0.45, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 19, "dex": 11, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Stamp (Upward Cut)",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "flamberge", "name": "Flamberge", "nameEN": "Flamberge",
    "category": "greatsword", "isSomber": False, "isDLC": False,
    "icon": "🔥", "weight": 9.5, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 124, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 304, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.5, "dex": 0.5, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 55, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 16, "dex": 14, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Brace",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "gargoyle_halberd", "name": "Gargoyle-Hellebarde", "nameEN": "Gargoyle's Halberd",
    "category": "halberd", "isSomber": False, "isDLC": False,
    "icon": "⚔️", "weight": 12.5, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 130, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 318, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.65, "dex": 0.3, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 26, "dex": 10, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Spinning Slash",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "banished_knight_halberd", "name": "Hellebarde des Verbannten Ritters", "nameEN": "Banished Knight's Halberd",
    "category": "halberd", "isSomber": False, "isDLC": False,
    "icon": "⚔️", "weight": 12.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 128, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 312, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.55, "dex": 0.45, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 14, "dex": 12, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Spinning Slash",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "nightrider_glaive", "name": "Nachtreiter-Gleve", "nameEN": "Nightrider Glaive",
    "category": "halberd", "isSomber": False, "isDLC": False,
    "icon": "⚔️", "weight": 13.5, "physDmgType": "Slash", "critical": 100,
    "baseDamage": {"phys": 141, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 345, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.65, "dex": 0.35, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 26, "dex": 10, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Spinning Slash",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "uchigatana", "name": "Uchigatana", "nameEN": "Uchigatana",
    "category": "katana", "isSomber": False, "isDLC": False,
    "icon": "⚔️", "weight": 5.5, "physDmgType": "Slash", "critical": 100,
    "baseDamage": {"phys": 115, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 269, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.4, "dex": 0.6, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 45, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 11, "dex": 15, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Unsheathe",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "nagakiba", "name": "Nagakiba", "nameEN": "Nagakiba",
    "category": "katana", "isSomber": False, "isDLC": False,
    "icon": "⚔️", "weight": 7.5, "physDmgType": "Slash", "critical": 100,
    "baseDamage": {"phys": 115, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 269, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.4, "dex": 0.6, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 45, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 18, "dex": 22, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard","heavy","keen","quality","fire","flame_art","lightning","sacred","magic","cold","poison","blood","occult"],
    "defaultSkill": "Unsheathe",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  # ── SOMBER +10 ──────────────────────────────────────────────
  {
    "id": "morgott_sword", "name": "Verfluchtes Schwert Morgotts", "nameEN": "Morgott's Cursed Sword",
    "category": "curved_greatsword", "isSomber": True, "isDLC": False,
    "icon": "🩸", "weight": 8.0, "physDmgType": "Slash", "critical": 100,
    "baseDamage": {"phys": 120, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 293, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.35, "dex": 0.6, "int": 0.0, "fai": 0.0, "arc": 0.5},
    "passive":    {"bleed": 55, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 14, "dex": 35, "int": 0, "fai": 0, "arc": 17},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Cursed-Blood Slice",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "dragon_halberd", "name": "Drachen-Hellebarde", "nameEN": "Dragon Halberd",
    "category": "halberd", "isSomber": True, "isDLC": False,
    "icon": "🐉", "weight": 10.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 118, "mag": 0, "fire": 0, "light": 72, "holy": 0},
    "maxDamage":  {"phys": 272, "mag": 0, "fire": 0, "light": 166, "holy": 0},
    "scaling":    {"str": 0.6, "dex": 0.5, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 50, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 22, "dex": 10, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Spinning Slash",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "maliketh_blade", "name": "Malikethss Schwarze Klinge", "nameEN": "Maliketh's Black Blade",
    "category": "colossal_sword", "isSomber": True, "isDLC": False,
    "icon": "💀", "weight": 21.0, "physDmgType": "Standard", "critical": 100,
    "baseDamage": {"phys": 120, "mag": 0, "fire": 0, "light": 0, "holy": 78},
    "maxDamage":  {"phys": 283, "mag": 0, "fire": 0, "light": 0, "holy": 185},
    "scaling":    {"str": 0.7, "dex": 0.3, "int": 0.0, "fai": 0.7, "arc": 0.0},
    "passive":    {"bleed": 0, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 34, "dex": 12, "int": 0, "fai": 20, "arc": 0},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Destined Death",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "hand_of_malenia", "name": "Hand der Malenia", "nameEN": "Hand of Malenia",
    "category": "katana", "isSomber": True, "isDLC": False,
    "icon": "🌸", "weight": 7.5, "physDmgType": "Slash", "critical": 100,
    "baseDamage": {"phys": 115, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 265, "mag": 0, "fire": 0, "light": 0, "holy": 0},
    "scaling":    {"str": 0.3, "dex": 1.0, "int": 0.0, "fai": 0.0, "arc": 0.0},
    "passive":    {"bleed": 50, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 16, "dex": 48, "int": 0, "fai": 0, "arc": 0},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Waterfowl Dance",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
  {
    "id": "eleonoras_poleblade", "name": "Eleonoras Stangenklinge", "nameEN": "Eleonora's Poleblade",
    "category": "twinblade", "isSomber": True, "isDLC": False,
    "icon": "🩸", "weight": 6.5, "physDmgType": "Slash", "critical": 100,
    "baseDamage": {"phys": 72, "mag": 0, "fire": 44, "light": 0, "holy": 0},
    "maxDamage":  {"phys": 166, "mag": 0, "fire": 102, "light": 0, "holy": 0},
    "scaling":    {"str": 0.2, "dex": 0.8, "int": 0.0, "fai": 0.0, "arc": 0.6},
    "passive":    {"bleed": 55, "frost": 0, "poison": 0, "rot": 0, "madness": 0, "sleep": 0},
    "req":        {"str": 12, "dex": 21, "int": 0, "fai": 0, "arc": 19},
    "supportedAffinities": ["standard"],
    "defaultSkill": "Bloodblade Dance",
    "patchTag": "1.16.1", "approximationLevel": "estimated"
  },
]

# Neue Kategorien zur WEAPON_CATEGORIES hinzufügen (als Kommentar in JSON)
existing_ids = {w["id"] for w in data["weapons"]}
added = 0
for w in new_weapons:
    if w["id"] not in existing_ids:
        data["weapons"].append(w)
        added += 1
        print(f"  + {w['nameEN']}")
    else:
        print(f"  ~ {w['nameEN']} (bereits vorhanden)")

data["meta"]["total_weapons"] = len(data["weapons"])

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ {added} Waffen hinzugefügt – gesamt: {len(data['weapons'])}")
