from flask import Flask
from flask import request
from flask import render_template

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

  


@app.route("/form")
def form():
	return render_template("form.html")

@app.route("/clientes",methods=['get'])
def clientes():
	return{"clientes":"Devolviendo todos los clientes"}	

@app.route("/clientes/<id>",methods=['get'])
def cliente(id):
	return{"cliente":{"id":id,"Nombre":"NN"}}

if __name__=='__main__':
	app.run()



 
