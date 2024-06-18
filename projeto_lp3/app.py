from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    # dependendo da aplicação, os arquivos html serão localizados dentro da pasta 'templates' na raíz do projeto, ou na pasta interior
    return render_template("home.html")

@app.route("/contato")
def pagina_contato():
    return render_template("contato.html")

@app.route("/produtos")
def pagina_produtos():
    lista_produtos = [
        {
            "nome": "coca-cola",
            "descricao": "coca cola espumante"
        },
        {
            "nome": "davi gomes",
            "descricao": "ta aí mano"
        },
        {
            "nome": "doritos",
            "descricao": "saguado",
        },
        {
            "nome": "Torre jenga",
            "descricao": "KK Q NEM O LATORRE"
        },
        {
            "nome": "sei la vey",
            "descricao": "ta aí mano"
        },
        {
            "nome": "doritos",
            "descricao": "de novo sim",
        }
    ]

    # para passar uma variavel, é necessário criar um nome de variável e passar o objeto
    return render_template("produtos.html", produtos=lista_produtos)

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