from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "This will be a pasta recipe.<p>" \
            "<img width='800' height='600' src='https://images.101cookbooks.com/HOMEMADE-PASTA-RECIPE-h.jpg?w=680'>"


if __name__ == "__main__":
    app.run(debug=True)