from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/",methods=['get','post'])
def hello_world():
	#nombre=request.args.post("nombre")
	#edad=request.args.get("edad")
	nombre=request.form.get("nombre")
	edad=request.form.get("edad")
	return render_template("bienvenido.html",nombre=nombre,edad=edad)
  


@app.route("/form")
def form():
	return render_template("form.html")
if __name__=='__main__':
	app.run()



 
