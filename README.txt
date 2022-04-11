Ciuculan Maria-Cristiana
333CC
                                README

    Pentru inceput, producer-ul va crea produsele intr-un loop infinit, de
fiecare data doar cantitatea ceruta pentru fiecare produs din lista. Se
incearca publicarea produsului si se asteapta pana cand produsul are
suficient spatiu pentru a fi adaugat. Dupa trecerea timpului de asteptare
pentru republicare se reincearca adaugarea lui si se repeta procesul pana
cand se poate publica. Trebuie crescut indexul produsului curent, iar daca
se ajunge la finalul listei, acesta se resteaza pe 0.
    In consumer se itereaza lista de cosuri si in fiecare dintre ele, lista
de operatii. Daca operatia din lista este adaugare se incearca adaugarea in
market, dar daca produsul nu este in stoc se asteapta timpul setat de
asteptare si se reincearca operatia. Pentru remove, se scoate fix cantitatea
de produs specificata. Daca nu exista operatia specificata, se transmite o
eroare. Se printeaza lista finala cu comenzile consumer-ului.
    In marketplace se implementeaza metodele cerute. Prima, register producer
va seta id-ul noului producer si va adauga in lista de produceri o noua lista
goala pentru produse. Publish adauga in market noul produs. Returneaza fals
daca numarul de produse a ajuns la limita impusa. Altfel, se adauga in lista
produsul si se returneaza adevarat. New cart adauga un nou cos de cumparaturi.
Creste id-ul curent, si adauga o lista goala in lista de cumparaturi. Se
returneaza id-ul curent. Add_to_cart itereaza prin lista de produse pana cand
este gasit produsul cautat de consumator. Daca este gasit, trebuie adaugat in
lista consumatorului si scos din lista producatorului ca pereche id-produs.
Returneaza adevarat cand este gasit si fals daca nu. Remove_from_cart cauta
produsul in cos si il elimina din cos, adaugandu-l in lista producatorului.
Place_order doar returneaza lista de la id-ul dat.

    Sursele principale de inspiratie au fost laboratoarele 1 si 2 cat si
diferite site-uri pentru a ma ajuta cu sintaxa in python.