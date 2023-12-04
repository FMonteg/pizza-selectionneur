from flask import Blueprint, render_template, request, jsonify
import json

pza_bp = Blueprint('pza', __name__)


# Initial pizza list
pizza_list = {
    'Tomato': ['Tomato Cheese Pizza', 'Tomato Mushroom Pizza'],
    'Cheese': ['Tomato Cheese Pizza', 'Cheese Mushroom Pizza'],
    'Mushroom': ['Cheese Mushroom Pizza', 'Tomato Mushroom Pizza'],
}


@pza_bp.route('/pza')
def pza_select():
    return render_template('pza_selector.html', title='Sélecteur de pizza')


@pza_bp.route('/update_pizza_list/<selected_ingredients_json>')
def update_pizza_list(selected_ingredients_json):
    selected_ingredients = json.loads(selected_ingredients_json)

    # Simulate updating the pizza list based on the selected ingredients
    # Replace this logic with your actual backend logic
    updated_pizza_list = []

    for pizza in pizza_list[selected_ingredients[0]]:
        if all(ingredient in pizza_list and pizza in pizza_list[ingredient] for ingredient in selected_ingredients[1:]):
            updated_pizza_list.append(pizza)

    return jsonify(updated_pizza_list)
