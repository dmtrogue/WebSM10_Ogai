# используется для сортировки
from operator import itemgetter


class House:
    """Дом"""
    def __init__(self, id, nmb, area, strt_id):
        self.id = id
        self.nmb = nmb
        self.area = area
        self.strt_id = strt_id


class Strt:
    """Улица"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


# Улица
strt = [
    Strt(1, 'ул. Усилова'),
    Strt(2, 'ул. Пушкина'),
    Strt(3, 'ул. Рокки Вуловича'),
    Strt(4, 'ул. Королёва'),
    Strt(5, 'ул. Гагарина'),
    Strt(6, 'ул. Ленина'),
]


# Дом
house = [
    House(1, '5', 1000, 1),
    House(2, '6', 2300, 2),
    House(3, '37', 5000, 4),
    House(4, '17/4', 1100, 3),
    House(5, '32/1', 2500, 6),
]


def main():
    """Основная функция"""
    # Соединение данных один-ко-многим 
    one_to_many = [(e.nmb, e.area, d.name) 
        for d in strt 
        for e in house 
        if e.strt_id==d.id]
    
    print('Задание 1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('Задание 2')
    res_12_unsorted = []
    # Перебираем все улицы
    for d in strt:
        # Список домов улицы
        d_house = list(filter(lambda i: i[2]==d.name, one_to_many))
        # Если улица имеет дома        
        if len(d_house) > 0:
            # Площади домов улицы
            d_area = [area for _,area,_ in d_house]
            # Суммарная площадь домов улицы
            d_area_sum = sum(d_area)
            res_12_unsorted.append((d.name, d_area_sum))


    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


if __name__ == '__main__':
    main()
