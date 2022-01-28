from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('theme', __name__, url_prefix='/theme')

@bp.route('/', methods=('GET', 'POST'))
@login_required
def set_theme():
    if request.method == 'POST':
        theme = request.form['theme']

        if theme != 'dark' and theme != 'light':
            return jsonify({'status': 'Theme can only be set to <dark> or <light>.'}), 403

        if not theme:
            return jsonify({'status': 'Theme is required.'}), 403

        db = get_db()
        
        db.execute(
            'UPDATE theme '
            'SET mode = (?)',
            (theme,)
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, changed_date, mode'
        ' FROM theme'
        ' ORDER BY changed_date DESC'
    ).fetchone()
    return jsonify({
        'status': 'Theme succesfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'changed_date': check['changed_date'],
            'theme': check['mode']
        }
    }), 200
