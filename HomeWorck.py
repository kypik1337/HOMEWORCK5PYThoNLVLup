# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# def url_ouver(url: str) -> (str, str, str):
#     *way, name = url.split('/')
#     name, extension = name.split('.')
#     way = ''.join(way)
#     return way, name, extension
# progn_url = url_ouver(input('Add ssilky:= '))
# print(f'   WAY    = {progn_url[0]} \n'
#       f'  NAME    = {progn_url[1]} \n'
#       f'EXTENSION = {progn_url[2]} \n')


# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии
# name = ['Ivan', 'Marry', 'Cristmas']
# stats = [10000, 20000, 30000] 
# bones = ["5.05%", "15.25%", "0.55%"]

# def dict_bonus (name: list, stat: list, bonus: list) -> dict:
#         return {n: (s*float(b[:-1]) / 100).__round__(2) for n, s, b in zip(name, stat, bonus)
#             if len(name) == len(stat) == len(bonus)}
# print(dict_bonus(name, stats, bones))


# 4. Создайте функцию генератор чисел Фибоначчи

def fibonacci(num: int):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b
print(list(fibonacci(10)))





