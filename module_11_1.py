# Домашнее задание по теме "Обзор сторонних библиотек Python"
# Пример применения библиотеки requests
import requests
print("Пример применения библиотеки - requests:\n")
# 1. Метод get() для выполнения GET-запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# 2. Свойство status_code для проверки статуса ответа
if response.status_code != 200:
    raise Exception(f"Request failed with status code {response.status_code}")

# 3. Метод json() для преобразования ответа в словарь Python
data = response.json()

# 4. Цикл for для итерации по элементам списка
for post in data[:3]:  # Выведем только первые три записи
    # 5. Доступ к ключам словаря для вывода значений
    print(f"ID: {post['id']}, Title: {post['title']}")

# Библиотека requests предоставляет разработчикам удобный интерфейс для работы с HTTP-запросами. Основные преимущества
# этой библиотеки включают:
# Простоту использования. Запросы выполняются всего несколькими строками кода, что делает интеграцию с веб-сервисами быстрой и удобной.
# Поддержку различных типов запросов. Помимо GET-запросов, библиотека также поддерживает POST, PUT, PATCH, DELETE и другие виды запросов.
# Автоматическую обработку JSON. Метод json() автоматически парсит ответы в формате JSON, превращая их в удобные для работы объекты Python.
# Управление сессиями. Библиотека поддерживает работу с сессиями, что полезно для выполнения последовательных запросов с сохранением cookies
# и других параметров.
# Гибкие настройки. Разработчики могут задавать различные параметры запросов, такие как заголовки, параметры URL, тело запроса
# и многое другое.

# Благодаря этим возможностям, requests стала стандартной библиотекой для работы с HTTP в Python, значительно упрощая задачи,
# связанные с взаимодействием с веб-сервисами.

# Пример применение библиотеки requests
import pandas as pd
print("\nПример применения библиотеки - pandas:\n")
# 1. Создаем DataFrame с данными
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# 2. Сохраняем DataFrame в CSV-файл
df.to_csv('test.csv', index=False)

# 3. Читаем данные из CSV-файла
df = pd.read_csv('test.csv')

# 4. Вычисляем средний возраст сотрудников
mean_age = df['Age'].mean()
print(f"Средний возраст сотрудников: {mean_age:.2f} лет")

# 5. Находим сотрудника с максимальной зарплатой
max_salary_index = df['Salary'].argmax()
employee_with_max_salary = df.iloc[max_salary_index]['Name']
print(f"Максимальную зарплату получает сотрудник: {employee_with_max_salary}")

# 6. Группируем данные по возрасту и считаем количество сотрудников в каждой группе
age_groups = df.groupby(['Age']).size().reset_index(name='Count')
print("Количество сотрудников по возрастам:")
print(age_groups)

# Библиотека pandas предоставляет мощные инструменты для работы с табличными данными, включая:
#
# Создание и манипуляция DataFrames: DataFrame — основной объект pandas, представляющий собой двумерную структуру данных,
# аналогичную таблицам в базе данных или электронным таблицам.
# Загрузка и сохранение данных: Поддерживаются различные форматы файлов, такие как CSV, Excel, JSON и многие другие.
# Анализ данных: Методы для агрегирования, группировки, фильтрации и статистического анализа данных.
# Визуализация данных: Хотя pandas сама по себе не предоставляет инструменты для построения графиков, она хорошо интегрируется
# с библиотеками вроде matplotlib и seaborn для визуализации данных.
# Работа с временными рядами: Специальные методы и классы для работы с данными, зависящими от времени.

# pandas значительно расширяет возможности Python для анализа данных, позволяя быстро и эффективно обрабатывать большие
# объемы информации, проводить сложные расчеты и представлять результаты в удобном виде.

# Пример применение библиотеки matplotlib
# import tkinter
# import numpy as np
# import matplotlib.pyplot as plt
# # import numpy as np
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Или 'Qt5Agg'
import matplotlib.pyplot as plt
print("\nПример применения библиотеки - matplotlib:\n")
# 1. Генерируем данные
x = np.linspace(0, 10, 100)
y = x * np.sin(x)

# 2. Вычисляем среднее значение y
mean_y = np.mean(y)
print(f"Среднее значение y: {mean_y:.2f}")

# 3. Строим график
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="sin(x)")
plt.axhline(mean_y, color="red", linestyle="--", label=f"Mean value ({mean_y:.2f})")
plt.title("График функции sin(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
# plt.show()

# Сохраняем график в файл
plt.savefig("graph.png")

# matplotlib предоставляет обширные возможности для визуализации данных, включая:
#
# Разнообразие типов графиков: Поддерживает создание линейных графиков, гистограмм, круговых диаграмм, тепловых карт,
# контурных графиков и многих других.
# Настройка внешнего вида: Позволяет изменять цвета, стили линий, размеры шрифтов, добавлять заголовки, подписи и легенды.
# Интерактивность: Графики могут быть интерактивными, что особенно полезно при работе в Jupyter Notebook.
# Экспорт графиков: Поддерживается экспорт графиков в различные форматы, такие как PNG, PDF, SVG и другие.
# Анимация: Возможность создавать анимационные графики, например, для визуализации изменения данных во времени.

# matplotlib значительно расширяет возможности Python для визуализации данных, предлагая гибкий и мощный инструментарий
# для представления данных в графическом виде.