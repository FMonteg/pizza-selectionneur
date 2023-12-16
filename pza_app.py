from flask import Blueprint, render_template, request, jsonify
import json
import os

pza_bp = Blueprint('pza', __name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)


@pza_bp.route('/pza')
def pza_select():
    with open('data/pza_compositions.json', 'r') as json_file:
        pizzas = json.load(json_file)
    return render_template('pza_selector.html', title='Sélecteur de pizza', pizzas=pizzas)


@pza_bp.route('/update_pizza_list/<selected_ingredients_json>')
def update_pizza_list(selected_ingredients_json):
    selected_ingredients = json.loads(selected_ingredients_json)

    with open(os.path.join('data', 'pza_ingredients.json'), 'r') as json_file:
        pizza_list = json.load(json_file)

    # Simulate updating the pizza list based on the selected ingredients
    # Replace this logic with your actual backend logic
    updated_pizza_list = []

    for pizza in pizza_list[selected_ingredients[0]]:
        if all(ingredient in pizza_list and pizza in pizza_list[ingredient] for ingredient in selected_ingredients[1:]):
            updated_pizza_list.append(pizza)

    return jsonify(updated_pizza_list)
