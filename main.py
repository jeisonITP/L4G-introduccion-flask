from flask import Flask, render_template
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

@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<int:contactoId>")
def editarContacto(contactoId):
    return render_template("editarContactos.html", id = contactoId)

# /edad/20  Naciste en el año 2000

app.run(debug=True)