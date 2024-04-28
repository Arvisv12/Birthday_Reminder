import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email_authentication(func):
    def wrapper(self, *args, **kwargs):
        if not self.server:
            self.connect_server()
        return func(self, *args, **kwargs)
    return wrapper

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Person:
    def __init__(self, name):
        self.name = name

class BirthdayReminder(Person, metaclass=Singleton):
    def __init__(self, filename='data.txt'):
        super().__init__('Birthday Reminder')
        self.filename = filename
        self.birthdays = self.import_data()
        self.server = None

    def import_data(self):
        try:
            with open(self.filename, 'r') as file:
                reader = file.readlines()
                return [{'name': row.split(',')[0], 'date': row.split(',')[1].strip()} for row in reader]
        except FileNotFoundError:
            return []

    def add_birthday(self, name, date):
        self.birthdays.append({'name': name, 'date': date})
        self.export_data()

    def remove_birthday(self, name):
        self.birthdays = [b for b in self.birthdays if b['name'] != name]
        self.export_data()

    def get_reminders(self):
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        return [b for b in self.birthdays if b['date'] == today]

    @email_authentication
    def send_email(self, name):
        try:
            msg = MIMEMultipart()
            msg['From'] = 'birthdayreminder608@gmail.com'
            msg['To'] = 'arvydas.abar@gmail.com'
            msg['Subject'] = 'Today is a special day!'
            message = f"{name} has a birthday today!"
            msg.attach(MIMEText(message, 'plain'))
            self.server.send_message(msg)
            print('Mail sent')
        except Exception as e:
            print(f"Error sending email: {e}")

    def connect_server(self):
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.starttls()
            self.server.login('birthdayreminder608@gmail.com', 'bfqv gvso bhgo wlnq')
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def export_data(self):
        with open(self.filename, 'w') as file:
            for b in self.birthdays:
                file.write(f"{b['name']},{b['date']}\n")

if __name__ == '__main__':
    reminder = BirthdayReminder()
    
    #reminder.add_birthday('Alice', '2024-04-19')
    #reminder.remove_birthday('Bob')


    print("Today's reminders:")
    for b in reminder.get_reminders():
        print(f"{b['name']} has a birthday today!")
        reminder.send_email(b['name'])
