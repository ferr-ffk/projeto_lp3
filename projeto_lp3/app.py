from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    # dependendo da aplicação, os arquivos html serão localizados dentro da pasta 'templates' na raíz do projeto, ou na pasta interior
    return render_template("home.html", img_url="https://ogimg.infoglobo.com.br/in/25437349-1bc-b09/FT1086A/98096331_SCCapa-do-album-Motomami-da-cantora-espanhola-Rosalia.jpg")

@app.route("/contato")
def pagina_contato():
    return render_template("contato.html")

@app.route("/produtos")
def pagina_produtos():
    lista_produtos = [
        {
            "nome": "CD Motomami",
            "descricao": "da rosalia diva",
            "img": {
                "url": "https://http2.mlstatic.com/D_Q_NP_760567-MLA49762876220_042022-O.webp",
                "alt": "CD Motomami",
            },
        },
        {
            "nome": "CD KICK ii",
            "descricao": "da arca bafonica",
            "img": {
                "url": "https://assets.boomkat.com/spree/products/811966/large/kick2-cd-b.jpg",
                "alt": "CD da Arca",
            },
        },
        {
            "nome": "CD Do Richard D. James",
            "descricao": "com essa capa assutadora mds",
            "img": {
                "url": "https://d1rgjmn2wmqeif.cloudfront.net/f/2000/327437.png",
                "alt": "asdawd",
            },
        },
    ]

    # para passar uma variavel, é necessário criar um nome de variável e passar o objeto
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/termos-de-uso")
def pagina_termos_uso():
    return render_template("termos-uso.html")

@app.route("/politica-privacidade")
def pagina_politica_privacidade():
    return render_template("politica-privacidade.html")

@app.route("/como-utilizar")
def pagina_como_utilizar():
    return render_template("como-utilizar.html")

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
    return render_template("identificador-gerado.html", id_name="cpf", id_generated=CPF().generate(True))

@app.route("/gerar-cnpj")
def pagina_gerar_cnpj():
    return render_template("identificador-gerado.html", id_name="cnpj", id_generated=CNPJ().generate(True))

if __name__ == "__main__":
    app.debug = True
    app.run()