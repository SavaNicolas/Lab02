from traduzione import Traduzione

class Dictionary:
    def __init__(self,nome,listaTraduzioni):
        self.nome = nome
        self.listaTraduzioni=listaTraduzioni

    def append(self,trad):
        self.listaTraduzioni.append(trad)

    def __str__(self):
        string = ""
        for i in self.listaTraduzioni:
            string += f" {i} \n"
        return string

    def cercaTraduzione(self,parolaAliena):
        listaTrad= self.listaTraduzioni

        for traduzione in listaTrad:
                if parolaAliena.lower().strip() == traduzione.alieno.strip().lower():
                    return str(traduzione.italiano)

        return "traduzione non trovata"


    def cercaTraduzioneWild(self,trad):
        #studio carattere uno alla volta, se il carattere è uguale a ? o è uguale al carattere nella stessa posizione allora lo stampo
            for i in self.listaTraduzioni:
                if len(i.alieno)== len(trad):
                    verifica= all(c1==c2 or c1=='?' for c1,c2  in zip(trad,i.alieno))
                    if verifica:
                        return str(i.italiano)

            return "traduzione non trovata"





