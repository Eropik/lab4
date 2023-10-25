ch=int(input("Меню для 4 лабораторной\n Выберите задачу(0 exit): "))
match ch:
    case 1:
        class Lst:
            length = 0
            lst = []

            def __init__(self):
                print("List constr.")
                lst = []
                length = 0

            def inp_lst(self, lst):
                Lst.lst = input("enter ur List: ")

            def len_lst(self, lst):
                Lst.length = len(Lst.lst)
                print("len of ur List= ", Lst.length)

            def ret_lst(self, lst):
                print("ur returned List:", lst[::-1])


        l = Lst()
        l.inp_lst(l)
        l.len_lst(l)
    case 2:

        class Country:
            name=""
            capital = ""
            square = 0.0
            people = 0

            def __init__(self):
                name="None"
                capital = "None"
                square = 0.0
                people = 0

        def square_search(self, c=Country()):
            cap=int("input country's square u search: ")
            if c.capital==cap:
                print("Searched by square country: ", c.name)


        def people_search (self, c=Country()):
            peop = int("input country's people u search: ")
            if c.people == peop:
                print("Searched by people country: ", c.name)











