import logging
logging.basicConfig(filename='prog.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

while True:
    try: #ввод чисел
        logging.info('User started program')
        
        k = int(input('Введите координату x в диапазоне от 1 до 8 первого поля: '))
        logging.info(f'Users input {k}')
        if k <= 0 or k > 8:
            print('Вы ввели некорректное значение. Повторите попытку')
            logging.error('Incorrect number')
            
            continue
        l = int(input('Введите координату y в диапазоне от 1 до 8 первого поля: '))
        logging.info(f'Users input {l}')
        if l <= 0 or l > 8:
            print('Вы ввели некорректное значение. Повторите попытку')
            
            continue
        m = int(input('Введите координату x в диапазоне от 1 до 8 второго поля: '))
        logging.info(f'Users input {m}')
        if m <= 0 or m > 8:
            print('Вы ввели некорректное значение. Повторите попытку')
            logging.error('Incorrect number')
            
            continue
        n = int(input('Введите координату y в диапазоне от 1 до 8 второго поля: '))
        logging.info(f'Users input {n}')
        if n <= 0 or n > 8: #если пользователь ввел неправильное значение
            print('Вы ввели некорректное значение. Повторите попытку')
            logging.error('Incorrect number')
            continue
        
        print('Выберите фигуру: 1 - Ферзь, 2 - Слон, 3 - Ладья, 4 - Конь')
        
        figure = int(input('Ваша фигура: ')) #выбор фигуры
        logging.info(f'User selects a figure')
        if figure < 0 or figure > 4: #если пользователь ввел неправильное значение
            print('Вы ввели некорректное значение. Повторите попытку')
            logging.error('Incorrect number')
            continue
    
    except ValueError: #если пользователь ввел неправильное значение
        print('Вы ввели некорректное значение. Повторите попытку')
        logging.info('Incorrect number')
        
    #четная сумма - белые, нечетная сумма - черные    
    s1 = (k + l) % 2
    s2 = (m + n) % 2
    if s1 == s2:
        print('Оба поля', end=' ')
        
        if s1 == 1:
            print('чёрного ', end='')
        else:
            print('белого ', end='')
        print('цвета')
        
    else:
        print('Поля разных цветов')
        logging.info('Program printed the color')
        
    distance_1 = abs(k-m)
    distance_2 = abs(l-n)

    if figure == 1: #ферзь
        if distance_1 == distance_2 or k == m or l == n:
            print(f'Ферзь угрожает полю ({m};{n})')
            logging.info('User made the right move')
        else:
            print('Ферзь не угрожает заданному полю')
            print(f'Для нападения передвиньте ферзя на поле ({m};{l})')
            logging.info('User made a wrong move')
          
    elif figure == 2: #слон
        if distance_1 == distance_2:
            print(f'Слон угрожает полю({m};{n})')
            logging.info('User made the right move')
        else:
            print('Слон не угрожает заданному полю')
            print(f'Для нападения передвиньте коня на поле ({l};{k})')
            logging.info('User made a wrong move')
            
    elif figure == 3: #ладья
        if k == m or l == n:
            print(f'Ладья угрожает полю ({m};{n})')
            logging.info('User made the right move')
        else:
            print('Ладья не угрожает заданному полю')
            print(f'Для нападения переставьте фигуру на поле ({k};{n})')
            logging.info('User made a wrong move')
            
    elif figure == 4: #конь
        if distance_1 == 2 and distance_2 == 1 or distance_1 == 1 and distance_2 == 2:
            print(f'Конь угрожает полю ({m};{n})')
            logging.info('User made the right move')
        else:
            print('Конь не угрожает заданному полю')
            logging.info('User made a wrong move')
    
    logging.info('Programm ended')
    break
