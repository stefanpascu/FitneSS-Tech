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
    
    steps = get_db().execute(
        'SELECT date, value, distance'
        ' FROM steps'
        ' ORDER BY date DESC'
    ).fetchone()
    
    temperature = get_db().execute(
        'SELECT id, timestamp, value'
        ' FROM temperature'
        ' ORDER BY timestamp DESC'
    ).fetchone()
    
    sleep = get_db().execute(
        'SELECT date, totalvalue, remvalue'
        ' FROM sleep'
        ' ORDER BY date DESC'
    ).fetchone()

    bpmMsg, stepsMsg, temperatureMsg = "", "", ""
    
    if bpm is None:
        bpmMsg = 'No bpm recorded'
    else:
        bpmMsg = str(bpm['value'])
        
    if steps is None:
        stepsMsg = 'No steps recorded'
        distanceMsg = 'No distance recorded'
    else:
        stepsMsg = str(steps['value'])
        distanceMsg = str(steps['distance'])
    
    if temperature is None:
        temperatureMsg = 'No temperature recorded'
    else:
        temperatureMsg = str(temperature['value'])

    if sleep is None:
        totalsleepMsg = 'No sleep recorded'
        remsleepMsg = 'No sleep recorded'
    else:
        totalsleepMsg = str(sleep['totalvalue'])
        remsleepMsg = str(sleep['remvalue'])

    return {
        'status': {
            'bpm': bpmMsg,
            'theme': theme['mode'],
            'steps': stepsMsg,
            'distance': distanceMsg,
            'temperature': temperatureMsg,
            'sleep': {
                'total hours of sleep': totalsleepMsg,
                'hours of rem sleep': remsleepMsg,  
            }
        }
    }