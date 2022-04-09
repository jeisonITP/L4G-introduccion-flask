from flask import Flask, flash, render_template, request, redirect, url_for, session
from models import productosModel
from validators import required

app = Flask(__name__)
app.secret_key = 'ElZ7GSMZq@!WNHoF'

@app.get("/")
def inicio():
    if not 'user_id' in session:
        return redirect(url_for('loginForm'))
    
    print('el usuario es:' + str(session['user_id']))
    
    productos = productosModel.obtenerProductos()
    
    return render_template("index.html", productos=productos)

@app.get("/form_crear")
def formCrearProducto():
    return render_template("crearProducto.html")

@app.post("/form_crear")
def crearProducto():
    imagen = request.files['imagen']
    
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
    
    if not required.isRequired(nombre, 'nombre'):
        is_valid = False
    
    if not required.isRequired(price, 'precio'):
        is_valid = False
    
    if not price.isdigit():
        flash("El precio debe ser un numero")
        is_valid = False
    
    if is_valid == False:
        return render_template("crearProducto.html", 
                nombre=nombre,
                price=price,
        )
        
    nombre_imagen = imagen.filename
    
    imagen.save('./static/imagen/' + nombre_imagen)
    
    productosModel.crearProducto(nombre=nombre, price=price, imagen='/static/imagen/' + nombre_imagen)
    #Volver al listado
    return redirect(url_for('inicio'))

@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<int:contactoId>")
def editarContacto(contactoId):
    return render_template("editarContactos.html", id = contactoId)

@app.get('/login')
def loginForm():
    return render_template('login.html')

@app.post('/login')
def loginPost():
    #Validar que las credenciales sean correctas
    
    user_id = 5
    
    #Crear la sesion
    session['user_id'] = user_id
    
    
    return 'Se ha iniciado sesion'

@app.get('/cerrar_sesion')
def cerrarSesion():
    
    session.clear()
    
    return redirect(url_for('loginForm'))

app.run(debug=True)