from Domain.Vanzare import creeaza_vanzare, get_id, get_titlu, get_gen, get_pret, get_tip_reducere


def test_domain():
    vanzare = creeaza_vanzare(5,'Print','Aventura',40,'silver')#trebuie stocat rezultatul undeva
    assert get_id(vanzare)== 5
    assert get_titlu(vanzare)=='Print'
    assert get_gen(vanzare)=='Aventura'
    assert get_pret(vanzare)==40
    assert get_tip_reducere(vanzare)=='silver'
