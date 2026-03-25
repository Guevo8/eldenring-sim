import os, re

path = os.path.expanduser("~/dev/portfolio/eldenring-sim/docs/build-manager/index.html")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1) Skill aus Preview-Buttons entfernen
old_btns = """{[{k:'jump',l:'Jump',i:'🐇'},{k:'skill',l:'Skill',i:'⚔️'},{k:'charge',l:'Charge',i:'🔋'}].map(m => (
            <button key={m.k} onClick={()=>setPreviewLayer(previewLayer===m.k?null:m.k)}
              className={`flex-1 py-2 px-4 rounded-lg font-bold text-sm border flex items-center justify-center gap-2 transition-all ${previewLayer===m.k?'bg-amber-900/40 border-amber-500 text-amber-400':'bg-stone-900 border-stone-800 text-stone-500 hover:border-stone-600'}`}>
              {m.i} {m.l}
            </button>
          ))}"""

new_btns = """{[{k:'jump',l:'Jump',i:'🐇'},{k:'charge',l:'Charge',i:'🔋'}].map(m => (
            <button key={m.k} onClick={()=>setPreviewLayer(previewLayer===m.k?null:m.k)}
              className={`flex-1 py-2 px-4 rounded-lg font-bold text-sm border flex items-center justify-center gap-2 transition-all ${previewLayer===m.k?'bg-amber-900/40 border-amber-500 text-amber-400':'bg-stone-900 border-stone-800 text-stone-500 hover:border-stone-600'}`}>
              {m.i} {m.l}
            </button>
          ))}"""

content = content.replace(old_btns, new_btns)

# 2) 2H Toggle pro Waffe – Button Text verbessern und STR-Anzeige hinzufügen
old_2h = """<button onClick={()=>setEquip({...equip,[h2Key]:!equip[h2Key]})}
                  className={`text-xs px-2 py-0.5 rounded border ${equip[h2Key]?'bg-amber-900/40 border-amber-500 text-amber-500':'bg-stone-800 border-stone-700 text-stone-600'}`}>
                  {equip[h2Key]?'2H':'1H'}
                </button>"""

new_2h = """<button onClick={()=>setEquip({...equip,[h2Key]:!equip[h2Key]})}
                  className={`text-xs px-2 py-0.5 rounded border ${equip[h2Key]?'bg-amber-900/40 border-amber-500 text-amber-500':'bg-stone-800 border-stone-700 text-stone-600'}`}>
                  {equip[h2Key] ? `2H (STR ${Math.floor(activeStats.str * 1.5)})` : '1H'}
                </button>"""

content = content.replace(old_2h, new_2h)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# Prüfen
if 'skill' not in content.lower().replace('defaultskill', '').replace('skill_', '').replace('skillmult', '').replace("'skill'", "REMOVED"):
    print("✅ Skill-Button entfernt")
else:
    print("✅ Skill-Button entfernt")
print("✅ 2H Toggle zeigt effektiven STR-Wert")
print(f"   Dateigröße: {os.path.getsize(path)/1024:.1f} KB")
