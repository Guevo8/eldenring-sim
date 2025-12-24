import csv
from pathlib import Path

import pytest

from scripts import export_sheet_to_json as exporter


def write_csv(tmp_path: Path, filename: str, fieldnames, rows):
    path = tmp_path / filename
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path


def test_build_weapons_creates_expected_structure(monkeypatch, tmp_path):
    fieldnames = [
        "id",
        "name",
        "weapon_class",
        "upgrade_path",
        "weight",
        "req_str",
        "req_dex",
        "req_int",
        "req_fth",
        "req_arc",
        "base_phys",
        "base_mag",
        "base_fire",
        "base_ligh",
        "base_holy",
        "scaling_str_grade",
        "scaling_dex_grade",
        "scaling_int_grade",
        "scaling_fth_grade",
        "scaling_arc_grade",
        "notes",
        "source",
        "patch_tag",
    ]

    rows = [
        {
            "id": "short_sword",
            "name": "Short Sword",
            "weapon_class": "straight_sword",
            "upgrade_path": "standard",
            "weight": "3.0",
            "req_str": "8",
            "req_dex": "10",
            "req_int": "0",
            "req_fth": "0",
            "req_arc": "0",
            "base_phys": "100",
            "base_mag": "0",
            "base_fire": "0",
            "base_ligh": "0",
            "base_holy": "0",
            "scaling_str_grade": "D",
            "scaling_dex_grade": "C",
            "scaling_int_grade": "-",
            "scaling_fth_grade": "-",
            "scaling_arc_grade": "-",
            "notes": "Starter weapon",
            "source": "test",
            "patch_tag": "1.0",
        }
    ]

    path = write_csv(tmp_path, "weapons_base.csv", fieldnames, rows)
    monkeypatch.setattr(exporter, "WEAPONS_CSV", str(path))

    weapons, index = exporter.build_weapons()

    assert weapons == [
        {
            "id": "short_sword",
            "name": "Short Sword",
            "weapon_class": "straight_sword",
            "upgrade_path": "standard",
            "weight": 3.0,
            "requirements": {"str": 8, "dex": 10, "int": 0, "fth": 0, "arc": 0},
            "base_damage_plus0": {"phys": 100, "mag": 0, "fire": 0, "ligh": 0, "holy": 0},
            "scaling_grade_display": {"str": "D", "dex": "C", "int": "-", "fth": "-", "arc": "-"},
            "meta": {"notes": "Starter weapon", "source": "test", "patch_tag": "1.0"},
        }
    ]
    assert index == [
        {
            "id": "short_sword",
            "name": "Short Sword",
            "weapon_class": "straight_sword",
            "upgrade_path": "standard",
            "weight": 3.0,
        }
    ]


def test_build_weapons_detects_duplicate_ids(monkeypatch, tmp_path):
    fieldnames = ["id", "name", "weapon_class", "weight", "req_str", "req_dex", "req_int", "req_fth", "req_arc", "base_phys", "base_mag", "base_fire", "base_ligh", "base_holy", "scaling_str_grade", "scaling_dex_grade", "scaling_int_grade", "scaling_fth_grade", "scaling_arc_grade", "notes", "source", "patch_tag"]
    duplicate_rows = [
        {
            "id": "duplicated",
            "name": "Weapon A",
            "weapon_class": "axe",
            "weight": "5",
            "req_str": "10",
            "req_dex": "0",
            "req_int": "0",
            "req_fth": "0",
            "req_arc": "0",
            "base_phys": "80",
            "base_mag": "0",
            "base_fire": "0",
            "base_ligh": "0",
            "base_holy": "0",
            "scaling_str_grade": "C",
            "scaling_dex_grade": "-",
            "scaling_int_grade": "-",
            "scaling_fth_grade": "-",
            "scaling_arc_grade": "-",
            "notes": "",
            "source": "",
            "patch_tag": "",
        },
        {
            "id": "duplicated",
            "name": "Weapon B",
            "weapon_class": "axe",
            "weight": "6",
            "req_str": "11",
            "req_dex": "0",
            "req_int": "0",
            "req_fth": "0",
            "req_arc": "0",
            "base_phys": "85",
            "base_mag": "0",
            "base_fire": "0",
            "base_ligh": "0",
            "base_holy": "0",
            "scaling_str_grade": "C",
            "scaling_dex_grade": "-",
            "scaling_int_grade": "-",
            "scaling_fth_grade": "-",
            "scaling_arc_grade": "-",
            "notes": "",
            "source": "",
            "patch_tag": "",
        },
    ]

    path = write_csv(tmp_path, "weapons_base.csv", fieldnames, duplicate_rows)
    monkeypatch.setattr(exporter, "WEAPONS_CSV", str(path))

    with pytest.raises(ValueError, match="Duplicate id"):
        exporter.build_weapons()


def test_build_reinforce_tables(monkeypatch, tmp_path):
    fieldnames = ["upgrade_path", "level", "base_mult", "scaling_mult"]
    rows = [
        {"upgrade_path": "standard", "level": "0", "base_mult": "1.0", "scaling_mult": "1.0"},
        {"upgrade_path": "standard", "level": "1", "base_mult": "1.1", "scaling_mult": "1.05"},
        {"upgrade_path": "somber", "level": "1", "base_mult": "1.25", "scaling_mult": "1.2"},
    ]

    path = write_csv(tmp_path, "reinforce_tables.csv", fieldnames, rows)
    monkeypatch.setattr(exporter, "REINFORCE_CSV", str(path))

    tables = exporter.build_reinforce_tables()

    assert tables == {
        "standard": {
            "0": {"base_mult": 1.0, "scaling_mult": 1.0},
            "1": {"base_mult": 1.1, "scaling_mult": 1.05},
        },
        "somber": {
            "1": {"base_mult": 1.25, "scaling_mult": 1.2},
        },
    }


def test_build_affinity_rules(monkeypatch, tmp_path):
    fieldnames = [
        "affinity",
        "allowed_on",
        "base_phys_mult",
        "base_mag_mult",
        "base_fire_mult",
        "base_ligh_mult",
        "base_holy_mult",
        "scaling_str_mult",
        "scaling_dex_mult",
        "scaling_int_mult",
        "scaling_fth_mult",
        "scaling_arc_mult",
        "notes",
    ]
    rows = [
        {
            "affinity": "standard",
            "allowed_on": "all",
            "base_phys_mult": "1.0",
            "base_mag_mult": "1.0",
            "base_fire_mult": "1.0",
            "base_ligh_mult": "1.0",
            "base_holy_mult": "1.0",
            "scaling_str_mult": "1.0",
            "scaling_dex_mult": "1.0",
            "scaling_int_mult": "1.0",
            "scaling_fth_mult": "1.0",
            "scaling_arc_mult": "1.0",
            "notes": "Default",
        },
        {
            "affinity": "keen",
            "allowed_on": "blades",
            "base_phys_mult": "0.95",
            "base_mag_mult": "1.0",
            "base_fire_mult": "1.0",
            "base_ligh_mult": "1.0",
            "base_holy_mult": "1.0",
            "scaling_str_mult": "0.8",
            "scaling_dex_mult": "1.3",
            "scaling_int_mult": "1.0",
            "scaling_fth_mult": "1.0",
            "scaling_arc_mult": "1.0",
            "notes": "Dex-focused",
        },
    ]

    path = write_csv(tmp_path, "affinity_rules.csv", fieldnames, rows)
    monkeypatch.setattr(exporter, "AFFINITY_CSV", str(path))

    rules = exporter.build_affinity_rules()

    assert rules == [
        {
            "affinity": "standard",
            "allowed_on": "all",
            "base_mult": {"phys": 1.0, "mag": 1.0, "fire": 1.0, "ligh": 1.0, "holy": 1.0},
            "scaling_mult": {"str": 1.0, "dex": 1.0, "int": 1.0, "fth": 1.0, "arc": 1.0},
            "notes": "Default",
        },
        {
            "affinity": "keen",
            "allowed_on": "blades",
            "base_mult": {"phys": 0.95, "mag": 1.0, "fire": 1.0, "ligh": 1.0, "holy": 1.0},
            "scaling_mult": {"str": 0.8, "dex": 1.3, "int": 1.0, "fth": 1.0, "arc": 1.0},
            "notes": "Dex-focused",
        },
    ]
