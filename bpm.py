import heartpy as hp

from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('bpm', __name__, url_prefix='/bpm')


def get_message(bpm):
    message = ""
    if bpm < 60:
        message = "Too Low"
    elif bpm > 120:
        message = "At RISK! Consult your doctor!"
    elif bpm > 90:
        message = "Too high"
    else:
        message = "Healthy"

    return message


@bp.route('/', methods=('GET', 'POST'))
@login_required
def set_bpm():
    if request.method == 'POST':
        data = hp.get_data('data.csv')
        sample_rate = 250
        _, m = hp.process(data, sample_rate)

        bpm = int(m['bpm'])

        if not bpm:
            return jsonify({'status': 'BPM is required.'}), 400

        db = get_db()
        db.execute(
            'INSERT INTO bpm (value)'
            ' VALUES (?)',
            (bpm,)
        )
        db.commit()

    try:
        check = get_db().execute(
            'SELECT id, timestamp, value'
            ' FROM bpm'
            ' ORDER BY timestamp DESC'
        ).fetchone()
        return jsonify({
            'status': 'bpm succesfully recorded/retrieved',
            'data': {
                'id': check['id'],
                'timestamp': check['timestamp'],
                'BPM': check['value'],
                'message': get_message(check['value']),
            }
        }), 200
    except:
        return jsonify({'status': 'No BPM recorded'}), 200
