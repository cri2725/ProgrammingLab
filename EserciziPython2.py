"""
import os
gwd=os.getcwd()
print("{}".format(gwd))

file = open("/home/cri2725/programmazione/LaboProg/CSVfiles/shampoo_sales.csv", "r")
print(file.readline())
file.close()
"""
"""
def contarighe(file):
    righe=0
    for riga in open(file):
        righe+=1
    return righe
file="LaboProg/CSVfiles/shampoo_sales.csv"
print("il file "+ file[30:] +" ha {} righe \n".format(contarighe(file)))
"""
"""
file=open("/home/cri2725/programmazione/LaboProg/CSVfiles/shampoo_sales.csv","r")
date=[]
sales=[]
for riga in file:
    rigapulita=riga.strip()
    elementi=rigapulita.split(",")
    if elementi[0]!="Date":
        date.append(elementi[0])
        sales.append(elementi[1])
print(f"le date sono: {date} \n")
print(f"gli elementi sono: {sales} \n")
"""
"""
def sumCSV(filepath):
    with open(filepath,"r") as fileCSV:
        valori=[]
        for riga in fileCSV:
            rigapulita=riga.strip()
            elementi=rigapulita.split(",")
            if elementi[0] != "Date": 
                valori.append(float(elementi[1]))
        return sum(valori)
file="/home/cri2725/programmazione/LaboProg/CSVfiles/shampoo_sales.csv"
print(f"la somma è {sumCSV(file)}")
"""