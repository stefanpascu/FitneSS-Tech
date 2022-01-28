from db import get_db

def get_status():
    bpm = get_db().execute(
        'SELECT id, timestamp, value'
        ' FROM bpm'
        ' ORDER BY timestamp DESC'
    ).fetchone()

    theme = get_db().execute(
        'SELECT id, changed_date, mode'
        ' FROM theme'
        ' ORDER BY changed_date DESC'
    ).fetchone()

    if bpm is None:
        return {'status': 'Please measure your bpm first'}

    if theme is None:
        return {'status': 'Please select a theme between <dark> and <light>'}

    return {
        'data': {
            'bpm': bpm['value'],
            'theme': {
                'last_changed': theme['changed_date'],
                'mode': theme['mode']
            }
        }
    }