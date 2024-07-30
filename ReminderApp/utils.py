from plyer import notification
from pathlib import Path
import json
import os
import outputformat as ouf
import uuid

class Utility:
    def __init__(self):
        self.REFRESH_INTERVAL = 300
        self.notification_file = Path("data.json")
        self.__init_notification_file()

    def __init_notification_file(self):
        if not self.notification_file.exists():
            with open(self.notification_file, "w") as f:
                json.dump({"reminders": []}, f, indent=4)

    @property
    def reminders(self):
        with open(self.notification_file, "r") as f:
            return json.load(f)["reminders"]
        
    @reminders.setter
    def reminders(self, r):
        with open(self.notification_file, "w") as f:
            json.dump({"reminders": r}, f, indent=4)

    @staticmethod
    def send_notification(title, message):
        notification.notify(
            title=title,
            message=message,
            app_name="ReminderApp",
            app_icon="icon.ico",
            timeout=10
        )

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def print_header():
        Utility.clear_screen()
        ouf.bigtitle("ReminderApp")
        ouf.showlist(
            data=["1. Add Reminder", "2. Edit Reminder", "3. View Reminders", "4. Delete Remider", "5. Exit"],
            style="box",
            title="Choose an option"
        )

    def generate_id(self):
        uid = int(str(uuid.uuid4().int)[:4])
        while True:
            if uid in [reminder["id"] for reminder in self.reminders]:
                uid = self.generate_id()
            else:
                break
        return uid