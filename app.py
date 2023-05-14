from flask import Flask
from controllers.routes import routes

app = Flask(__name__)

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)

#este é aquele arquivo python que Fred tinha passado para nós, onde colocaríamos as rotas etc., 
#esse register_blueprint é, ao que parece, uma biblioteca que facilita a exportação de rotas pra que não 
#seja necessário fazer aquela função init_app