import os
import re

vault_dir = "c:/Users/Hero/Documents/Obsidian Vault/Personagens"
found = []

for file in os.listdir(vault_dir):
    if file.endswith(".md"):
        path = os.path.join(vault_dir, file)
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                if "FOR" in content or "Força" in content:
                    # Look for lines containing FOR, AGI, DES, RES
                    lines = content.split("\n")
                    for i, line in enumerate(lines):
                        if "Força" in line or "FOR" in line or "Agilidade" in line or "AGI" in line:
                            found.append(f"{file}:{i+1}: {line.strip()}")
        except Exception:
            pass

for item in found[:100]:
    print(item)
