# eldenring-sim

Mini-Demo: Elden Ring Weapon Simulator (CSV -> JSON Export + Static UI via GitHub Pages).

## Datenquellen
- `data/weapons_base.csv`: Grundwerte der Waffen.
- `data/regulation_params.csv`: Snapshot aus Regulation Params mit echten Reinforce-Tabellen, Affinity-Regeln und Scaling-Kurven.
- `data/reinforce_tables.csv` & `data/affinity_rules.csv`: menschenlesbare Ableitungen derselben Daten (werden beim Export eingelesen, falls das Regulation-Snapshot fehlt).

## Export & lokale Vorschau
```bash
# JSON neu bauen (liest regulation_params.csv und schreibt docs/data/*)
python scripts/export_sheet_to_json.py

# Static UI lokal aufrufen
cd docs && python -m http.server 8000
```

## Berechnungslogik (Kurzfassung)
- Reinforce-Multiplikatoren und Affinity-Regeln werden direkt aus `regulation_params.csv` in die JSON-Dateien übernommen.
- Scaling-Kurven pro Grade (S/E) stammen ebenfalls aus `regulation_params.csv` und werden im Browser linear interpoliert.
- Base Damage = Waffen-Basisschaden × Reinforce `base_mult` × Affinity-Basis-Multiplikatoren.
- Scaling Damage = Base Damage × (Grade-Startwert) × (Kurvenfaktor passend zum Stat) × Reinforce `scaling_mult` × Affinity-Scaling-Multiplikator.
- Zweihändig: STR wird wie im Spiel mit `floor(str * 1.5)` sowohl für Requirement-Check als auch für das Scaling verwendet.
- Wenn Requirements nicht erfüllt sind, wird das Scaling auf Basis des erfüllten Anteils abgeschwächt (Penalty-Faktor).

