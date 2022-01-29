from flask import (
    Blueprint, request, jsonify
)
from datetime import date

from auth import login_required
from db import get_db

bp = Blueprint('steps', __name__, url_prefix='/steps')

@bp.route('/', methods=('GET', 'POST'))

@login_required
def steps():
    def set_steps():
        steps = request.form['steps']
        distance = int(steps) / 0.762   # is the average distance in meters that equals a step
        distance = round(distance,1)
        
        if not steps:
            return jsonify({'status': 'Number of steps required.'}), 403
        
        
        db = get_db()
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        try:
            db.execute(
                'INSERT INTO steps (date, value, distance)'
                'VALUES (?, ?, ?)',
                            
                (d1, steps, distance,)
            )
            db.commit()
            
        except:
            db.execute(
                'UPDATE steps '
                'SET value = (?), distance = (?)'
                'WHERE date = (?)',
                (steps, distance, d1,)
            )
            db.commit()
    
        return jsonify({'status': 'Steps successfully recorded'}), 200


    def get_steps():
        try:
            check = get_db().execute(
                'SELECT date, value, distance'
                ' FROM steps'
                ' ORDER BY date DESC'
            ).fetchone()
            return jsonify({
                'data': {
                    'date': check['date'],
                    'distance': check['distance'],
                    'steps': check['value']
                }
            }), 200
        except:
            return jsonify({'status': 'No steps recorded'}), 403
        
    if request.method == 'POST':
        return set_steps()
    else:
        return get_steps()