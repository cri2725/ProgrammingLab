# classe per le eccezioni
class ExamException(Exception):
    pass

#classe per media movente
class MovingAverage():
    #inizializzazione con lunghezza finestra
    def __init__(self, lfinestra):
        self.lfinestra=lfinestra
    def compute(self, l_input):
        media_mobile=[]
        for i,_ in enumerate(l_input):
            if (i+self.lfinestra)<=len(l_input):
                new_elemento=1
                for x in range(self.lfinestra):
                    new_elemento*=l_input[i+x]
                media_mobile.append(new_elemento)
            else:
                return media_mobile
                
if __name__ == "__main__":
    lunghezza=input("determinare la lunghezza della finestra: ")
    
    qval=input("determinare la quantità di valori da usare: ")
    try:
        lunghezza=int(lunghezza):
            
    qval=int(qval)
    lista_valori=[]
    if isinstance(qval, int):
        for i in range(qval):
            lista_valori.append(input(f"valore {i+1}: "))
    else:
        raise ExamException("errore")

    mediamovente=MovingAverage(lunghezza)
    
    print(mediamovente.compute(lista_valori))
    