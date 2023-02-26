from flask import Flask, make_response, jsonify, request


app = Flask(__name__)

personagens = [
    {'nome':'string',
     'descricao':'string',
     'imagem':'string',
     'programa':'string',
     'animador':'string'
     },
]

@app.route("/characters", methods = ['GET'])
def get_personagens():
    return make_response( jsonify(personagens))

@app.route("/characters", methods = ['POST'])
def create_personagem():
    personagem = request.json
    personagens.append(personagem)
    return "Personagem criado com sucesso"


app.run()