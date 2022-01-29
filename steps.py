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
    distance = int(steps) / 0.762   # is the average distance in meters that equals a step
    distance = round(distance,1)
    
    if not steps:
        return jsonify({'status': 'Number of steps required.'}), 403
    
    db = get_db()
    
    db.execute(
        'INSERT INTO steps (value, distance)'
        ' VALUES (?, ?)',
        (steps, distance,)
    )
    db.commit()

    check = get_db().execute(
        'SELECT timestamp, value, distance'
        ' FROM steps'
        ' ORDER BY timestamp DESC'
    ).fetchone()
    return jsonify({
        'status': 'Steps succesfully recorded/retrieved',
        'data': {
            'timestamp': check['timestamp'],
            'distance in meters': check['distance'],
            'number of steps': check['value']
        }
    }), 200
