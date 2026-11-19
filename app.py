from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contacto/")
def contacto():
    return render_template("contacto.html")


@app.route("/hola/<nombre>/")
def saludo(nombre):
    return render_template("saludo.html", nombre=nombre)


@app.route("/cursos/")
def cursos():
    lista_cursos = ["Entornos de Control", "Analisis de Datos", "Programación orientada a objetos"]
    return render_template("cursos.html", cursos=lista_cursos)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    # Solo para desarrollo. En un servidor real se usa gunicorn (paso 9).
    app.run(debug=True)
