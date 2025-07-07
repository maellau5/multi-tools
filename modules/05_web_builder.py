# 05_web_builder.py
# Générateur HTML simple

def build_webpage(title, description, button_text):
    html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    <p>{description}</p>
    <button>{button_text}</button>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("✅ Fichier 'index.html' généré avec succès.")

if __name__ == "__main__":
    print("=== Web Builder ===")
    title = input("Titre de la page : ")
    description = input("Description : ")
    button_text = input("Texte du bouton : ")

    build_webpage(title, description, button_text)
