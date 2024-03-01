from app import app


@app.route("/")
# função da pagina principal
def index(): 
    return "Olá mundo!"
