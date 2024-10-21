import smtplib
import os
from dotenv import load_dotenv

load_dotenv('.env.py')
password = os.getenv('Password')
login = os.getenv('Login')
login2 = os.getenv('login2')
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)

server.login(login, password)
server.login2(login2)
letter = '''\
From: devmanorg@yandex.ru
To: trosnek@yandex.by
Content-Type: text/plain; charset="UTF-8"
Subject: Важно!

Привет, %friend_name%! %my_name% приглашает вас на сайт %website%!

%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачу. Получаем отзывы от преподавателей.

Как будет проходить ваше обучение на %website%?

→ Попрактикуешься на своих кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут в раунд. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решения наших задач — можно ссылаться на твоём GitHub. Работодатели такое оценят.

Регистрируйся → %website%
На курсы, которые еще не вышли, можно подписаться и получить о релизе сразу на имейл.'''

letter = letter.replace('%website%', 'https://dvmn.org/referrals/trr8ewBBmwwHwghTVxFXK7WOTQc1kDT8W6SbPhA1').replace('%friend_name%', 'Игорь').replace('%my_name%', 'Илья')
letter= letter.encode('utf-8')
server.sendmail(login, login2,letter)

server.quit()