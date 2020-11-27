# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify

app = Flask('app')

@app.route("/")
def hello():
    return "Hello World in Flask!"

@app.route("/<name>")
def index(name):

    return "Olá {}".format(name), 200

@app.route("/html/<nome>")
def html_page(nome):

    return render_template("html_page.html", nome=nome)

@app.route("/jsonify")
def json_api_jsonify():
    pessoas = [{"nome": "Ana", "idade": 25},
               {"nome": "Claudia", "idade": 26},
               {"nome": "Priscila", "idade": 27},
               {"nome": "Carine", "idade": 28}]

    return jsonify(pessoas=pessoas, total=len(pessoas))

@app.route("/eleicao2020/")
def get_eleitos():
    candidatas = []

    return jsonify(eleitas=candidatas, total=len(candidatas))

app.run(debug=True, use_reloader=True)

if __name__ == "__main__":
    app.run()