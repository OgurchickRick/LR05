def input_stack():
    towers = int(input('Введите кол-во башен: '))
    rings = int(input('Введите кол-во колец: '))
    start_tower = int(input('Введите номер начальной башни: '))
    finish_tower = int(input('Введите номер конечной башни: '))
    return hanoi(rings, start_tower, finish_tower, towers)


def hanoi(rings, start_tower, finish_tower, towers):
    sum = 0
    if rings <= 0:
        return
    for i in range(1, towers+1):
        sum += i
    help_tow = sum - start_tower - finish_tower
    hanoi(rings - 1, start_tower, help_tow, towers)
    print(start_tower, '=>', finish_tower)
    hanoi(rings - 1, help_tow, finish_tower, towers)


if __name__ == '__main__':
    input_stack()
