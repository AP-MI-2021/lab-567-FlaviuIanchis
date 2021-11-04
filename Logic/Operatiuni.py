from Domain.Vanzare import get_tip_reducere, creeaza_vanzare, get_id, get_titlu, get_gen, get_pret




def aplicare_discount(lista):
    '''
    Aplica un discount de 5% pentru toate reducerile de tip silver si 10% pentru cele de tip gold
    :param lista: lista de vanzari
    :return: se returneaza lista cu vanzari cu  pretul redus in urma discountului facut
    '''

    lista_vanzari_modificate = []
    for vanzare in lista:
        if  'silver' == get_tip_reducere(vanzare):
            vanzare_noua_1 = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                get_pret(vanzare)-0.05*get_pret(vanzare),
                get_tip_reducere(vanzare)
            )
            lista_vanzari_modificate.append(vanzare_noua_1)
        elif 'gold' == get_tip_reducere(vanzare):
            vanzare_noua_2 = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                get_pret(vanzare) - 0.1 * get_pret(vanzare),
                get_tip_reducere(vanzare)
            )
            lista_vanzari_modificate.append(vanzare_noua_2)
        else:
            lista_vanzari_modificate.append(vanzare)
    return lista_vanzari_modificate


def modificare_gen(lista,titlu_dat,noul_gen):
    '''
    Functia modifica genul unei carti pe baza titlului cautat
    :param lista: lista de vanzare
    :param titlu_dat: titlul dat de la tastatura
    :param noul_gen: genul dat de utilizator
    :return: o lista de vanzari cu genul modificat pentru cartile care au titlul dat
    '''
    lista_vanzari_modificate = []
    for vanzare in lista:
        if titlu_dat == get_titlu(vanzare):
            vanzare_noua = creeaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                noul_gen,
                get_pret(vanzare),
                get_tip_reducere(vanzare)
            )
            lista_vanzari_modificate.append(vanzare_noua)
        else:
            lista_vanzari_modificate.append(vanzare)
    return lista_vanzari_modificate

def determinare_minim(lista):
    '''
    Functia determina pretul minim pentru fiecare gen
    :param lista: lista de vanzari
    :return: un dictionar unde cheia este genul si valoarea este pretul minim pentru genul respectiv
    '''

    #
    minim = {}#dictionar care retine ca si chei genurile distincte ale vanzarilor si pentru fiecare cheie valoarea va fi pretul minim al vanzarii cu genul respectiv
    for vanzare in lista:
        if get_gen(vanzare) in minim.keys():#daca exista deja cheia in dictionar(am mai intalnit genul asta in vanzarile de pana acum) atunci valoarea din dictionar reprezinta pretul minim de pana acum
            if get_pret(vanzare)<minim[get_gen(vanzare)]:#daca pretul vanzarii curente este mai mic decat pretul minim calculat pana acum atunci am gasit un nou minim si updatam valoarea de la cheia respectiva
                minim[get_gen(vanzare)] = get_pret(vanzare)
        else:#daca nu avem genul vanzarii curente in dictionar adaugam genul asta ca si cheie si valoarea va fi pretul vanzarii curente
            minim[get_gen(vanzare)]= get_pret(vanzare)
    return minim

def titluri_distincte(lista):
    '''
    Functia afiseaza numarul de titluri distincte pentru fiecare gen
    :return:
    '''

    distincte = {}#prima data pentru fiecare gen vom calcula multimea de titluri distincte,apoi vom retine in dictionarul distincte pentru fiecare cheie numarul de elemente din multime
    #folosim set-ul din Python si el stie sa nu adauge inca o data un element care deja exista in multime
    for vanzare in lista:
        if get_gen(vanzare) in distincte.keys():#daca genul vanzarii exista in dictionar atuncti adaug la multimea de titluri titlul vanzarii curente
            distincte[get_gen(vanzare)].add(get_titlu(vanzare))
        else:#daca nu exista genul atunci il adaug iar valoarea va fi multimea care contine deja titlul vanzarii curente
            distincte[get_gen(vanzare)] = set()#cream o multime goala
            distincte[get_gen(vanzare)].add(get_titlu(vanzare))
    print(distincte)
    for cheie in distincte.keys():#inlocuim multimea titlurilor distincte cu numarul elementelor din multime
        distincte[cheie]= len(distincte[cheie])

    return distincte

def ordonare_dupa_pret(lista):
    '''
    Functia ordoneaza vanzarile crescator dupa pret
    :param lista: lista de vanazari
    :return: o lista de vanzari ordonata dupa pret
    '''

    return sorted(lista,key=lambda vanzare:get_pret(vanzare))