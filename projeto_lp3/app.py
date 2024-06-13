from flask import Flask
from validate_docbr import CPF, CNPJ

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

# Exercicios 
# /servicos retornar "Nossos servicos"
# pagina /gerar-cpf retorna Cpf aleatório
# pagina /gerar-cnpj retorna Cnpj aleatório

@app.route("/servicos")
def pagina_servicos():
    return """
    Nossos Serviços
    <a href=\"/gerar-cpf\">Gerar Cpf</a>
    <a href=\"/gerar-cnpj\">Gerar Cnpj</a>
    <script>
    
        alert('bem vindoooo :3')

    </script>
    """

@app.route("/somar/<int:Number>/<int:Number2>")
def pagina_soma(Number, Number2):
    return f"Soma de {Number} + {Number2} = {Number + Number2}"

@app.route("/gerar-cpf")
def pagina_gerar_cpf():
    return CPF().generate(True)

@app.route("/gerar-cnpj")
def pagina_gerar_cnpj():
    return CNPJ().generate(True)





if __name__ == "__main__":
    app.debug = True
    app.run()