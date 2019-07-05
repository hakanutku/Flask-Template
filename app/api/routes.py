from flask import render_template, jsonify
from app.api import bp


@bp.route('/')
def index():
    name = 'Flask template'
    return render_template('index.html', name=name)


@bp.route('/json_response')
def json_response():
    sample_dict = {
        'name': 'hello',
        'surname': 'world'
    }
    return jsonify(sample_dict)
