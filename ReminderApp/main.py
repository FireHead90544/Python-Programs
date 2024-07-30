import time
from datetime import datetime
import sys
from utils import Utility
import outputformat as ouf
# from threading import Thread # approach 2
# from timer import reminder_timer # approach 2

utilities = Utility()

def add_reminder():
    utilities.clear_screen()
    ouf.boxtitle("Add a Reminder", style="line")
    title = input(">>> Title: ")
    message = input(">>> Message: ")
    timestamp = input(">>> Time (DD-MM-YYYY HH:MM): ")
    try:
        timestamp = datetime.strptime(timestamp, "%d-%m-%Y %H:%M")
        if timestamp <= datetime.now():
            raise ValueError
        timestamp = timestamp.timestamp()
        reminder = {"id": utilities.generate_id(), "title": title, "message": message, "timestamp": timestamp}
        utilities.reminders = utilities.reminders + [reminder]
    except ValueError:
        ouf.linetitle("\nInvalid Timestamp", style="line")
        time.sleep(2)
        add_reminder()

def edit_reminder():
    utilities.clear_screen()
    ouf.boxtitle("Edit a Reminder", style="line")
    reminder_id = input(">>> Enter the ID: ")
    try:
        reminder_id = int(reminder_id)
        if reminder_id not in [reminder['id'] for reminder in utilities.reminders]:
            raise ValueError
        
        title = input(">>> Title: ")
        message = input(">>> Message: ")
        timestamp = input(">>> Time (DD-MM-YYYY HH:MM): ")

        timestamp = datetime.strptime(timestamp, "%d-%m-%Y %H:%M")
        if timestamp <= datetime.now():
            raise TypeError
        timestamp = timestamp.timestamp()
        edited_reminder = {"id": reminder_id, "title": title, "message": message, "timestamp": timestamp}
        utilities.reminders = list(map(lambda reminder: reminder if reminder['id'] != reminder_id else edited_reminder, utilities.reminders))
    except ValueError:
        ouf.linetitle("\nInvalid ID", style="line")
        time.sleep(2)
        edit_reminder()
    except TypeError:
        ouf.linetitle("\nInvalid Timestamp", style="line")
        time.sleep(2)
        edit_reminder()

def view_reminders():
    utilities.clear_screen()
    ouf.boxtitle("View Reminders", style="line")
    print("\n")
    for reminder in sorted(utilities.reminders, key=lambda x: x["timestamp"]):
        ouf.showlist([reminder['message'], datetime.fromtimestamp(reminder['timestamp']).strftime('%b. %d, %Y | %I:%M %p')], style="line", title=f"{reminder['id']} | {reminder['title']}")
        print('\n')
    input("Press to enter to go back to home screen...")

def delete_reminder():
    utilities.clear_screen()
    ouf.boxtitle("Delete a Reminder", style="line")
    reminder_id = input(">>> Enter the ID: ")
    try:
        reminder_id = int(reminder_id)
        utilities.reminders = list(filter(lambda reminder: reminder['id'] != reminder_id, utilities.reminders))
    except ValueError:
        ouf.linetitle("\nInvalid ID", style="line")
        time.sleep(2)
        delete_reminder()

def take_input_and_perform_action():
    utilities.print_header()
    maps = {
        "1": add_reminder,
        "2": edit_reminder,
        "3": view_reminders,
        "4": delete_reminder,
        "5": sys.exit
    }
    try:
        choice = input(">>> ")
        maps[choice]()
    except KeyError:
        take_input_and_perform_action()

if __name__ == "__main__":
    # timer_thread = Thread(target=reminder_timer) # approach 2
    # timer_thread.start() # approach 2
    while True:
        take_input_and_perform_action()

    # timer_thread.join() # approach 2