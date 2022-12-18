from flask import Flask, render_template

app = Flask(__name__)

# criar a primeira página do site
# toda página tem uma route e uma função
# Precisa ter uma pasta "templates" para acomodar os templates de cada página HTML/CSS

@app.route("/")    
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

if __name__=="__main__":

    app.run(debug=True) #colocar o site no ar
