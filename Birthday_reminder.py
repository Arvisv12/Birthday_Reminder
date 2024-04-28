import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Person:
    def __init__(self, name):
        self.name = name

class BirthdayReminder(Person):
    def __init__(self, filename='data.txt'):
        super().__init__('Birthday Reminder')
        self.filename = filename
        self.birthdays = self.import_data()

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

    def send_email(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('birthdayreminder608@gmail.com', 'bfqv gvso bhgo wlnq')
            msg = MIMEMultipart()
            msg['From'] = 'birthdayreminder608@gmail.com'
            msg['To'] = 'arvydas.abar@gmail.com'
            msg['Subject'] = 'Today is a special day!'
            message = f"{b['name']} has a birthday today!"
            msg.attach(MIMEText(message, 'plain'))
            server.send_message(msg)
            server.quit()
            print('Mail sent')
        except Exception as e:
            print(f"Error sending email: {e}")

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
        reminder.send_email()
