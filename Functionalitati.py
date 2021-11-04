'''
Lista functionalitati:
F1.Adaugare vanzare
F2.Stergere vanzare
F3.Modificare vanzare
F4.Aplicare discount
F5.Modificare gen
F6.Determinare minim
F7.Afisarea numarului de titluri distincte
F8.Ordonarea vanzarilor crescator dupa pret
F9.Afiseaza toate vanzarile
F10.Undo
F11.Redo
-----------------

Scenariu de rulare pentru F1

    #Utilizator            Program                     Precizari
1.                     afiseaza meniul initial
2.      1                                              Utilizatorul alege optiunea 1
3.                      Da-ti id-ul                    Programul cere id-ul
4.      3                                              Utilizatorul da id-ul
5.                     Dati titlul cartii              Programul cere titlul cartii
6.     Praslea                                         Utilizatorul da titlu :Praslea
7.                     Dati genul cartii               Programul cere genul cartii
8.     Aventura                                        Utilizatorul da genul :aventura
9.                    Dati pretul cartii               Programul cere pretul cartii
10.      20                                            Utilizatorul da pretul 20 de lei
11.                   Dati tipul reducerii             Programul cere tipul reducerii
12     gold                                            Utilizatorul da tipul :gold
13                    Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F1:
1.Reprezentarea unei vanzari printr-un dictionar
2.Definirea getterilor
3.Citirea datelor de la tastatura
4.Adaugarea vanzarii in lista



Scenariu de rulare pentru F2

    #Utilizator            Program                     Precizari
1.                     afiseaza meniul initial
2.      2                                              Utilizatorul alege optiunea 2
3.                      Da-ti id-ul de sters           Programul cere id-ul de sters
4.      4                                              Utilizatorul da id-ul
5                    Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F2:
1.Reprezentarea unei vanzari printr-un dictionar
2.Definirea getterilor
3.Citirea datelor de la tastatura
4.Stergerea unei vanzari din lista pe baza unui id de sters

-------------------------
Scenariu de rulare pentru F3

    #Utilizator            Program                     Precizari
1.                     afiseaza meniul initial
2.      3                                              Utilizatorul alege optiunea 3
3.                      Da-ti id-ul de modificat       Programul cere id-ul care se doreste a fi modificat
4.      4                                              Utilizatorul da id-ul
5.                     Dati noul titlu al cartii       Programul cere noul titlu al cartii
6.     Praslea                                         Utilizatorul da titlu :Informatica
7.                     Dati noul gen al cartii         Programul cere noul gen al  cartii
8.     Stiintific                                      Utilizatorul da genul :Stiintific
9.                    Dati noul pret al cartii         Programul cere noul pret al cartii
10.      30                                            Utilizatorul da pretul 30 de lei
11.                   Dati noul tip de  reducere       Programul cere noul tip de reducere
12     silver                                          Utilizatorul da tipul :silver
13                    Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F3:
1.Reprezentarea unei vanzari printr-un dictionar
2.Definirea getterilor
3.Citirea datelor de la tastatura
4.Modificarea unei vanzari din lista pe baza unui id_de_modificat

-------------------------

Scenariu de rulare pentru F4

    #Utilizator            Program                     Precizari
1.                     afiseaza meniul initial
2.      4                                              Utilizatorul alege optiunea 4
3                    Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F4:
1.Crearea unei functii pentru aplicare a discount-ului

-------------------------

Scenariu de rulare pentru F5

    #Utilizator            Program                     Precizari
1.                     afiseaza meniul initial
2.      5                                              Utilizatorul alege optiunea 5
3.                      Da-ti titlul                   Programul cere titlul cartii  care se doreste a fi modificata
4.      Mate                                           Utilizatorul da titlul
5.                     Dati noul gen al cartii         Programul cere noul gen al cartii
6.     Aventura                                        Utilizatorul da genul Aventura
7                    Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F5:
1.Crearea unei functii pentru modificarea genului

-------------------------
Scenariu de rulare pentru F6

    #Utilizator            Program                            Precizari
1.                     afiseaza meniul initial
2.      6                                                     Utilizatorul alege optiunea 6
3.                    Se afiseaza intr-un dictionar
                      avand ca si cheie genul cartii
                      iar ca si valoarea pretul minim gasit
4                     Afiseaza din nou meniul initial


--------------------------------
Lista de activitati pentru F6:
1.Crearea unei functii pentru a determina pretul minim pentru fiecare gen

-------------------------
Scenariu de rulare pentru F7

    #Utilizator            Program                            Precizari
1.                     afiseaza meniul initial
2.      7                                                     Utilizatorul alege optiunea 7
3.                    Se afiseaza intr-un dictionar
                      avand ca si cheie genul cartii
                      iar ca si valoare numarul de
                      titluri distincte pt fiecare gen
4                     Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F7:
1.Crearea unei functii care afiseaza numarul de titluri distincte pentru fiecare gen

-------------------------
Scenariu de rulare pentru F8

    #Utilizator            Program                     Precizari
1.                     afiseaza meniul initial
2.      8                                              Utilizatorul alege optiunea 8
3                     Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F8:
1.Crearea unei functii care ordoneaza vanzarile crescator dupa pret
-------------------------
Scenariu de rulare pentru F9

    #Utilizator            Program                     Precizari
1.                     afiseaza meniul initial
2.      a                                              Utilizatorul alege optiunea a
3                  Programul afiseaza toate vanzarile
4                    Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F9:
1.Crearea unei functii de afisare a tuturor vanzarilor

-------------------------

Scenariu de rulare pentru F10

    #Utilizator            Program                     Precizari
1.                     afiseaza meniul initial
2.      u                                              Utilizatorul alege optiunea u
3                     Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F1:
1.Initializarea unei liste goale de tipul undo_list in main
2.Setarea acestei liste ca si parametru la functiile de afisare pentru operatiile din CRUD

-------------------------

Scenariu de rulare pentru F11

    #Utilizator            Program                     Precizari
1.                     afiseaza meniul initial
2.      r                                              Utilizatorul alege optiunea r
3                     Afiseaza din nou meniul initial

--------------------------------
Lista de activitati pentru F11:
1.Initializarea unei liste goale redo_list in main
2.Setarea acestei liste ca si parametru la functiile de afisare pentru operatiile din CRUD

-------------------------

Planificarea iteratiilor:
-Laborator 5:F1,F2,F3,
-Laborator 6:F4,F5,F6,F7
-Laborator 7:F8,F9,F10

'''