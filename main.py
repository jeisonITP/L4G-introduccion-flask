from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port=3306,
    database='productos'
)
db.autocommit = True

app = Flask(__name__)

@app.get("/")
def inicio():
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("select * from productos")
    productos = cursor.fetchall() #Obtener todo
    #producto = cursor.fetchone() 
    
    cursor.close()
    
    return render_template("index.html", productos=productos)

@app.get("/form_crear")
def formCrearProducto():
    return render_template("crearProducto.html")

@app.post("/form_crear")
def crearProducto():
    #Recuperar los datos del formulario
    nombre = request.form.get('nombre')
    price = request.form.get('price')
    
    #Insertar los datos en la base de datos
    cursor = db.cursor()
    
    cursor.execute("insert into productos(nombre, price) values(%s, %s)", (
        nombre,
        price,
    ))
    
    cursor.close()
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