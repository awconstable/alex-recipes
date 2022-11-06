from flask import Flask, render_template

app = Flask(__name__)

recipes = [
    {"id": 1, "title": "Pasta *****", "instructions": [{"step_id": "1", "description": "Step 1: 2 whole eggs, 3 egg yoks, 300g of flower, pich of salt and 2tbsp of oil and blend together for 2 minute's."}, {"step_id": "2", "description": "step 2"}],
     "image_src": "https://images.immediate.co.uk/production/volatile/sites/30/2021/04/Pasta-alla-vodka-f1d2e1c.jpg?resize=768,574"},
    {"id": 2, "title": "Fish and Chips ****", "instructions": [{"step_id": "1", "description": "step 1"}, {"step_id": "2", "description": "step 2"}],
     "image_src": "https://quaysidehotel.co.uk/wp-content/uploads/2022/08/Fish-chips-and-mushy-peas-served-with-a-lemon-slice-from-the-Best-fish-and-chips-restaurant-in-Brixham-Devon-UK-.jpg"},
    {"id": 3, "title": "Burger *****", "instructions": [{"step_id": "1", "description": "step 1"}, {"step_id": "2", "description": "step 2"}],
     "image_src": "data:image/jpeg;base64,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"},
]


@app.route("/")
def home():
    return render_template('index.html', recipes=recipes)


def get_recipe(recipe_id):
    for recipe in recipes:
        if recipe.get("id") == recipe_id:
            return recipe


@app.route("/recipe/<int:recipe_id>.html")
def recipe_page(recipe_id):
    recipe = get_recipe(recipe_id)
    return render_template('recipe.html', recipe=recipe)


if __name__ == "__main__":
    app.run(debug=True)