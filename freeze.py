from flask_frozen import Freezer
from recipe_website import app

freezer = Freezer(app)
app.config['FREEZER_BASE_URL'] = "https://awconstable.github.io/alex-recipes/"

if __name__ == '__main__':
    freezer.freeze()
