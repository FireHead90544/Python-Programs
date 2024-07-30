import time
from datetime import datetime
from utils import Utility

utilities = Utility()

def get_next_reminder():
    reminders = sorted(utilities.reminders, key=lambda reminder: reminder['timestamp'])
    current_time = datetime.now()
    for reminder in reminders:
        if datetime.fromtimestamp(reminder['timestamp']) > current_time:
            return reminder

    return None

def sleep_until_next_reminder(reminder):
    current_time = time.time()
    sleep_duration = reminder['timestamp'] - current_time
    if sleep_duration > 0:
        time.sleep(sleep_duration)

def send_reminder_notification(reminder):
    utilities.send_notification(
        title=reminder['title'],
        message=reminder['message']
    )
    utilities.reminders = list(filter(lambda r: r['id'] != reminder['id'], utilities.reminders))

def reminder_timer():
    while True:
        next_reminder = get_next_reminder()
        if next_reminder:
            sleep_time = next_reminder['timestamp'] - time.time()
            if sleep_time > utilities.REFRESH_INTERVAL:
                time.sleep(utilities.REFRESH_INTERVAL)
                continue
            sleep_until_next_reminder(next_reminder)
            send_reminder_notification(next_reminder)
        else:
            time.sleep(utilities.REFRESH_INTERVAL)

if __name__ == "__main__":
    reminder_timer()