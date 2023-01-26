while 1:
    countvalie = int(input("Введи количество"))
    otvet=0
    command = input("Введите команду: \n+\n-\n*\n/\n**\nВвод: ")
    if(command == "+"):
        while countvalie > 0:
            value = int(input("Введи число"))
            otvet += value
            countvalie-=1
        print(otvet)
    elif(command == "-"):
        while countvalie > 0:
            value = int(input("Введи число"))
            otvet -= -value
            countvalie-=1
        print(otvet)
    elif(command == "*"):
        i = 0
        while countvalie > 0:
            value = int(input("Введи число"))
            if(i != 0):
                for number in range(value):
                    otvet += value
                    number+=1
                countvalie-=1
            else:
                otvet = value
            i+=1
        print(otvet)
    elif(command == "/"):
        while countvalie > 0:
            value = int(input("Введи число"))
            for number in range(value):
                otvet -= value
                number+=1
            countvalie-=1
        print(otvet)
    