import os, re

path = os.path.expanduser("~/dev/portfolio/eldenring-sim/docs/build-manager/index.html")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1) WEAPON_DB hart kodiert raus, durch fetch ersetzen
# Alles zwischen createWeapon-Definition und WEAPON_DB entfernen
# und durch async loader ersetzen

old_db = """const WEAPON_DB = [
  createWeapon({ id:'ruins_gs',"""

# Finde den kompletten WEAPON_DB Block und ersetze ihn
import re

# Entferne den gesamten WEAPON_DB Block (von const WEAPON_DB bis zum schließenden ];)
content = re.sub(
    r'const WEAPON_DB = \[[\s\S]*?\];\s*\nconst DB_VALIDATION',
    'const DB_VALIDATION',
    content
)

# 2) DB_VALIDATION anpassen – läuft jetzt nach dem fetch
old_val = "const DB_VALIDATION = validateAll(WEAPON_DB);"
new_val = "let WEAPON_DB = []; let DB_VALIDATION = { valid: true, count: 0, errors: [], summary: 'Lade...' };"
content = content.replace(old_val, new_val)

# 3) Boot-Logik: fetch einbauen vor ReactDOM.createRoot
old_boot = """window.addEventListener('error', (e) => {
      document.getElementById('root').style.display = 'none';
      const err = document.getElementById('error-screen');
      document.getElementById('error-text').textContent = e.message + '\\n\\n' + (e.filename||'') + ':' + (e.lineno||'');
      err.style.display = 'block';
    });
    try {
      const rootEl = document.getElementById('root');
      if (!rootEl) throw new Error('Root element nicht gefunden');
      ReactDOM.createRoot(rootEl).render(<EldenBuildManagerV13 />);
    } catch(e) {
      document.getElementById('root').style.display = 'none';
      document.getElementById('error-screen').style.display = 'block';
      document.getElementById('error-text').textContent = 'Boot-Fehler: ' + e.message;
    }"""

new_boot = """window.addEventListener('error', (e) => {
      document.getElementById('root').style.display = 'none';
      const err = document.getElementById('error-screen');
      document.getElementById('error-text').textContent = e.message + '\\n\\n' + (e.filename||'') + ':' + (e.lineno||'');
      err.style.display = 'block';
    });

    // Waffen aus JSON laden, dann App starten
    async function bootApp() {
      try {
        const rootEl = document.getElementById('root');
        if (!rootEl) throw new Error('Root element nicht gefunden');

        // Lade-Screen anzeigen
        rootEl.innerHTML = '<div style="display:flex;align-items:center;justify-content:center;min-height:100vh;background:#060606;color:#d4af37;font-family:Georgia,serif;font-size:1.2rem;">⚔️ Lade Waffendaten...</div>';

        // JSON fetchen
        const res = await fetch('../data/weapons_full.json');
        if (!res.ok) throw new Error('Waffendaten konnten nicht geladen werden (HTTP ' + res.status + ')');
        const json = await res.json();

        // Globale WEAPON_DB befüllen
        WEAPON_DB = json.weapons.map(w => createWeapon(w));
        DB_VALIDATION = validateAll(WEAPON_DB);

        if (!DB_VALIDATION.valid) {
          console.warn('⚠️ DB Validierungsfehler:', DB_VALIDATION.errors);
        } else {
          console.log('%c' + DB_VALIDATION.summary, 'color:#22c55e;font-weight:bold');
        }

        // App rendern
        rootEl.innerHTML = '';
        ReactDOM.createRoot(rootEl).render(<EldenBuildManagerV13 />);

      } catch(e) {
        document.getElementById('root').style.display = 'none';
        document.getElementById('error-screen').style.display = 'block';
        document.getElementById('error-text').textContent = 'Boot-Fehler: ' + e.message;
      }
    }

    bootApp();"""

content = content.replace(old_boot, new_boot)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

size = os.path.getsize(path) / 1024
print(f"✅ Frontend auf JSON-fetch umgestellt")
print(f"   Dateigröße: {size:.1f} KB (vorher ~41 KB)")

# Prüfen ob WEAPON_DB noch hart kodiert vorkommt
remaining = content.count("createWeapon({")
if remaining > 1:  # 1 ist die createWeapon-Funktion selbst
    print(f"⚠️ Warnung: {remaining-1} hart kodierte createWeapon() Aufrufe noch vorhanden")
else:
    print("✅ Keine hart kodierten Waffen mehr im Frontend")
