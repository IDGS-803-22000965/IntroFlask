from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    grupo = "IDGS803"
    lista = ["Juan", "Pedro", "Carlos", "Luis", "Marcos"]
    return render_template("index.html", grupo=grupo, lista=lista)

@app.route("/hola")
def hola():
    return "Hola"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}"

@app.route("/numero/<int:n>")
def numero(n):
    return "Número: {}".format(n)

@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre: {user} ID: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}".format(n1 + n2)

@app.route("/form1")
def form1():
    return '''
    <form>
        <input type="text" name="nombre" placeholder="Nombre">
        <br>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Nombre">
        <br>
    </form>
    '''

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/operasBas", methods=["GET", "POST"])
def operas():
    resultado = None
    if request.method == "GET":  # Cambié de "POST" a "GET"
        try:
            num1 = int(request.args.get("n1", 0))  # request.args en lugar de request.form
            num2 = int(request.args.get("n2", 0))
            resultado = num1 + num2
        except ValueError:
            resultado = "Error: Ingrese números válidos"
    return render_template("OperasBas.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
    