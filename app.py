from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World"

if __name__ == '__mainn__':
    app.run()