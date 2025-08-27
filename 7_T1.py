kuukaudet = {"1":"talvi", "2":"talvi", "3":"kevät", "4":"kevät", "5":"kevät", "6":"kesä",
             "7":"kesä", "8":"kesä", "9":"syksy", "10":"syksy", "11":"syksy", "12":"talvi"}
while True:
    KuukausiInput = input("Anna kuukauden numero: ")
    try:
        if KuukausiInput in kuukaudet:
            print(kuukaudet[KuukausiInput])
        else:
            print("Nuh uh")
    except ValueError:
            print("Jotain meni väärin")