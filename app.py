# Importando as denpendências
from flask import Flask

# Inicializar variáveis e componentes 

# Inicializa o aplicativo Flask (HTTP)
app = Flask(__name__)

# Rota da pagána inicial (rota raiz oui root)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    output = "Sobre nóis..."
    return output
    
# Ativa o modo DEBUG e o main loop no localhost
if __name__ == "__main__":
    app.run(debug=True)

