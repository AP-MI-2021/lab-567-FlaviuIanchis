from Domain.Vanzare import creeaza_vanzare, get_id, get_titlu, get_gen, get_pret, get_tip_reducere


def get_by_id(vanzari,id):
    '''
    Gaseste o vanzare dupa id
    :param vanzari:
    :param id:
    :return:ne returneaza vanzarea cu id-ul cautat sau None daca nu o gaseste
    '''

    for vanzare in vanzari:
        if get_id(vanzare) == id:
            return vanzare

    return None

def adaugare_vanzare(id,titlu,gen,pret,tip_reducere,lista):
    '''
    Adauga o vanzare in lista
    :param id: id-ul vanzarii
    :param titlu: titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param tip_reducere: tipul reducerii
    :return: nu returneaza nimic
    '''
    vanzare = creeaza_vanzare(id,titlu,gen,pret,tip_reducere)
    lista.append(vanzare)


def stergere_vanzare(id,lista):
    '''
    Sterge o vanzare din lista dupa id
    :param id: id-ul vanzarii de sters
    :param lista: lista de vanzari
    :return:lista cu vanzari fara id-ul dat(ce trebuia sters)
    '''
    return [vanzare for vanzare in lista if get_id(vanzare)!=id]




def modificare_vanzare(lista,id_de_modificat,titlu,gen,pret,tip_reducere):
    '''
    Modifica o vanzare dupa id_de_modificat
    :param lista: lista de vanzari
    :param id_de_modificat: id-ul al carei vanzari vrem sa o modificam
    :param titlu: noul titlu
    :param gen: noul gen
    :param pret: noul pret
    :param tip_reducere: noul tip_reducere
    :return:
    '''

    lista_vanzari_modificate = []
    for vanzare in lista:
        if get_id(vanzare) == id_de_modificat:
            vanzare_noua = creeaza_vanzare(
                id_de_modificat,
                titlu if titlu!='' else get_titlu(vanzare),
                gen if gen!='' else get_gen(vanzare),
                pret if pret!=0 else get_pret(vanzare),
                tip_reducere if tip_reducere!= '' else get_tip_reducere(vanzare),
            )
            lista_vanzari_modificate.append(vanzare_noua)
        else:
            lista_vanzari_modificate.append(vanzare)
    return lista_vanzari_modificate
