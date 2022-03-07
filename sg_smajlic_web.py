import PySimpleGUI as sg
import requests
import webbrowser as w
sg.theme('Python')
link = 'https://sinke100.github.io/smiley/'
page = requests.get(link)
content = page.content.decode()
slika = [ord(i)-127991 for i in content]
slika = [i for i in slika if i>=0]
slika = bytes(slika)
layout = [[sg.Image(slika)]]
win = sg.Window('', layout)
w.open(link)
while True:
	e, v = win.read()
	if e == sg.WIN_CLOSED:
		break 
win.close()
