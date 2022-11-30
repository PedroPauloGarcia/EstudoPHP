from selenium import webdriver
from datetime import date
import pyautogui
import pyscreenshot
import time

data_atual = date.today()
data_em_texto = '{}-{}-{}'.format(data_atual.day, data_atual.month,
data_atual.year)

print(data_em_texto)

navegador = webdriver.Chrome()
navegador.get("http://localhost/EstudoPHPemCasa/EstudoPHP/projeto/")
navegador.maximize_window()
# navegador.fullscreen_window()

image = pyscreenshot.grab(bbox=(10, 10, 1366, 768)) 
#image.show() 
image.save(r"C:\Users\pedro\Documents\GitHub\Mangueira\foto ad mangueira\ad1_"+data_em_texto+".jpg") 

#from PIL import Image 
#im = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg")  
#im.show()  

# --------------------------------------------------------------------------------------

navegador.get("http://localhost/EstudoPHPemCasa/EstudoPHP/projeto/produtos.php")

time.sleep(2)

image = pyscreenshot.grab(bbox=(10, 10, 1366, 768))  
image.save(r"C:\Users\pedro\Documents\GitHub\Mangueira\foto ad mangueira\ad2_"+data_em_texto+".jpg") 
  
# -----------------------------------------------------------------------------------------

navegador.get("http://localhost/EstudoPHPemCasa/EstudoPHP/projeto/sobre_nos.php")

time.sleep(2)

image = pyscreenshot.grab(bbox=(10, 10, 1366, 768))  
image.save(r"C:\Users\pedro\Documents\GitHub\Mangueira\foto ad mangueira\ad3_"+data_em_texto+".jpg") 

# -----------------------------------------------------------------------------------------

navegador.get("http://localhost/EstudoPHPemCasa/EstudoPHP/projeto/contato.php")

time.sleep(2)

image = pyscreenshot.grab(bbox=(10, 10, 1366, 768))  
image.save(r"C:\Users\pedro\Documents\GitHub\Mangueira\foto ad mangueira\ad4_"+data_em_texto+".jpg") 

# -----------------------------------------------------------------------------------------

