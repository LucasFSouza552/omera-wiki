import os

vault_dir = "c:/Users/Hero/Documents/Obsidian Vault/Personagens"
found = []

for file in os.listdir(vault_dir):
    if file.endswith(".md"):
        path = os.path.join(vault_dir, file)
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                if "Vitalidade" in content or "VIT" in content:
                    found.append(f"{file} has Vitalidade")
        except Exception:
            pass

print(found)
