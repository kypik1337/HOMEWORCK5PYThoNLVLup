# Задание Nº3
# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

text = 'Создайте из строки словарь, где ключ — буква, а значение — код буквы.'
my_dict = {symbol: ord(symbol) for symbol in set(text)}
my_dict_iterator = iter(my_dict.items())
count = 5

for _ in range(count):
    print(*next(my_dict_iterator))










