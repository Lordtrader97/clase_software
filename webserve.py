from flask import Flask
from flask import request
from flask import render_template
import numpy as np

app = Flask(__name__)

@app.route("/",methods=['get','post'])
def hello_world():
	#nombre=request.args.post("nombre")
	#edad=request.args.get("edad")
	nombre=request.form.get("nombre")
	edad=int(request.form.get("edad"))
	if edad >= 18:
		aceptado = True
	else:
		aceptado = False
	return{"aceptado":aceptado}

  
f=0
nombre=[0,0,0,0,0]
apellido=[0,0,0,0]

@app.route("/form")
def form():
	return render_template("form.html")

@app.route("/clientes",methods=['get'])
def clientes():
	global nombre
	return {"Clientes":nombre}	

@app.route("/clientes/<id>",methods=['get'])

def cliente(id):
	global nombre
	return{"cliente":{"id":int(id),"Nombre":nombre[int(id)]}}

@app.route("/register",methods=['post'])
def crear_cliente():
	global f
	global nombre
	global apellido
	nombre[f]=(request.form.get("nombre"))
	apellido[f]=(request.form.get("apellido"))
	print("Creando cliente...")
	f=f+1
	return {"cliente":{"id":f,"nombre":nombre[f-1],"apellido":apellido[f-1]}}


@app.route("/cliente/editar/<id>",methods=['put'])
def editar_cliente(id):
	global nombre
	nombre[int(id)]=(request.form.get("nombre"))
	apellido[int(id)]=(request.form.get("apellido"))
	print("Creando cliente...")
	return {"editando cliente ..":{"id":f,"nombre":nombre[int(id)],"apellido":apellido[int(id)]}}

@app.route("/cliente/editar/nombre/<id>",methods=['put'])
def editar_cliente_nombre(id):
	global nombre
	nombre[id]=(request.form.get("nombre"))
	print("Editando cliente...")
	return {"cliente":{"id":f,"nombre":nombre[id]}}

@app.route("/cliente/borrar/<id>",methods=['delete'])
def eliminar_cliente(id):
	global nombre
	nombre[int(id)]= "sin info"
	apellido[int(id)]= "sin info"
	return {"Cliente eliminado":"ok"}

if __name__=='__main__':
	app.run()



 
