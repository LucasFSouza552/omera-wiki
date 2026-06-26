import os

vault_dir = "c:/Users/Hero/Documents/Obsidian Vault"
found = []

for root, dirs, files in os.walk(vault_dir):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    for line_num, line in enumerate(f, 1):
                        if "defesa" in line.lower():
                            found.append(f"{file}:{line_num}: {line.strip()}")
            except Exception:
                pass

for item in found[:100]:
    print(item)
