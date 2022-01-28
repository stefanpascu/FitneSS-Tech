import heartpy as hp
import matplotlib.pyplot as plt

from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('bpm', __name__, url_prefix='/bpm')

@bp.route('/', methods=('GET', 'POST'))
@login_required
def set_bpm():
    if request.method == 'POST':        
        data = hp.get_data('data.csv')
        sample_rate = 250
        _ , m = hp.process(data, sample_rate)
        
        bpm = int(m['bpm'])

        if not bpm:
            return jsonify({'status': 'BPM is required.'}), 403

        db = get_db()
        db.execute(
            'INSERT INTO bpm (value)'
            ' VALUES (?)',
            (bpm,)
        )
        db.commit()

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
            'BPM': check['value']
        }
    }), 200



# TODO:
# Create endpoint that allows to get and change model of bpms (models: cushioned, leather, plastic)