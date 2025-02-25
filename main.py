from flask import Flask, render_template, request
from flask import g
from flask import flash
from forms import RegistroForm
from flask_wtf.csrf import CSRFProtect
import forms 

app = Flask(__name__)
app.secret_key = "Esta es clave secreta"
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.before_request
def before_request():
    g.nombre = "Diego"
    print("Before request 1")
    
@app.after_request
def after_request(response):
    print("After request 3")
    return response

@app.route("/")
def index():
    grupo = "IDGS803"
    lista = ["Juan", "Pedro", "Carlos", "Luis", "Marcos"]
    print("index 2")
    print("Hello {}".format(g.nombre))
    return render_template("index.html", grupo=grupo, lista=lista)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    matricula=""
    edad=""
    nombre=""
    apellido=""
    email=""
    alumno_clase=forms.RegistroForm(request.form)
    if request.method == "POST" and alumno_clase.validate():
        matricula=alumno_clase.matricula.data
        nombre=alumno_clase.nombre.data
        edad=alumno_clase.edad.data
        apellido=alumno_clase.apellido.data
        email=alumno_clase.email.data
        mensaje="Bienvenido {}".format(nombre)
        return render_template("alumnos.html", form=alumno_clase, matricula=matricula, nombre=nombre, edad=edad, apellido=apellido, email=email)


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
    if request.method == "GET":  
        try:
            num1 = int(request.args.get("n1", 0))  
            num2 = int(request.args.get("n2", 0))
            resultado = num1 + num2
        except ValueError:
            resultado = "Error: Ingrese números válidos"
    return render_template("OperasBas.html", resultado=resultado)

@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        nombre = request.form.get("nombre")
        compradores = int(request.form.get("compradores"))
        cantidad_boletos = int(request.form.get("cantidad_boletos"))
        tarjeta_cineco = request.form.get("tarjeta_cineco") == "true"
        
        boletos_maximos = compradores * 7
        if cantidad_boletos > boletos_maximos:
            return render_template("cinepolis.html", 
                                error=f"No puede comprar más de 7 boletos por persona. Máximo permitido: {boletos_maximos}")
        
        precio_base = 12 * cantidad_boletos
        
        if cantidad_boletos > 5:
            descuento = 0.15  
        elif cantidad_boletos >= 3:
            descuento = 0.10  
        else:
            descuento = 0    
        
        precio_con_descuento = precio_base * (1 - descuento)
        
        if tarjeta_cineco:
            precio_final = precio_con_descuento * (1 - 0.10) 
        else:
            precio_final = precio_con_descuento
            
        precio_final = round(precio_final, 2)
            
        return render_template("cinepolis.html",
                             nombre=nombre,
                             compradores=compradores,
                             cantidad_boletos=cantidad_boletos,
                             precio_base=round(precio_base, 2),
                             precio_final=precio_final,
                             descuento_aplicado=descuento * 100,
                             tarjeta_cineco=tarjeta_cineco)
    except Exception as e:
        return render_template("cinepolis.html", error=str(e))
    
    
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)
    