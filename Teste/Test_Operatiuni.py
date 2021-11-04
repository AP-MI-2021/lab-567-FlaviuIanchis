from Domain.Vanzare import creeaza_vanzare, get_titlu, get_gen, get_pret, get_tip_reducere, get_id
from Logic.Crud import get_by_id
from Logic.Operatiuni import modificare_gen, aplicare_discount, determinare_minim, titluri_distincte, ordonare_dupa_pret


def test_aplicare_discount():
    vanzare1 = creeaza_vanzare(5, 'Cal', 'Zoo', 45, 'silver')
    vanzare2 = creeaza_vanzare(6, 'Leu', 'Animal', 80, 'gold')
    lista = [vanzare1, vanzare2]
    lista = aplicare_discount(lista)
    vanzare_modificata = get_by_id(lista, 5)
    assert get_titlu(vanzare_modificata) == 'Cal'
    assert get_gen(vanzare_modificata) == 'Zoo'
    assert get_pret(vanzare_modificata) == 42.75
    assert get_tip_reducere(vanzare_modificata) == 'silver'
    vanzare_modificata2 = get_by_id(lista,6)
    assert get_titlu(vanzare_modificata2) == 'Leu'
    assert get_gen(vanzare_modificata2) == 'Animal'
    assert get_pret(vanzare_modificata2) == 72.00
    assert get_tip_reducere(vanzare_modificata2) == 'gold'



def test_modificare_gen():
    vanzare1 = creeaza_vanzare(5, 'Cal', 'Zoo', 45, 'silver')
    vanzare2 = creeaza_vanzare(6, 'Leu', 'Animal', 80, 'gold')
    lista = [vanzare1, vanzare2]
    lista = modificare_gen(lista,'Cal','Animal')
    vanzare_modificata = get_by_id(lista, 5)
    assert get_titlu(vanzare_modificata) == 'Cal'
    assert get_gen(vanzare_modificata) == 'Animal'
    assert get_pret(vanzare_modificata) == 45
    assert get_tip_reducere(vanzare_modificata) == 'silver'
    assert get_by_id(lista, 6) == vanzare2


def test_determinare_minim():
    vanzare1 = creeaza_vanzare(4, 'Ahile', 'Razboi', 40, 'gold')
    vanzare2 = creeaza_vanzare(6, 'Mate', 'Stiintific', 60, 'silver')
    vanzare3 = creeaza_vanzare(8, 'Romana', 'Literatura', 80, 'none')
    vanzare4 = creeaza_vanzare(10, 'Geografie', 'Stiinte', 100, 'silver')
    vanzare5 = creeaza_vanzare(12, 'Bomba', 'Razboi', 5, 'silver')
    lista = [vanzare1, vanzare2, vanzare3, vanzare4, vanzare5]
    minime=determinare_minim(lista)
    assert minime['Razboi']==5
    assert minime['Stiintific']==60
    assert minime['Literatura']==80
    assert minime['Stiinte']==100


def test_titluri_distincte():
    vanzare1 = creeaza_vanzare(4, 'Ahile', 'Razboi', 40, 'gold')
    vanzare2 = creeaza_vanzare(6, 'Mate', 'Stiintific', 60, 'silver')
    vanzare3 = creeaza_vanzare(8, 'Romana', 'Literatura', 80, 'none')
    vanzare4 = creeaza_vanzare(10, 'Geografie', 'Stiinte', 100, 'silver')
    vanzare5 = creeaza_vanzare(12, 'Bomba', 'Razboi', 5, 'silver')
    lista = [vanzare1, vanzare2, vanzare3, vanzare4, vanzare5]
    distincte=titluri_distincte(lista)
    assert distincte['Razboi']==2
    assert distincte['Stiintific']==1
    assert distincte['Literatura']==1
    assert distincte['Stiinte']==1

def test_ordonare_dupa_pret():
    vanzare1 = creeaza_vanzare(4, 'Ahile', 'Razboi', 40, 'gold')
    vanzare2 = creeaza_vanzare(6, 'Mate', 'Stiintific', 60, 'silver')
    vanzare3 = creeaza_vanzare(8, 'Romana', 'Literatura', 80, 'none')
    vanzare4 = creeaza_vanzare(10, 'Geografie', 'Stiinte', 100, 'silver')
    vanzare5 = creeaza_vanzare(12, 'Bomba', 'Razboi', 5, 'silver')
    lista = [vanzare1, vanzare2, vanzare3, vanzare4, vanzare5]
    lista = ordonare_dupa_pret(lista)
    assert get_id(lista[0])==12
    assert get_id(lista[1])==4
    assert get_id(lista[2])==6
    assert get_id(lista[3])==8
    assert get_id(lista[4])==10
