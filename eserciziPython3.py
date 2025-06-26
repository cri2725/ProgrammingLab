"""
import random
class Person():
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def __str__(self):
        return f"sono {self.name} {self.surname}"
    def saluto_salutone(self):
        n=random.randint(0,2)
        if n==0:
            return f"ciao hai beccato {n} e ciao"
        elif n==1:
            return f"ciao hai beccato {n} e ciaone"
        else:
            return f"ciao hai beccato {n} e ciaonene"
class Student(Person):
    def __str__(self):
        return f"ciao sono {self.name} {self.surname} e sono uno studente"

na="Paolo"
sur="Rossi"
persona=Person(na,sur)
print(f"il nome è {persona.name}")
print(f"il cognome è {persona.surname}")
print(persona)
print(persona.saluto_salutone())
nom="gino"
cogn="peppino"
studente=Student(nom,cogn)
print(studente)
print(studente.saluto_salutone())
"""
"""
Create un oggetto CSVFile che rappresenti un file CSV, e che:
    1. venga inizializzato sul nome del file csv, e
    2. abbia un attributo “name” che ne contenga il nome
    3. abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste,
    ad es: [ [’01-01-2012’, ’266.0'] , [’01-02-2012’, ’145.9’], ... ]
"""
"""
class CSVfile():
    def __init__(self,nomeFile):
        self.name=nomeFile
    def getdata(self):
        lista_dati=[]
        with open("/home/cri2725/programmazione/LaboProg/CSVfiles/"+self.name, "r") as file:
            for riga in file:
                rigapulita=riga.strip().split(",")
                if rigapulita[0] != "Date":
                    lista_dati.append(rigapulita)
        print(lista_dati)
file="shampoo_sales.csv"
filecsvshampoo=CSVfile(file)
filecsvshampoo.getdata()
"""
