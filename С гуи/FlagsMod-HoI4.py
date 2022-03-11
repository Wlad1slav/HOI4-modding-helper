from PIL import Image
from colorama import init, Fore, Style
import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog


class App(QWidget):
	def __init__(self):
		
		try:
			self.ui = uic.loadUi(os.path.abspath(os.path.dirname(sys.argv[0]))+"/design.ui")
		except:
			input(f'{Fore.RED}Не найден файл дизайна программы!\nОн должен находится в одной папке с программой!\n{Style.RESET_ALL}')
			quit()
		else:
			print('Дизайн программы успешно найден.')

		self.ui.show()

		self.dirlist = None

		self.ui.but_path.clicked.connect(lambda: self.set_path())
		self.ui.start.clicked.connect(lambda: self.start())

		try:
			file = open(os.path.abspath(os.path.dirname(sys.argv[0]))+"/old_path.txt",'r')
			self.dirlist = file.read()
			self.ui.text_path.setText(self.dirlist)
			file.close()
		except FileNotFoundError:
			pass

	
	def set_path(self):

		self.dirlist = QFileDialog.getExistingDirectory(None,"Выбрать папку",".")
		self.ui.text_path.setText(self.dirlist)

		file = open(os.path.abspath(os.path.dirname(sys.argv[0]))+"/old_path.txt",'w')
		file.write(self.dirlist)
		file.close()

	def start(self):

		if self.dirlist != None:
			try:
				files = os.listdir(self.dirlist) #arr
			except:
				print(f"{Fore.RED}Ошибка! Неправильно указан путь.\n{Style.RESET_ALL}")
				return

			try:
				images = filter(lambda x: x.endswith('.tga'), files) 

				#Вот то самое шизовое место
				if len(list(images)) == 0:
					print(f"{Fore.RED}Файлы формата .tga не найдены.{Style.RESET_ALL}")
					return
				else:
					print(len(list(images)) == 0)



				for name in images:
					print(name)
					try:
						flag = Image.open(f"{self.dirlist}\{name}")

						flag = flag.resize((41, 26), Image.ANTIALIAS)
						flag.save(f"{self.dirlist}\medium\{name}")

						flag = flag.resize((10, 7), Image.ANTIALIAS)
						flag.save(f"{self.dirlist}\small\{name}")

						print('.', end='')
					except:
						print(f"{Fore.RED}Ошибка при открытии или форматировании {name}{Style.RESET_ALL}")
						try: errors+=1
						except: errors=1
				print()

			except:
				print(f"{Fore.RED}Ошибка при считывании файлов!\n{Style.RESET_ALL}")

			print(f"{Fore.GREEN}Флаги успешно отформатированы!{Style.RESET_ALL}")
			try: print(f"{Fore.RED}Всего {errors} ошибок при форматировании!{Style.RESET_ALL}")
			except: print(f"{Fore.GREEN}Нет ошибок при форматировании.{Style.RESET_ALL}")



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	app.exec_()