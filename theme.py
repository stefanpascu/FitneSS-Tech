from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('theme', __name__, url_prefix='/theme')

@bp.route('/', methods=('GET', 'POST'))
@login_required
def theme():
    # if request.method == 'POST':
    def set_theme():
        theme = request.form['theme']

        if theme != 'dark' and theme != 'light':
            return jsonify({'status': 'Theme can only be set to <dark> or <light>.'}), 400

        if not theme:
            return jsonify({'status': 'Theme is required.'}), 400

        db = get_db()
        
        db.execute(
            'UPDATE theme '
            'SET mode = (?)',
            (theme,)
        )
        db.commit()
        return jsonify({'status': 'Theme successfully changed'}), 200

    def get_theme():
        check = get_db().execute(
            'SELECT id, changed_date, mode'
            ' FROM theme'
            ' ORDER BY changed_date DESC'
        ).fetchone()
        return jsonify({
            'data': {
                'id': check['id'],
                'changed_date': check['changed_date'],
                'theme': check['mode']
            }
        }), 200
        
    if request.method == 'POST':
        return set_theme()
    else:
        return get_theme()
        