from Domain.Vanzare import to_string
from Logic.Crud import ui_adaugare_vanzare, ui_stergere_vanzare, ui_modificare_vanzare, adaugare_vanzare, \
    stergere_vanzare, modificare_vanzare
from Teste.Run_all import run_all_tests


def ui_print(lista):
    if len(lista)==0:
        print('Lista goala')
    for i in range(len(lista)):
        print(to_string(lista[i]))
    print()





def print_menu():
    print('1.Introduti comanda ')
    print('x.Iesire')

def main():
    lista = []
    while True:
        print_menu()
        opt = input('Introduceti optiunea ')
        if opt == '1':
            comanda=input('Introduceti comanda ')
            comenzi = comanda.split(';')
            for optiune in comenzi :
                bucatele = optiune.split(',')

                if bucatele[0] == 'adauga':
                    adaugare_vanzare(int(bucatele[1]),bucatele[2],bucatele[3],int(bucatele[4]),bucatele[5],lista)
                elif bucatele[0] == 'sterge':
                     lista = stergere_vanzare(int(bucatele[1]),lista)
                elif bucatele[0] == 'modifica':
                     lista = modificare_vanzare(lista,int(bucatele[1]),bucatele[2],bucatele[3],int(bucatele[4]),bucatele[5])
                elif bucatele[0] == 'afisare':
                     ui_print(lista)

        elif opt == 'x':
            break
        else:
            'Optiune invalida'

main()