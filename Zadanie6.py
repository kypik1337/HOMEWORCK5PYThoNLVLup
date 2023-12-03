# Задание №6
# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного генератора,
# где каждый элемент генератора — отдельный пример таблицы умножения.
# Для вывода результата используйте «принт»
# без перехода на новую строку.

LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMN = 4
ONE = 1


for i_main in (LOWER_LIMIT, LOWER_LIMIT + COLUMN):
    for second_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE):
        for first_num in range(i_main, i_main + COLUMN):
            print(f'{first_num:>3} X {second_num:>3} = {first_num * second_num:>2} ', end='\t')
        print()
    print()


table_generator = (f'{first_num:>2} X {second_num:>2} = {first_num * second_num:>2}  \t' if first_num < i_main + COLUMN - ONE else
                   f'{first_num:>2} X {second_num:>2} = {first_num * second_num:>2}\n' if second_num < UPPER_LIMIT else
                   f'{first_num:>2} X {second_num:>2} = {first_num * second_num:>2}\n\n'
                    for i_main in (LOWER_LIMIT, LOWER_LIMIT + COLUMN)
                    for second_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE)
                    for first_num in range(i_main, i_main + COLUMN))
print(*table_generator)



