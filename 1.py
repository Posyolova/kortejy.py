def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int): # проверяет является ли целым числом
            return (tpl) # если нет то в исходный 
    return tuple(sorted(tpl)) # отсортированный кортеж
print(tpl_sort((4, 8, 3, 1, 9)))
print(tpl_sort((4, 6, 2.1, 1, 7)))
