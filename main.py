from Igorclass import Igor

a = None


while True:

    a = input("Введите значение: ")

    if a == "0":
        print("Конец программы")
        break
    elif a == "1":
        continue
    else:
        b = Igor()
        print(b.tall)
        b.voice()
        print(str(b.age()) + " AGE")


