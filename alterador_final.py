from flask import Flask, render_template, request

app = Flask(__name__)

CONFIG = {
    "Português": [
        "mkt",
        "marketing",
        "juridico",
        "contato",
        "atendimento",
        "comercial",
        "sac"
    ],
    "Espanhol": [
        "mkt",
        "marketing",
        "legale",
        "contacto",
        "atendimento",
        "comercial",
        "sac",
        "cac",
        "csa",
        "ayuda"
    ],
    "Inglês": [
        "mkt",
        "marketing",
        "legal",
        "contact",
        "service",
        "commercial",
        "csc",
        "support",
        "csa",
        "help"
    ]
}


@app.route("/", methods=["GET", "POST"])
def index():
    emails = ""
    idioma = "Português"

    if request.method == "POST":
        dominio = request.form.get("dominio", "").strip()
        idioma = request.form.get("idioma")

        if dominio and idioma in CONFIG:
            usuarios = CONFIG[idioma]
            lista_emails = [f"{u}@{dominio}" for u in usuarios]
            emails = ", ".join(lista_emails)

    return render_template("index.html", emails=emails, idioma=idioma)


if __name__ == "__main__":
    app.run()

