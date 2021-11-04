from Teste.Test_Domain import test_domain
from Teste.Test_Operatiuni import test_modificare_gen, test_aplicare_discount, test_determinare_minim, \
    test_titluri_distincte, test_ordonare_dupa_pret
from Teste.Test_crud import test_adaugare_vanzare, test_stergere_vanzare, test_modificare_vanzare


def run_all_tests():
    test_domain()
    test_adaugare_vanzare()
    test_stergere_vanzare()
    test_modificare_vanzare()
    test_modificare_gen()
    test_aplicare_discount()
    test_determinare_minim()
    test_titluri_distincte()
    test_ordonare_dupa_pret()