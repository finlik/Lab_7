while True:
    try:
        k = int(input('Введите координату x в диапазоне от 1 до 8 первого поля: '))

        if k <= 0 or k > 8:
            print('Вы ввели некорректное значение. Повторите попытку')
            
            continue
        l = int(input('Введите координату y в диапазоне от 1 до 8 первого поля: '))
       
        if l <= 0 or l > 8:
            print('Вы ввели некорректное значение. Повторите попытку')
            
            continue
        m = int(input('Введите координату x в диапазоне от 1 до 8 второго поля: '))
       
        if m <= 0 or m > 8:
            print('Вы ввели некорректное значение. Повторите попытку')
            
            continue
        n = int(input('Введите координату y в диапазоне от 1 до 8 второго поля: '))
        
        if n <= 0 or n > 8:
            print('Вы ввели некорректное значение. Повторите попытку')
            
            continue
        print('Выберите фигуру: 1 - Ферзь, 2 - Слон, 3 - Ладья, 4 - Конь')
        figure = int(input('Ваша фигура: '))
        
        if figure < 0 or figure > 4:
            print('Вы ввели некорректное значение. Повторите попытку')
            
            continue
    except ValueError:
        print('Вы ввели некорректное значение. Повторите попытку')
        
    s1 = (k + l) % 2
    s2 = (m + n) % 2
    if s1 == s2:
        print('Оба поля', end=' ')
        
        if s1 == 1:
            print('чёрного ', end='')
        else:
            print('белого ', end="")
        print('цвета')
        
    else:
        print('Поля разных цветов')
        

    distance_1 = abs(k-m)
    distance_2 = abs(l-n)

    if figure == 1:
        if distance_1 == distance_2 or k == m or l == n:
            print(f'Ферзь угрожает полю ({m};{n})')    
        else:
            print('Ферзь не угрожает заданному полю')
            print(f'Для нападения передвиньте ферзя на поле ({m};{l})')
          
    elif figure == 2:
        if distance_1 == distance_2:
            print(f'Слон угрожает полю({m};{n})')    
        else:
            print('Слон не угрожает заданному полю')
            print(f'Для нападения передвиньте коня на поле ({l};{k})')
            
    elif figure == 3:
        if k == m or l == n:
            print(f'Ладья угрожает полю ({m};{n})')    
        else:
            print('Ладья не угрожает заданному полю')
            print(f'Для нападения переставьте фигуру на поле ({k};{n})')
            
    elif figure == 4:
        if distance_1 == 2 and distance_2 == 1 or distance_1 == 1 and distance_2 == 2:
            print(f'Конь угрожает полю ({m};{n})')    
        else:
            print('Конь не угрожает заданному полю')    
    break
