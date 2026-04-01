from flask import Flask, render_template
import random
app = Flask(__name__)

história_planetas = [
    "Mercúrio é o planeta mais próximo do Sol e tem uma superfície rochosa e cheia de crateras",
    "Vênus é o segundo planeta a partir do Sol e é conhecido por sua atmosfera densa e quente, composta principalmente de dióxido de carbono",
    "Marte é o quarto planeta a partir do Sol e é conhecido como o 'Planeta Vermelho' devido à sua cor característica, causada pela presença de óxido de ferro em sua superfície",
    "Júpiter é o maior planeta do sistema solar e é conhecido por suas faixas de nuvens coloridas e sua grande mancha vermelha, uma tempestade gigante que tem durado por séculos",
    "Saturno é o sexto planeta a partir do Sol e é famoso por seus anéis, compostos principalmente de partículas de gelo e rocha",
    "Urano é o sétimo planeta a partir do Sol e é conhecido por sua cor azul-esverdeada, causada pela presença de metano em sua atmosfera",
    "Netuno é o oitavo planeta a partir do Sol e é conhecido por sua cor azul intensa, causada pela presença de metano em sua atmosfera, e por seus ventos extremamente fortes"
]

fatos_aleátorios = [
    "Sol é uma estrela localizada no centro do nosso sistema solar, e é a fonte de energia para a vida na Terra",
    "A Lua é o único satélite natural da Terra e o quinto maior do sistema solar",
    "Espaço é um ambiente hostil para os seres humanos, com temperaturas extremas, radiação e falta de ar",
    "A Via Láctea é a galáxia onde está localizado o nosso sistema solar, e contém bilhões de estrelas",
    "A Terra é o terceiro planeta a partir do Sol e é o único conhecido por abrigar vida",
    "O universo é vasto e em constante expansão, contendo bilhões de galáxias, cada uma com bilhões de estrelas e planetas",
    "A gravidade é a força que mantém os planetas em órbita ao redor do Sol e é responsável por muitos fenômenos no espaço, como a formação de buracos",
    "A exploração espacial tem permitido que os humanos aprendam mais sobre o universo e desenvolvam tecnologias avançadas, como satélites, telescópios e missões tripuladas a outros planetas"
]
style = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f8ff;
        text-align: center;
        padding: 50px;
    }
    h1 {
        color: #333;
    }
    p {
        font-size: 18px;
        color: #555;
    }
    a {
        display: inline-block;
        margin-top: 20px;
        padding: 10px 15px;
        background-color: #4CAF50;
        color: white;
        text-decoration: none;
        border-radius: 5px;
    }
    a:hover {
        background-color: #45a049;
    }
</style>
"""
@app.route("/")
def home():
    return style + '''
        <h1>🌟Olá!</h1>
        <h2>Aperte F5 Para atualizar!</h2>
        <p>Clique no botão abaixo para ver um fato aleatório:</p>
        <a href="/random_fact">Ver fato aleatório</a>
    '''

@app.route("/planets")
def planets():
    return style + f'''
        <h1>🪐 Planetas</h1>
        <p>{random.choice(história_planetas)}</p>
        <a href="/">Voltar</a>
    '''

@app.route("/random_fact")
def random_fact():
    return style + f'''
        <h1>📚 Fato aleatório</h1>
        <p>{random.choice(fatos_aleátorios)}</p>
        <a href="/">Voltar</a>
    '''

@app.route("/history_planets")
def history_planets():
    return style + f'''
        <h1>🌌 História dos Planetas</h1>
        <p>{random.choice(história_planetas)}</p>
        <a href="/">Voltar</a>
    '''
    

@app.route("/index")
def index():
    return render_template("index.html")

app.run(debug=True)