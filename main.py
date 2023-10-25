class Lst:
    length=0
    lst=[]
    def __init__(self):
        print("List constr.")
        lst=[]
        length=0

    def inp_lst(self,lst):

        Lst.lst = input("enter ur List: ")

    def len_lst(self,lst):
        Lst.length=len(Lst.lst)
        print("len of ur List= ", Lst.length)

    def ret_lst(self,lst):
        print("ur returned List:",lst[::-1])


l=Lst()
l.inp_lst(l)
l.len_lst(l)
