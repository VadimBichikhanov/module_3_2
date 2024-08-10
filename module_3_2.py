import re

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Define the valid email pattern
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(com|ru|net)$')
    
    # Check if the sender and recipient emails are valid
    if not email_pattern.match(sender) or not email_pattern.match(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    
    # Check if the sender and recipient are the same
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    
    # Check if the sender is the default sender
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса{sender} на адрес {recipient}")

# Example of executed code (tests)
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')