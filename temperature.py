from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('temperature', __name__)


@bp.route('/temperature', methods=('GET', 'POST'))
@login_required
def set_temperature():
    if request.method == 'POST':
        temp = request.form['temp']
        error = None

        if not temp:
            return jsonify({'status': 'Temp is required.'}), 403

        print(temp)
        db = get_db()
        db.execute(
            'INSERT INTO temperature (value)'
            ' VALUES (?)',
            (temp,)
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, timestamp, value'
        ' FROM temperature'
        ' ORDER BY timestamp DESC'
    ).fetchone()
    return jsonify({
        'status': 'Temperature succesfully recorded',
        'data': {
            'id': check['id'],
            'timestamp': check['timestamp'],
            'temperature in °C': check['value']
         }
         }), 200