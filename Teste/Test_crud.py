from Domain.Vanzare import get_id, get_titlu, get_gen, get_pret, get_tip_reducere, creeaza_vanzare
from Logic.Crud import adaugare_vanzare, stergere_vanzare, modificare_vanzare, get_by_id
from Logic.Operatiuni import modificare_gen


def test_adaugare_vanzare():
    lista = []
    adaugare_vanzare(3,'Luna','Stiintific',40,'none',lista)
    assert get_id(lista[0]) == 3
    assert get_titlu(lista[0]) == 'Luna'
    assert get_gen(lista[0]) == 'Stiintific'
    assert get_pret(lista[0]) == 40
    assert get_tip_reducere(lista[0]) == 'none'

def test_stergere_vanzare():
    vanzare1=creeaza_vanzare(5,'Cal','Zoo',45,'silver')
    vanzare2=creeaza_vanzare(6,'Leu','Animal',80,'gold')
    lista = [vanzare1,vanzare2]

    lista = stergere_vanzare(5,lista)
    assert len(lista)==1

def test_modificare_vanzare():
    vanzare1 = creeaza_vanzare(5, 'Cal', 'Zoo', 45, 'silver')
    vanzare2 = creeaza_vanzare(6, 'Leu', 'Animal', 80, 'gold')
    lista = [vanzare1, vanzare2]
    lista = modificare_vanzare(lista,5,'','Boss',90,'gold')
    vanzare_modificata = get_by_id(lista,5)
    assert get_titlu(vanzare_modificata)=='Cal'
    assert get_gen(vanzare_modificata)=='Boss'
    assert get_pret(vanzare_modificata)==90
    assert get_tip_reducere(vanzare_modificata)=='gold'
    assert get_by_id(lista,6)==vanzare2

    lista = [vanzare1,vanzare2]
    lista = modificare_vanzare(lista,10,'Cerb','Comedie',60,'none')
    assert get_by_id(lista,5)==vanzare1
    assert get_by_id(lista,6)==vanzare2


