from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('steps', __name__, url_prefix='/steps')

@bp.route('/', methods=('GET', 'POST'))
@login_required
def set_steps():
    steps = request.form['steps']
    
    if not steps:
        return jsonify({'status': 'Number of steps required.'}), 403
    
    db = get_db()
    
    db.execute(
        'INSERT INTO steps (value)'
        ' VALUES (?)',
        (steps,)
    )
    db.commit()

    check = get_db().execute(
        'SELECT timestamp, value'
        ' FROM steps'
        ' ORDER BY timestamp DESC'
    ).fetchone()
    return jsonify({
        'status': 'Steps succesfully recorded/retrieved',
        'data': {
            'timestamp': check['timestamp'],
            'Number of steps': check['value']
        }
    }), 200
