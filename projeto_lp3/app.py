from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return "<h1>oieeee</h1><p>manooo</p>"

@app.route("/contato")
def pagina_contato():
    return "essa é a pagina de contatooooo"

@app.route("/produtos")
def pagina_produtos():
    return "<h1>produtos</h1>"