import time
import vk_api
import datetime

time = str(datetime.datetime.now())

print('''
██╗░░░██╗██╗░░██╗░██████╗██╗███╗░░░███╗██╗░░░░░██╗░░░░░███████╗██████╗░██████╗░░█████╗░████████╗
██║░░░██║██║░██╔╝██╔════╝██║████╗░████║██║░░░░░██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
╚██╗░██╔╝█████═╝░╚█████╗░██║██╔████╔██║██║░░░░░██║░░░░░█████╗░░██████╔╝██████╦╝██║░░██║░░░██║░░░
░╚████╔╝░██╔═██╗░░╚═══██╗██║██║╚██╔╝██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗██╔══██╗██║░░██║░░░██║░░░
░░╚██╔╝░░██║░╚██╗██████╔╝██║██║░╚═╝░██║███████╗███████╗███████╗██║░░██║██████╦╝╚█████╔╝░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░
разработчики:
https://vk.com/dsfasdfasdf1
https://vk.com/alekseyagafonov212190
версия - 0.1
	''')

print('''
	Давайте ввойдем для начала в профиль Вконтакте
	Скиньте сюда токен от профилья Вконтакте
	Можете найти свой токен здесь -> https://vkserv.ru/api/token
	''')
token = input('ваш токен:')
vk_session = vk_api.VkApi(token = token)
vk = vk_session.get_api()

print('Вы успешно авторизовались :)')

def bot():
	print('''
		Введи команду comment для накрутки
		Если хочешь завершить работу, напиши exit
		''')
	comm = input()
	if comm == "comment":
		print('---настройка накрутки---')
		poster = input('Введите ID поста, он находится после _:')
		messer = input('Введи сообщения для накрутки:')
		print('''
					Для бота существует два способа накртуи:
					1 - 50 коментариев, есть шансы , что ваш аккаунт не забанят 
					2 - бесконечность, остановка Ctrl + C. Большие риски для блокироваки аккаунта
					''')
		variant = input('Выберите способ накрутки(1, 2): ')
		if variant == "2":
			while True:
				vk.wall.createComment(post_id = poster, message = messer)
				print('Комментарий успешно опубликован! Текст комментария: ', messer)
		if variant == "1":
			for i in range(50):
				try:
					vk.wall.createComment(post_id = poster, message = messer)
					print('Комментарий успешно опубликован! Текст комментария: ', messer)
				except vk_api.exceptions.Captcha:
					print("Ошибка! Вылезла капча! Зайдите на сайт и решите её. Пауза 30 секунд")					
					time.sleep(30)
		else:
			print(' -- Вводите только 1 либо 2! -- ')
	elif comm == "exit":
		print(' -- Бот прекращает свою работу -- ')
		raise SystemExit

if __name__ == '__main__':
    bot()
