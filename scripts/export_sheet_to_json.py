#!/usr/bin/env python3
import csv
import json
import os
from datetime import datetime, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(ROOT, "data")
OUT_DIR = os.path.join(ROOT, "docs", "data")

WEAPONS_CSV = os.path.join(DATA_DIR, "weapons_base.csv")
REINFORCE_CSV = os.path.join(DATA_DIR, "reinforce_tables.csv")
AFFINITY_CSV = os.path.join(DATA_DIR, "affinity_rules.csv")

def fnum(x, default=0.0):
    try:
        return float(str(x).strip().replace(",", "."))
    except Exception:
        return default

def inum(x, default=0):
    try:
        return int(float(str(x).strip().replace(",", ".")))
    except Exception:
        return default

def s(x, default=""):
    if x is None:
        return default
    v = str(x).strip()
    return v if v != "" else default

def read_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def ensure_dirs():
    os.makedirs(OUT_DIR, exist_ok=True)

def build_weapons():
    rows = read_csv(WEAPONS_CSV)
    weapons = []
    index = []
    seen = set()

    for r in rows:
        wid = s(r.get("id"))
        if not wid:
            continue
        if wid in seen:
            raise ValueError(f"Duplicate id in weapons_base.csv: {wid}")
        seen.add(wid)

        weapon = {
            "id": wid,
            "name": s(r.get("name")),
            "weapon_class": s(r.get("weapon_class")),
            "upgrade_path": s(r.get("upgrade_path"), "unknown"),
            "weight": fnum(r.get("weight"), 0.0),
            "requirements": {
                "str": inum(r.get("req_str"), 0),
                "dex": inum(r.get("req_dex"), 0),
                "int": inum(r.get("req_int"), 0),
                "fth": inum(r.get("req_fth"), 0),
                "arc": inum(r.get("req_arc"), 0),
            },
            "base_damage_plus0": {
                "phys": inum(r.get("base_phys"), 0),
                "mag":  inum(r.get("base_mag"), 0),
                "fire": inum(r.get("base_fire"), 0),
                "ligh": inum(r.get("base_ligh"), 0),
                "holy": inum(r.get("base_holy"), 0),
            },
            # Grade-Letters sind nur Anzeige/QA.
            # Echte Scaling-Curves kommen später aus Regulation Params.
            "scaling_grade_display": {
                "str": s(r.get("scaling_str_grade"), "-"),
                "dex": s(r.get("scaling_dex_grade"), "-"),
                "int": s(r.get("scaling_int_grade"), "-"),
                "fth": s(r.get("scaling_fth_grade"), "-"),
                "arc": s(r.get("scaling_arc_grade"), "-"),
            },
            "meta": {
                "notes": s(r.get("notes")),
                "source": s(r.get("source")),
                "patch_tag": s(r.get("patch_tag")),
            }
        }

        weapons.append(weapon)
        index.append({
            "id": weapon["id"],
            "name": weapon["name"],
            "weapon_class": weapon["weapon_class"],
            "upgrade_path": weapon["upgrade_path"],
            "weight": weapon["weight"],
        })

    return weapons, index

def build_reinforce_tables():
    rows = read_csv(REINFORCE_CSV)
    tables = {}
    for r in rows:
        path = s(r.get("upgrade_path"), "unknown")
        lvl = inum(r.get("level"), 0)
        tables.setdefault(path, {})
        tables[path][str(lvl)] = {
            "base_mult": fnum(r.get("base_mult"), 1.0),
            "scaling_mult": fnum(r.get("scaling_mult"), 1.0),
        }
    return tables

def build_affinity_rules():
    rows = read_csv(AFFINITY_CSV)
    rules = []
    for r in rows:
        rules.append({
            "affinity": s(r.get("affinity")),
            "allowed_on": s(r.get("allowed_on"), "unknown"),
            "base_mult": {
                "phys": fnum(r.get("base_phys_mult"), 1.0),
                "mag":  fnum(r.get("base_mag_mult"), 1.0),
                "fire": fnum(r.get("base_fire_mult"), 1.0),
                "ligh": fnum(r.get("base_ligh_mult"), 1.0),
                "holy": fnum(r.get("base_holy_mult"), 1.0),
            },
            "scaling_mult": {
                "str": fnum(r.get("scaling_str_mult"), 1.0),
                "dex": fnum(r.get("scaling_dex_mult"), 1.0),
                "int": fnum(r.get("scaling_int_mult"), 1.0),
                "fth": fnum(r.get("scaling_fth_mult"), 1.0),
                "arc": fnum(r.get("scaling_arc_mult"), 1.0),
            },
            "notes": s(r.get("notes")),
        })
    return rules

def main():
    ensure_dirs()
    weapons, index = build_weapons()
    reinforce = build_reinforce_tables()
    affinities = build_affinity_rules()

    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "schema": "eldenring_sim_v1",
        "note": "reinforce_tables/affinity_rules are placeholders until regulation params are imported.",
    }

    full = {
        "meta": meta,
        "weapons": weapons,
        "reinforce_tables": reinforce,
        "affinity_rules": affinities,
    }

    with open(os.path.join(OUT_DIR, "weapons_index.json"), "w", encoding="utf-8") as f:
        json.dump({"meta": meta, "weapons_index": index}, f, ensure_ascii=False, indent=2)

    with open(os.path.join(OUT_DIR, "weapons_full.json"), "w", encoding="utf-8") as f:
        json.dump(full, f, ensure_ascii=False, indent=2)

    print("OK: wrote docs/data/weapons_index.json and docs/data/weapons_full.json")

if __name__ == "__main__":
    main()
