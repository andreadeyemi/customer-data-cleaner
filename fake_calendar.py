from datetime import datetime, timedelta

def load_sample_events():
    now = datetime.now().replace(second=0, microsecond=0)
    return [
        {'start': now.replace(hour=9), 'end': now.replace(hour=10, minute=30)},
        {'start': now.replace(hour=12), 'end': now.replace(hour=13)},
        {'start': now.replace(hour=14), 'end': now.replace(hour=15, minute=30)}
    ]