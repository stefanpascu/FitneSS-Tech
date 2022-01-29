from datetime import date
from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('sleep', __name__, url_prefix='/sleep')


@bp.route('/', methods=('GET', 'POST'))

@login_required
def sleep():
    def set_sleep():
        totalsleep = request.form['total']
        remsleep = request.form['rem']

        if not totalsleep:
            return jsonify({'status': 'number of hours of total sleep is required.'}), 403
        
        if not remsleep:
            return jsonify({'status': 'number of hours of rem sleep is required.'}), 403

        print(totalsleep)
        print(remsleep)
        db = get_db()
        today = date.today()
        d1 = today.strftime("%Y-%m-%d")
        try:
            db.execute(
                'INSERT INTO sleep (date, totalvalue, remvalue)'
                'VALUES (?, ?, ?)',
                            
                (d1, totalsleep, remsleep,)
            )
            db.commit()
            
        except:
            db.execute(
                'UPDATE sleep '
                'SET totalvalue = (?), remvalue = (?)'
                'WHERE date = (?)',
                (totalsleep, remsleep, d1,)
            )
        db.commit()
        return jsonify({'status': 'Number of hours of sleep successfully recorded'}), 200

    def get_sleep():
        try:
            check = get_db().execute(
                'SELECT date, totalvalue, remvalue'
                ' FROM sleep'
                ' ORDER BY date DESC'
            ).fetchone()
            return jsonify({
                'data': {
                    'date': check['date'],
                    'total sleep': check['totalvalue'],
                    'rem sleep': check['remvalue']
                }
            }), 200
        except:
            return jsonify({'status': 'No sleep recorded'}), 403
      
    if request.method == 'POST':
        return set_sleep()
    else:
        return get_sleep()