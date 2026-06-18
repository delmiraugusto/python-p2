from flask import Flask
app = Flask(__name__)
@app.route("/")
def inicio():
    return "Minha primeira API Flask"
if __name__ == "__main__":
    app.run(debug=True)