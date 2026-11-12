# class Counter:
#     def __init__(self, value):
#         self.value = value
         
#     def __gt__(self, other):
#         return self.value > other.value
#     def __lt__(self, other):
#         return self.value < other.value
 
     
# counter1 = Counter("rrr")
# counter2 = Counter("пок")
     
# if counter1 > counter2: 
#     print("counter1 больше чем counter2")
# elif counter1 < counter2:
#     print("counter1 меньше чем counter2")
# else: 
#     print("counter1 и counter2 равны")

# class Duck:
#     def swim(self):
#         return "Утка плывёт."

#     def sound(self):
#         return "Кря-кря!"

# class Person:
#     def swim(self):
#         return "Человек плывёт."

#     def sound(self):
#         return "Привет!"

# def describe(entity):
#     print(entity.swim())
#     print(entity.sound())

# describe(Duck())

# while True:
#     a = input()
#     if a == 'stop':
#         break
#     try:
#         a = int(a)
#         if a > 0:
#             print('круто')
#     except ValueError:
#             print('нет')
#             break

# import time

# def timing(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         elapsed = time.time() - start
#         print(f"{func.__name__}: {round(elapsed, 4)} c")
#         return result
#     return wrapper

# @timing
# def calculate_sum(n):
#     return sum(range(n))

# calculate_sum(1_000_000)

# from datetime import datetime, timedelta

# line = "2026-05-27 14:30:42 ERROR disk full"

# logged_at = datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")
# now = datetime(2026, 5, 29, 10, 0)

# print(now - logged_at)

# print(now - logged_at < timedelta(days=4))

# import time

# # Текущий момент как Unix timestamp (секунд с 1 января 1970)
# print(time.time())

# # Пауза на N секунд
# print("Начало")
# time.sleep(2)
# print("Прошло 2 секунды")

from bs4 import BeautifulSoup
import requests

# response = requests.get("https://realpython.github.io/fake-jobs/") #добавляем ссылочку

# soup = BeautifulSoup(response.text, "html.parser") #тут бибилотека, второй аргумент обязательно, работать будет, но не факт

# cards = soup.find_all('div', class_='card-content') #буквально "СУП НАЙЖИ ПЖ ВСЕ ДИВЫ КЛАССА КАРД-КОНТЕНТ"

# cards = cards[0] #тут из кардс выбираем первую карточку

# title = cards.find("h2", class_="title").text.strip()
# company = cards.find('h3', class_='company').text.strip()       #тут легко, создаем переменные, каждой присваием искаемый тег с определенным классом. текст стрип для очистки
# location = cards.find('p', class_='location').text.strip()

# print(title)
# print(company)
# print(location)

response = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('div', class_="col-md-4 country")

#vocabulary = []
countries10 = []
for table in tables:
        title = table.find('h3', class_='country-name').text.strip()
        population = float(table.find('span', class_='country-population').text.strip())
        area = float(table.find('span', class_ = 'country-area').text.strip())
        capital = table.find('span', class_= 'country-capital').text.strip()

        # countries = {"title": title, "population": population, "area": area, "capital": capital}
        # vocabulary.append(countries)

        density = round(population/area) if area > 0 else 0

        countries10.append({
        'name': title,
        'population': population,
        'area': area,
        'density': density,
    })

        top_10 = sorted(countries10, key=lambda x: x['density'], reverse=True)[:15]

for i, country in enumerate(top_10, 1):
  print(f"{i}. {country['name']} — {country['density']} чел./км²")
#print(vocabulary)