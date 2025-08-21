from datetime import datetime, timedelta

def find_open_slots(events, min_block_minutes=60):
    events = sorted(events, key=lambda e: e['start'])

    now = datetime.now().replace(second=0, microsecond=0)
    day_end = now.replace(hour=18, minute=0)

    open_blocks = []
    current = now

    for event in events:
        if event['start'] > current:
            gap = (event['start'] - current).total_seconds() / 60
            if gap >= min_block_minutes:
                open_blocks.append({'start': current, 'end': event['start']})
        if event['end'] > current:
            current = event['end']

    if current < day_end:
        gap = (day_end - current).total_seconds() / 60
        if gap >= min_block_minutes:
            open_blocks.append({'start': current, 'end': day_end})

    return open_blocks