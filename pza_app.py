from flask import Blueprint, render_template, request
from pza_class import PZA

pza_bp = Blueprint('pza', __name__)


@pza_bp.route('/pza')
def pza_select():
    pza = PZA()
    return render_template('pza_selector.html', title='Sélecteur de pizza')




