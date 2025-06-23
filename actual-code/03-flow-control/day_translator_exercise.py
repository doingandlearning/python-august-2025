# Instructions at https://gist.github.com/doingandlearning/3c3382126a904b3b2cc987d9bcd5370d

day = input("Enter a day of the week in English: ").title()

if day == "Monday":
    print("Lunes")
elif day == "Tuesday":
    print("Martes")
elif day == "Wednesday":
    print("Miércoles")
elif day == "Thursday":
    print("Jueves")
elif day == "Friday":
    print("Viernes")
elif day == "Saturday":
    print("Sábado")
elif day == "Sunday":
    print("Domingo")
else:
    print("Invàlido")


match day:
    case "Monday":
        print("Lunes")
    case "Tuesday":
        print("Martes")
    case "Wednesday":
        print("Miércoles")
    case "Thursday":
        print("Jueves")
    case "Friday":
        print("Viernes")
    case "Saturday":
        print("Sábado")
    case "Sunday":
        print("Domingo")
    case _:
        print("Inválido")