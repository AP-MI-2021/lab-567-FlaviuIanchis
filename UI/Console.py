from Domain.Vanzare import to_string
from Logic.Crud import adaugare_vanzare, stergere_vanzare, modificare_vanzare
from Logic.Operatiuni import aplicare_discount, modificare_gen, determinare_minim, titluri_distincte, ordonare_dupa_pret
from copy import deepcopy
#Folosim deepcopy pentru a salva in lista de undo valorile efective ale listei de vanzari la momentul adaugarii ,
#Altfel,va salva o referinta catre lista de vanzari,adica va citi valorile existente in lista de vanzari


def ui_print(lista):
    if len(lista) ==0:
      print('Lista goala')
    for i in range(len(lista)):
        print(to_string(lista[i]))

def ui_adaugare_vanzare(lista,undo_list,redo_list):#o sa aiba doua parti,una de citire a datelor si alta de adaugare in lista
    id = int(input('Dati id-ul vanzarii '))
    titlu = input('Dati titlul cartii ')
    gen = input('Dati genul cartii ')
    pret = int(input('Dati pretul cartii '))
    tip_reducere = input('Dati tipul reducerii ')

    redo_list.clear()
    undo_list.append(deepcopy(lista))
    adaugare_vanzare(id,titlu,gen,pret,tip_reducere,lista)



def ui_stergere_vanzare(lista,undo_list,redo_list):
    id = int(input('Dati id-ul vanzarii de sters '))

    redo_list.clear()
    undo_list.append(deepcopy(lista))
    return stergere_vanzare(id,lista)

def ui_modificare_vanzare(lista,undo_list,redo_list):
    id_de_modificat = int(input('Dati id-ul vanzarii de modificat '))
    titlu = input('Dati noul titlu ')
    gen = input('Dati noul gen ')
    pret = int(input('Dati noul pret '))
    tip_reducere = input('Dati noul tip de reducere ')

    redo_list.clear()
    undo_list.append(deepcopy(lista))
    return modificare_vanzare(lista,id_de_modificat,titlu,gen,pret,tip_reducere)



def ui_aplicare_discount(lista,undo_list,redo_list):

    redo_list.clear()
    undo_list.append(deepcopy(lista))
    return aplicare_discount(lista)

def ui_modificare_gen(lista,undo_list,redo_list):
    titlu_dat = input('Dati titlul ')
    noul_gen = input('Dati noul gen ')

    redo_list.clear()
    undo_list.append(deepcopy(lista))
    return modificare_gen(lista,titlu_dat,noul_gen)

def ui_determinare_minim(lista):
    minime=determinare_minim(lista)
    print(minime)

def ui_titluri_distincte(lista):
    distincte = titluri_distincte(lista)
    print(distincte)

def ui_ordonare_dupa_pret(lista):
    return ordonare_dupa_pret(lista)




def print_menu():
    print('1.Adaugare vanzare')
    print('2.Stergere vanzare')
    print('3.Modificare vanzare')
    print('4.Aplicare discount ')
    print('5.Modificare gen ')
    print('6.Determinare minim')
    print('7.Afisarea numarului de titluri distincte')
    print('8.Ordonarea vanzarilor crescator dupa pret ')
    print('a.Afiseaza toate vanzarile')
    print('u.Undo')
    print('r.Redo')
    print('x.Iesire')

def run_menu(lista,undo_list,redo_list):
    while True:
        print_menu()
        opt = input('Introduceti optiunea ')
        if opt == '1':
            ui_adaugare_vanzare(lista,undo_list,redo_list)
        elif opt == '2':
            lista = ui_stergere_vanzare(lista,undo_list,redo_list)
        elif opt == '3':
            lista = ui_modificare_vanzare(lista,undo_list,redo_list)
        elif opt == '4':
            lista = ui_aplicare_discount(lista,undo_list,redo_list)
        elif opt == '5':
            lista = ui_modificare_gen(lista,undo_list,redo_list)
        elif opt == '6':
            ui_determinare_minim(lista)
        elif opt == '7':
            ui_titluri_distincte(lista)
        elif opt == '8':
            lista = ui_ordonare_dupa_pret(lista)
        elif opt == 'a':
            ui_print(lista)
        elif opt == 'u':
            if len(undo_list)>0:
                redo_list.append(deepcopy(lista))
                lista = undo_list.pop()
            else:
                print('Nu se poate face undo ')
        elif opt == 'r':
            if len(redo_list)>0:
                undo_list.append(deepcopy(lista))
                lista = redo_list.pop()
            else:
                print('Nu se poate face redo ')
        elif opt == 'x':
            break
        else:
            'Optiune invalida'

