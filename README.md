1.
a. What is the application? 
My application is a simple birthday reminder.  It helps users keep track of birthdays and sends them email reminders on the day of the birthday.

b. How to run the program?
1. Download the birthday_reminder.py file.
2. Ensure you have Python installed on your system.
3. Open a terminal or command prompt.
4. Navigate to the directory where birthday_reminder.py is located.
5. Run the program by executing the following command: python birthday_reminder.py

c. How to use the program?
Once the program is running, you can perform the following actions:

In the line 56 you need to change the current email to your email you want to get a reminder to.

To Add a Birthday: To add a birthday to the reminder list, uncomment the reminder.add_birthday('Name', 'YYYY-MM-DD') line in the __main__ block. Replace 'Name' with the name of the person and 'YYYY-MM-DD' with their birthdate. Run the program to add the birthday.

To Remove a Birthday: To remove a birthday from the reminder list, uncomment the reminder.remove_birthday('Name') line in the __main__ block. Replace 'Name' with the name of the person whose birthday you want to remove. Run the program to remove the birthday.

You can add and remove Birthdays editing the data.txt file aswell, that would be a faster way to do that.

To Get Today's Reminders: The program automatically checks for birthdays on the current date and prints any reminders. It also sends email reminders if configured to do so.
2.
● Polymorphism
class BirthdayReminder(Person, metaclass=Singleton): 
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

In this method, send_email from the base class is overridden in the BirthdayReminder class to send a birthday reminder email.

● Abstraction
def import_data(self):
    try:
        with open(self.filename, 'r') as file:
            reader = file.readlines()
            return [{'name': row.split(',')[0], 'date': row.split(',')[1].strip()} for row in reader]
    except FileNotFoundError:
        return []

This method abstracts away the file input/output operations and encapsulates the logic for reading birthday data from a file.

● Inheritance
class Person:
    def __init__(self, name):
        self.name = name

The Person class is a base class, and the BirthdayReminder class inherits from it.

● Encapsulation
def export_data(self):
    with open(self.filename, 'w') as file:
        for b in self.birthdays:
            file.write(f"{b['name']},{b['date']}\n")

The export_data method encapsulates the logic for writing birthday data to a file, hiding the implementation details of file output operations.

● Singleton
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class BirthdayReminder(Person, metaclass=Singleton):
    def __init__(self, filename='data.txt'):
        super().__init__('Birthday Reminder')
        self.filename = filename
        self.birthdays = self.import_data()
        self.server = None

In this code, BirthdayReminder class uses the Singleton pattern. The metaclass=Singleton ensures that only one instance of the BirthdayReminder class is created throughout the program's lifecycle.

● Decorator
def email_authentication(func):
    def wrapper(self, *args, **kwargs):
        if not self.server:
            self.connect_server()
        return func(self, *args, **kwargs)
    return wrapper
Here, email_authentication is a decorator function. It adds the functionality of authenticating the email server before sending an email.

● Reading from a file:
def import_data(self):
    try:
        with open(self.filename, 'r') as file:
            reader = file.readlines()
            return [{'name': row.split(',')[0], 'date': row.split(',')[1].strip()} for row in reader]
    except FileNotFoundError:
        return []

● Writing to a file:
def export_data(self):
    with open(self.filename, 'w') as file:
        for b in self.birthdays:
            file.write(f"{b['name']},{b['date']}\n")
3.
a.
● It was hard to find a working solution for sending emails through gmail with python. Recently Google changed its policies and in order for code to work with gmail you need to allow less secure apps through gmail and set up a separate gmail app password for sending automated emails.

● I struggled to implement unit tests into the code despite trying multiple approaches. Even after watching several tutorials, I couldn't get them to work in any way I tried. I experimented with different methods, meticulously followed step-by-step guides, but the issue persisted. so i gave up.

b.
● So i found out a way to send emails using python code.
● The result of the program meet my expectations, i was able to implement every single function that i was planning to add. And the program works.

c. So the next upgrade for my code would be a separate web site with web interface that would allow people to do the same but with different, more simple UI. The program would have more functionalities aswell like User Authentication, Admin Panel and a separate database for information.

