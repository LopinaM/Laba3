import yaml 

k = 1
while (k == 1):

    with open("C:/Users/V/Desktop/Маша/4 курс/ИИСИТ/1 лаба/Новая папка/in.yaml", encoding="utf-8") as file: 
        documents = yaml.full_load(file) 
        
        print("Объекты: ")
        y = documents['Objects']
        for count, item in enumerate(y):
                print(count + 1, item)
        print()
        
        num = int(input("Введите номер объекта: " ))
        numObj = y[num-1]
        print("Ваш бъект: " + numObj)
        print()

       
        print("Связи: ")
        data = ['часть состава', 'относится к', 'аудитория']
        for count, item in enumerate(data):
                print(count + 1, item)
        print()
    
        num2 = int(input("Введите номер связи: " ))
        numSvz = data[num2-1]
        print("Выбранная связь: " + numSvz)
        print()

        # поиск
        print("Результат: ")
        x = documents['Connection']
        for item in x:
            if item['type'] == numSvz and item['src'] == numObj:
                print(item)
        print()

        k1 = int(input("Введите 1, если хотите продолжить. Введите 0, если хотите завершить работу: "))
        k = k1
