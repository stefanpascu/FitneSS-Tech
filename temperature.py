from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('temperature', __name__)


@bp.route('/temperature', methods=('GET', 'POST'))
@login_required
def temperature():
    def set_temperature():
        temp = request.form['temp']

        if not temp:
            return jsonify({'status': 'Temp is required.'}), 400

        print(temp)
        db = get_db()
        db.execute(
            'INSERT INTO temperature (value)'
            ' VALUES (?)',
            (temp,)
        )
        db.commit()
        return jsonify({'status': 'Temperature successfully recorded'}), 201

    def get_temperature():
        try:
            check = get_db().execute(
                'SELECT id, timestamp, value'
                ' FROM temperature'
                ' ORDER BY timestamp DESC'
            ).fetchone()
            return jsonify({
                'data': {
                    'id': check['id'],
                    'timestamp': check['timestamp'],
                    'temperature': check['value']
                }
                }), 200
        except:
            return jsonify({'status': 'No temperature recorded'}), 200
        
    if request.method == 'POST':
        return set_temperature()
    else:
        return get_temperature()