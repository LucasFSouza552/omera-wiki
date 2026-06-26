import os
import re
import sys

personagens_dir = "c:/Users/Hero/Documents/Obsidian Vault/Personagens"

chars = []

for file in os.listdir(personagens_dir):
    if file.endswith(".md") and file != "Personagens.md":
        name = file[:-3]
        path = os.path.join(personagens_dir, file)
        
        # Default metadata
        especie = "—"
        classe = "—"
        status = "—"
        afiliacao = "—"
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                
                # Try parsing from table format: | **Espécie:** [[Humano]] |
                esp_match = re.search(r"\*\*Esp\u00e9cie:\*\*?\s*(\[\[[^\]]+\]\]|[^|\n\r]+)", content)
                if esp_match:
                    especie = esp_match.group(1).strip()
                
                class_match = re.search(r"\*\*Classe:\*\*?\s*([^|\n\r]+)", content)
                if class_match:
                    classe = class_match.group(1).strip()
                    
                status_match = re.search(r"\*\*Status:\*\*?\s*([^|\n\r]+)", content)
                if status_match:
                    status = status_match.group(1).strip()
                    
                af_match = re.search(r"\*\*Afilia\u00e7\u00e3o:\*\*?\s*([^|\n\r]+)", content)
                if af_match:
                    afiliacao = af_match.group(1).strip()
                elif "Origem:" in content:
                    orig_match = re.search(r"\*\*Origem:\*\*?\s*([^|\n\r]+)", content)
                    if orig_match:
                        afiliacao = orig_match.group(1).strip()
        except Exception:
            pass
            
        chars.append({
            "name": name,
            "especie": especie,
            "classe": classe,
            "status": status,
            "afiliacao": afiliacao
        })

# Sort alphabetically by character name
chars.sort(key=lambda x: x["name"].lower())

out = []
out.append("---")
out.append("sticker: emoji//1f465")
out.append("tags:")
out.append("  - index")
out.append("  - personagens")
out.append("---")
out.append("")
out.append("# \u00cdndice de Personagens")
out.append("")
out.append("Esta p\u00e1gina lista todas as fichas de personagens ativos, coadjuvantes, entidades e vil\u00f5es da campanha **Guardi\u00f5es: O Despertar do Abismo**.")
out.append("")
out.append("| Personagem | Esp\u00e9cie | Classe / Fun\u00e7\u00e3o | Afilia\u00e7\u00e3o / Origem | Status |")
out.append("| :--- | :--- | :--- | :--- | :--- |")

for c in chars:
    out.append(f"| [[Personagens/{c['name']}\\|{c['name']}]] | {c['especie']} | {c['classe']} | {c['afiliacao']} | {c['status']} |")

sys.stdout.reconfigure(encoding='utf-8')
print("\n".join(out))
