from fake_calendar import load_sample_events
from productivity_model import find_open_slots
from datetime import datetime


def run():
    events = load_sample_events()
    blocks = find_open_slots(events)

    print("\n🔁 Deep Work Scheduling – CLI View")
    print("-----------------------------------")

    if not blocks:
        print("⚠️ No available blocks today.")
        return

    for i, block in enumerate(blocks, start=1):
        start = block['start'].strftime('%I:%M %p')
        end = block['end'].strftime('%I:%M %p')
        duration = (block['end'] - block['start']).seconds // 60
        print(f"{i}. {start} → {end}  | {duration} min")


if __name__ == "__main__":
    run()