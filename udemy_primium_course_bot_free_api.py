import requests
import os
import pyautogui
import time
import webbrowser
from bs4 import BeautifulSoup
from random import randint

page = requests.get(
    'https://www.real.discount/filter/?category=All&subcategory=All&store=Udemy&duration=All&price=0&rating=All&language=All&search=&submit=Filter').text
page = BeautifulSoup(page)

all = page.find_all(name="div", class_="col-sm-12 col-md-6 col-lg-4 col-xl-4")
all_links = [
    f"https://www.real.discount{link.find(name='a').get('href')}" for link in all]

# for link in all_links:
#     link_page = BeautifulSoup(requests.get(link).text)
#     button = link_page.find('div',{"class": "col-xs-12 col-md-12 col-sm-12 text-center"}).find('a').get('href')
#     print(button)  #short tric is below

udemy_link = [BeautifulSoup(requests.get(link).text).find('div', {
    "class": "col-xs-12 col-md-12 col-sm-12 text-center"}).find('a').get('href') for link in all_links]

print(f"-------------------------page no : {1}-------------------------")
for link in udemy_link:
    print(f"{link}")
    webbrowser.open_new_tab(link)
    time.sleep(7)
    pyautogui.click(1320, 554)
    time.sleep(7)
    pyautogui.click(1487, 460)


for i in range(2, 6):
    print(f"-------------------------page no : {i}-------------------------")
    os.system("taskkill /im firefox.exe /f")
    page = BeautifulSoup(requests.get(
        f'https://www.real.discount/filter/?category=All&subcategory=All&store=Udemy&duration=All&price=0&rating=All&language=All&search=&submit=Filter&page={i}').text)
    all = page.find_all(
        name="div", class_="col-sm-12 col-md-6 col-lg-4 col-xl-4")
    all_links = [
        f"https://www.real.discount{link.find(name='a').get('href')}" for link in all]
    result = [BeautifulSoup(requests.get(link).text).find('div', {
        "class": "col-xs-12 col-md-12 col-sm-12 text-center"}).find('a').get('href') for link in all_links]
    for link in result:
        print(f"{link}")
        webbrowser.open_new_tab(link)
        time.sleep(randint(5, 10))
        pyautogui.click(1320, 554)
        time.sleep(randint(5, 7))
        pyautogui.click(1487, 460)
    time.sleep(5)
    pyautogui.hotkey('altleft','f4')
    # udemy_link.append(result)
