def creeaza_vanzare(id,titlu,gen,pret,tip_reducere):
    '''
    Functia creeaza un dictionar(obiect) pentru a putea reprezenta o vanzare
    :param id: id-ul vanzarii
    :param titlu:titlul cartii
    :param gen: genul cartii
    :param pret: pretul cartii
    :param tip_reducere: tipul reducerii
    :return: un obiect de tipul vanzare
    '''
    # return {
    #     'id':id,
    #     'titlu':titlu,
    #     'gen':gen,
    #     'pret':pret,
    #     'tip_reducere':tip_reducere
    # }
    return [id,titlu,gen,pret,tip_reducere]

def get_id(vanzare):
    '''
    Functia da id-ul vanzarii
    :param vanzare
    :return:id-ul vanzarii
    '''
    #return vanzare['id']
    return vanzare[0]

def get_titlu(vanzare):
    '''
    Functia da titlul cartii
    :param vanzare
    :return: titlul cartii
    '''
    #return vanzare['titlu']
    return vanzare[1]

def get_gen(vanzare):
    '''
    Functia da genul cartii
    :param vanzare
    :return: genul cartii
    '''
    #return vanzare['gen']
    return vanzare[2]

def get_pret(vanzare):
    '''
    Functia da pretul cartii
    :param vanzare
    :return: pretul cartii
    '''
    #return vanzare['pret']
    return vanzare[3]


def get_tip_reducere(vanzare):
    '''
    Functia da tipul reducerii
    :param vanzare
    :return: tipul reducerii
    '''
    #return vanzare['tip_reducere']
    return vanzare[4]

def to_string(vanzare):#functia afiseza parametrii
    return 'id:{},titlu:{},gen:{},pret:{},tip_reducere:{}'.format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_tip_reducere(vanzare)

    )