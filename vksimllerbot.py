import time
import vk_api
import datetime
import json
import random
import colorama
from colorama import Fore, Style
import smtplib as root
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

list_citat = [" — Какой твой любимый ужастик?", 
"Ты сейчас один дома ?", 
"""— Кто же ты?
— Вопрос не в том, кто я... А в том, где я...
— И где же ты?
— Возле парадного входа.
— Тогда зачем же ты звонишь?
— Это неотъемлемая часть любого ужастика.""" , 
"""
— Кто там? Кто там?
— Никогда не спрашивай «кто там?» Ты же смотришь ужасы? Это желание смерти... Еще бы вышла и проверила, что тут за странные звуки.
""",
"""
- Существует очень простая формула для выявления убийцы. Все являются подозреваемыми!
""",
"""
— Вы больные отморозки, помешанные на фильмах.
— Не смей винить фильмы! Не они создают психов, они лишь делают их более изобретательными.""",
"- Я слежу за тобой...",
"""

- Ало!
- Привет мелкий, что ты делаешь ?
- Нихрена, лежу , смотрю редак, всасываю косек
- Ты тоже совсем один ?
- Э-э-э-э-э-э-й чува-а-а-а-а-ак
- Чуваа-а-а-а-а-а-ак
- Что это ? Кто там?
- Эй, возьми трубку!
- Эй! Чува-а-а-а-а-а-а-а-а-а-а-а-ак
- Чуваа-а-а-а-а-а-а-а-а-а-а-а-а-а-ак
- Эй, Дуги! Возьму трубку!
- Йоу!
- Чуваа-а-а-а-а-а-а-а-а-ак
- Чуваа-а-а-а-а-а-а-а-а-а-а-а-а-а-а-ак
- Чуваа-а-а-а-а-а-а-а-а-а-а-а-а-а-а-ак
- Эй-ха-ха-ха-ха
- А ты что делаешь ?
- Ничего, скучаю, убиваю!
- Ну.. бывает

""",
]

print('''
		Давайте ввойдем для начала в профиль Вконтакте
		Можете найти свой токен здесь -> https://vkserv.ru/api/token
		Скопируй ссылку полностью и вставь сюда
		UPD:Токен действует ровно 24 часа с момента создания 
	''')
token = input('ваша ссылка:')
print("ваш токен:" + "[    " + token[43:241] + "    ]")
vk_session = vk_api.VkApi(token = token[43:241])
vk = vk_session.get_api()

vk_session = vk_api.VkApi()





	# имя файла
FILENAME = "tokens.txt"
# определяем пустой список
messages = list()
 
for i in range(1):
	message = token[43:241]
	messaf = token[263:272]
	messages.append("user ID - :" + messaf + "\nВаш токен:\n"+ message + "\n")

	# запись списка в файл
with open(FILENAME, "a") as file:
	for message in messages:
		file.write(message)

print('Вы успешно авторизовались :)')

print("Для того чтоб начать, напишите start.")
colorama.init()
sta = input(":")
if sta =="start":

	print(Fore.RED + '''

	██╗░░░██╗██╗░░██╗░██████╗██╗███╗░░░███╗██╗░░░░░██╗░░░░░███████╗██████╗░██████╗░░█████╗░████████╗
	██║░░░██║██║░██╔╝██╔════╝██║████╗░████║██║░░░░░██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
	╚██╗░██╔╝█████═╝░╚█████╗░██║██╔████╔██║██║░░░░░██║░░░░░█████╗░░██████╔╝██████╦╝██║░░██║░░░██║░░░
	░╚████╔╝░██╔═██╗░░╚═══██╗██║██║╚██╔╝██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗██╔══██╗██║░░██║░░░██║░░░
	░░╚██╔╝░░██║░╚██╗██████╔╝██║██║░╚═╝░██║███████╗███████╗███████╗██║░░██║██████╦╝╚█████╔╝░░░██║░░░
	░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░
''')
print(Style.RESET_ALL)

print(Fore.RED + random.choice(list_citat))

print(Style.RESET_ALL)
print('''
	============
	версия - 2.1
	=====================
	команды:
	1. меню - /help
	2. разработчики и тестировщики /test
	3. начать /start
	4. выход /exit
	5. открыть БД токенов /tok
	6. что за бот? /bot
	=====================
		''')

while True:
	yoy = input('====>')
	if yoy == "/start" :

		def bot():
			print('''
				Введи команду comment для накрутки
				Если хочешь завершить работу, напиши exit
				''')
			comm = input(':')
			if comm == "comment":
				print('---настройка накрутки---')
				id_gri = input('Введи айди страницы:')
				id_poster = input('Введите ID поста, он находится после _:')
				messer = input('Введи сообщения для накрутки:')
				print('''
							Для бота существует два способа накртуи:
							1 - бесконечность, остановка Ctrl + C. Большие риски для блокироваки аккаунта
							2 - 5 коментариев, есть шансы , что ваш аккаунт не забанят 
							3 - свое количесвто, но не больше 50
							
							''')
				variant = input('Выберите способ накрутки(1, 2 или 3): ')
				if variant == "1":
					while True:
						vk.wall.createComment(owner_id= id_gri, post_id = id_poster, message = messer)
						print('Комментарий успешно опубликован! Текст комментария: ', messer)
				if variant == "2":
					for i in range(5):
						try:
							vk.wall.createComment(owner_id= id_gri, post_id = id_poster, message = messer)
							print('Комментарий успешно опубликован! Текст комментария: ', messer)
						except vk_api.exceptions.Captcha:
							print("Ошибка! Вылезла капча! Зайдите на сайт и решите её. Пауза 30 секунд")					
							time.sleep(30)

				if variant =="3":
					num = int(input("Введите количесвто, но не больше 50:"))
					for i in range(num):
						try:
							vk.wall.createComment(owner_id = id_gri, post_id = id_poster, message = messer)
							print('Комментарий успешно опубликован! Текст комментария: ', messer)
						except vk_api.exceptions.Captcha:
							print("Ошибка! Вылезла капча! Зайдите на сайт и решите её. Пауза 30 секунд")					
							time.sleep(30)
				else:
					print(' -- Вводите только 1 либо 2! -- ')

		if __name__ == '__main__':
			bot()

	if yoy =="/test":
		print("""
		тестировщики - ЕЩЕ НИ КТО НЕ ТЕСТИРОВАЛ
		разработчики:
		https://vk.com/dsfasdfasdf1 ( Артем )
		https://vk.com/alekseyagafonov212190 ( Алексей )
				""")
	if yoy =="/help":
		print("""
		команды:
		1. меню - /help
		2. разработчики и тестировщики /test
		3. начать /start
		4. выход /exit
		5. открыть БД токенов /tok
		6. что за бот? /bot
				""")
	elif yoy == "/exit":
			print(' -- Бот прекращает свою работу -- ')
			raise SystemExit
	if yoy == "/tok":
		with open("tokens.txt", "r") as file:
			for line in file:
				print(line, end="")
	if yoy == "/clear":
		open('tokens.txt', 'w').close()
		print("База Данных токенов успешно очищена!\nМожите заполнять их новыми :)")
	if yoy =="/bot":
		print("""
		Этот бот создан для накрутки комментариев от лица пользователя(страницы вк)

		В последующих обновлениях будет добавлено:
		1 - накрутка коммнтраев от лица сообщества
		2 - накрутка на посты сообществ
		3 - накрутка лайков на посты от всех лиц ( от пользователя и от сообщества )
		4 - версия в GUI(Графический интерфейс)

		VKSIMLLERBOT
		Version: 2.1
			""")

