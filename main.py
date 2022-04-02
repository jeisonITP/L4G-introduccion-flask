from flask import Flask, flash, render_template, request, redirect, url_for
from models import productosModel
from validators import required

app = Flask(__name__)
app.secret_key = 'ElZ7GSMZq@!WNHoF'

@app.get("/")
def inicio():
    productos = productosModel.obtenerProductos()
    
    return render_template("index.html", productos=productos)

@app.get("/form_crear")
def formCrearProducto():
    return render_template("crearProducto.html")

@app.post("/form_crear")
def crearProducto():
    #Recuperar los datos del formulario
    nombre = request.form.get('nombre')
    price = request.form.get('price')
    
    '''response = Validate([
        {
            'value': nombre,
            'validators': 'required,min:8'
        },
        {
            'value': price,
            'validators': 'required,numeric'
        },
    ])
    
    print(response)''' #[] ['El nombre es requerido', 'el precio debe ser un numero']
    
    is_valid = True
    
    if required.isRequired(nombre, 'nombre'):
        is_valid = False
    
    if required.isRequired(price, 'precio'):
        is_valid = False
    
    if not price.isdigit():
        flash("El precio debe ser un numero")
        is_valid = False
    
    if is_valid == False:
        return render_template("crearProducto.html", 
                nombre=nombre,
                price=price,
        )
    
    productosModel.crearProducto(nombre=nombre, price=price)
    #Volver al listado
    return redirect(url_for('inicio'))

@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<int:contactoId>")
def editarContacto(contactoId):
    return render_template("editarContactos.html", id = contactoId)

# /edad/20  Naciste en el año 2000

app.run(debug=True)