from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola Mundo, aqui ismael polanco (Matricula 2021-0293)!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
#ismael polanco