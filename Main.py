from Domain.Vanzare import creeaza_vanzare
from Teste.Run_all import run_all_tests
from UI.Console import run_menu


def main():

    vanzare1 = creeaza_vanzare(4,'Ahile','Razboi',40,'gold')
    vanzare2 = creeaza_vanzare(6,'Mate','Stiintific',60,'silver')
    vanzare3 = creeaza_vanzare(8,'Romana','Literatura',80,'none')
    vanzare4 = creeaza_vanzare(10,'Geografie','Stiinte',100,'silver')
    vanzare5 = creeaza_vanzare(12,'Bomba','Razboi',5,'silver')
    lista = [vanzare1,vanzare2,vanzare3,vanzare4,vanzare5]
    undo_list = []
    redo_list = []
    run_menu(lista,undo_list,redo_list)

run_all_tests()
main()