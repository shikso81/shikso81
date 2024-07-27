import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from colorama import init
init()
from colorama import Fore, Back, Style
from banner import banner, ikon
from pystyle import *
import os
import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored
import json

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}
with open('senders.json', 'r') as f:
    senders = json.load(f)
receivers = ['stopCA@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner_with_ikon = f"{Colorate.Horizontal(Colors.red_to_white, Center.XCenter(banner))}   {Colorate.Horizontal(Colors.red_to_white, Center.XCenter(ikon))}"
    print(banner_with_ikon)
select = input(f'{COLOR_CODE["RED"]}[+]{COLOR_CODE["BOLD"]} НАЖМИ enter {COLOR_CODE["RED"]} ')
def menu():
    choice = input(f'{COLOR_CODE["RED"]}[+]{COLOR_CODE["BOLD"]} Выбрать >{COLOR_CODE["RED"]} ')
    return choice

def send_email(receiver, sender, password, subject, body):
    if "@gmail.com" in sender:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        service = 'gmail'
    elif "@outlook.com" in sender or "@hotmail.com" in sender or "@live.com" in sender:
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
        service = 'hotmail'
    else:
        raise ValueError("Неподдерживаемый почтовый сервис")

    proxies = {
        'http': '62.33.207.202:80',
        'http': '5.189.184.147:27191',
        'http': '50.221.74.130:80',
        'http': '172.67.43.209:80'
    }

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver
        try:
            with requests.Session() as session:
                session.proxies.update(proxies)
                smtp.send_message(msg)
        except Exception as e:
            print(f"Не удалось отправить сообщение получателю {receiver} через {service}: {e}")
            with open("failed_emails.txt", "a") as f:
                f.write(f"Получатель: {receiver}, Отправитель: {sender}, Тема: {subject}, Сервис: {service}\n")
            
            with open('senders.json', 'r') as f:
                senders = json.load(f)
            if sender in senders:
                with open('invalid_senders.json', 'a') as f:
                    json.dump({sender: password}, f, indent=4)
                del senders[sender]
                with open('senders.json', 'w') as f:
                    json.dump(senders, f, indent=4)
            return

def main():
    sent_emails = 0
    logo()
    choice = menu()
    if choice == '1':
        print("1. Спам.")
        print("2. Доксинг.")
        print("3. Троллинг.")
        print("4. Снос сессий.")
        print("5. С премкой.")
        print("6. С вирт номером.")
        comp_choice = input("-> ")
        if comp_choice in ["1", "2", "3"]:
            print("следуй за указаниям.")
            username = input("юзернейм: ")
            id = input("айди: ")
            chat_link = input("ссылка на чат: ")
            violation_link = input("ссылка на нарушение: ")
            print("Начинаю отправлять жалобы...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я недавно столкнулся с пользователем, который, как мне кажется, занимается массовой рассылкой спама. Его юзернейм - {username}, его айди - {id}, ссылка на чат, где я это наблюдал, - {chat_link}, а вот ссылка на примеры нарушений - {violation_link}. Я бы очень просил вас разобраться с этим случаем и принять необходимые меры в отношении данного пользователя.",
                "2": f"Уважаемая поддержка, на вашей платформе я обнаружил пользователя, который, судя по всему, занимается распространением чужих личных данных без согласия владельцев. Его юзернейм - {username}, айди - {id}, ссылка на чат, где я это заметил, - {chat_link}, а вот ссылка на примеры таких нарушений - {violation_link}. Я прошу вас тщательно разобраться в этом инциденте и предпринять соответствующие меры, вплоть до блокировки аккаунта этого пользователя.",
                "3": f"Добрый день, уважаемая поддержка Telegram. Недавно мне довелось наблюдать, как один из пользователей вашей платформы активно использует нецензурную лексику и занимается спамом в чатах. Его юзернейм - {username}, айди - {id}, ссылка на чат, где я это видел, - {chat_link}, а вот примеры таких нарушений - {violation_link}. Я очень рассчитываю, что вы отреагируете на этот случай и примете надлежащие меры, включая возможную блокировку аккаунта данного пользователя."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    try:
                        comp_text = comp_texts[comp_choice]
                        comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                        violation_link=violation_link.strip())
                        send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                    except Exception as e:
                        print("Не удалось отправить письмо")
                        sent_emails += 14888
                        time.sleep(5)

        elif comp_choice == "4":
            print("следуйте указаниям:")
            username = input("юзернейм: ")
            id = input("айди: ")
            print("Ожидайте...")
            comp_texts = {
                "4": f"Уважаемая поддержка, прошу вас о помощи. Вчера я случайно перешел по ссылке, которая оказалась фишинговой, и в результате потерял доступ к своему аккаунту. Мой юзернейм - {username}, айди - {id}. Я очень прошу вас как можно скорее удалить этот аккаунт или сбросить все сессии, чтобы я мог восстановить доступ и обезопасить свою учетную запись. Заранее благодарен за оперативное рассмотрение моего обращения."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    try:
                        comp_text = comp_texts[comp_choice]
                        comp_body = comp_text.format(username=username.strip(), id=id.strip())
                        send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                    except Exception as e:
                        print("Не удалось отправить письмо")
                        sent_emails += 14888
                        time.sleep(5)

        elif comp_choice in ["5", "6"]:
            print("следуйте указаниям:")
            username = input("юзернейм: ")
            id = input("айди: ")
            comp_texts = {
                "5": f"Добрый день, поддержка Telegram! Я хотел бы сообщить вам, что пользователь с аккаунтом {username} ({id}) использует виртуальный номер, приобретенный на специализированном сайте по активации номеров. Насколько я могу судить, этот номер не имеет к нему никакого отношения. Я очень прошу вас разобраться в этой ситуации. Заранее благодарю за содействие!",
                "6": f"Уважаемая поддержка Telegram! Мне стало известно, что пользователь с аккаунтом {username} ({id}) приобрел премиум-аккаунт в вашем мессенджере с целью рассылки спам-сообщений и обхода ограничений Telegram. Я настоятельно прошу вас проверить эту информацию и принять необходимые меры. Заранее признателен за ваше внимание к данному вопросу."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    try:
                        send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    except Exception as e:
                        print("Не удалось отправить письмо")
                        time.sleep(5)


    elif choice == "2":
        
        print("1. Личные данные.")
        print("2. Живодерство.")
        print("3. Цп.")
        print("4. Прайс каналы.")
        print("5. Наркотики.")
        ch_choice = input("выбор: ")

        if ch_choice in ["1", "2", "3", "4", "5"]:
            channel_link = input("ссылка на канал: ")
            channel_violation = input("ссылка на нарушение (в канале): ")
            print("Ожидайте...")
            comp_texts = {
                "1": f"Уважаемая поддержка Telegram, я обнаружил на вашей платформе канал, который, по всей видимости, занимается распространением личных данных невинных людей. Ссылка на этот канал - {channel_link}, а вот ссылки на конкретные примеры нарушений - {channel_violation}. Убедительно прошу вас оперативно заблокировать данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка Telegram. К сожалению, на вашей платформе я наткнулся на канал, который, кажется, занимается распространением контента, связанного с жестоким обращением с животными. Ссылка на этот канал - {channel_link}, а ссылки на подтверждающие материалы - {channel_violation}. Я очень надеюсь, что вы примете срочные меры по блокировке этого канала.",
                "3": f"Уважаемая поддержка Telegram, мною был обнаружен на вашей платформе канал, который, по имеющимся данным, распространяет порнографический контент с участием несовершеннолетних. Ссылка на этот канал - {channel_link}, а вот ссылки на конкретные примеры таких нарушений - {channel_violation}. Убедительно прошу вас как можно скорее заблокировать данный канал.",
                "4": f"Здравствуйте, уважаемый модератор Telegram. Я хотел бы пожаловаться на канал в вашем мессенджере, который, как мне стало известно, предоставляет услуги по доксингу и сваттингу. Ссылка на этот канал - {channel_link}, а ссылки на подтверждающие материалы - {channel_violation}. Прошу вас незамедлительно заблокировать данный канал.",
                "5": f"Уважаемая поддержка, в вашем мессенджере Telegram я обнаружил канал, который, судя по всему, занимается незаконной продажей наркотических веществ. Айди этого канала - {channel_link}, а вот ссылка на конкретное нарушение - {channel_violation}. Убедительно прошу вас рассмотреть этот вопрос и принять соответствующие меры по блокировке данного канала."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip())
                    try:
                        send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    except Exception as e:
                        print(f"Ошибка при отправке на {receiver} от {sender_email}: {e}")
                        time.sleep(0.5)


    elif choice == "3":
        print("1. Осинт")
        print("2. Наркошоп")
        bot_ch = input("Выберите вариант -> ")

        if bot_ch == "1":
            bot_user = input("юз бота: ")
            print("Ожидайте...")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                "2" :f"Здравствуйте, в вашем мессенджере я наткнулся на бота который производит незаконную торговлю наркотиками. Прошу отреагировать на мою жалобу и принять меры по блокировке данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    try:
                        send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                        print(f"Отправлено на {receiver} от {sender_email}!")
                        sent_emails += 1
                    except Exception as e:
                        print("Не удалось отправить письмо")
                        time.sleep(5)
        
    elif choice == "4":
        comp_text = input("Введите текст своего письма -> ")
        comp_teme = input("Введите тему своего письма -> ")
        for sender_email, sender_password in senders.items():
            for receiver in receivers:
                comp_body = comp_text
                send_email(receiver, sender_email, sender_password, comp_teme, comp_body)
                print(f"Отправлено на {receiver} от {sender_email}!")
                sent_emails += 1
                time.sleep(5)
        
    elif choice == "5":
        device_name = socket.gethostname()
        ip_address = socket.gethostbyname(device_name)
        current_time = datetime.datetime.now()
        url = 'https://telegram.org/support'
        ua = UserAgent()
        yukino = 0
        def send_complaint(text, contact):
            headers = {
                'User-Agent': ua.random
                
            }
            payload = {
                'text': text,
                'contact': contact
                
            }
            proxies = {
                'http': '62.33.207.202:80',
                'http': '5.189.184.147:27191',
                'http': '50.221.74.130:80',
                'http': '172.67.43.209:80',
                
            }
            response = requests.post(url, data=payload, headers=headers, proxies=proxies)
            if response.status_code == 200:
                print(f"Жалоба №", yukino, "отправлена")
            else:
                print(colored(f"Произошла ошибка при отправке жалобы", 'red'))
        text = input("Введите текст жалобы -> ")
        contact = [
            "+79967285422",
            "+79269736273",
            "+79963668355",
            "+79661214909",
            "+79254106650",
            "+22666228126",
            "+79269069196",
            "+79315894431",
            "+79621570718",
            "+79936356488",
            "+79933426488",
            "+79932567875",
            "+79957927875",
            "+79932707875",
            "+79938964840",
            "+79939287875",
            "+79932596488",
            "+79936327082",
            "+79935946212",
            "+79332055767",
            "+79932715767",
            "+79938946212",
            "+79956576212",
            "+79933516212",
            "+79936956212",
            "+79959236212",
            "+79951546212",
            "+79933586212",
            "+79932595767",
            "+79775305892",
            "+79932495767",
            "+79951545767",
            "+79950995767",
            "+79933685767",
            "+79935895767",
            "+79939015767",
            "+79932455767",
            "+79935799337",
            "+79935774933",
            "+79956344119",
            "+79951284119",
            "+79956338805",
            "+79334841905",
            "+79956338515",
            "+79334848505",
            "+79951282057",
            "+79956926093",
            "+79935779943",
            "+79935799335",
            "+79935792057",
            "+79935779433",
            "+79334843012",
            "+79935782057",
            "+79951282609",
            "+79935779733",
            "+79935799331",
            "+79956332057",
            "+79334842609",
            "+79935784119",
            "+79334844119",
            "+79935774119",
            "+79959864119",
            "+79935802057",
            "+79334842057",
            "+79956926096",
            "+79932546212",
            "+79957956488",
            "+79932677875"
            ]
        for numberph in contact:
            yukino += 1
            chosen_text = random.choice(text)
            chosen_contact = random.choice(contact)
            send_complaint(chosen_text, chosen_contact)
            time.sleep(5)
        
    elif choice == "6":
        print("Скоро...")
  
if __name__ == "__main__":
    main()
