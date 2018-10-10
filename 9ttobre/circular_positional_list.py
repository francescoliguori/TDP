from TdP_collections.list.positional_list import PositionalList


class CircularPositionalList(PositionalList):

    #già implementate in PositionalList: first, last, is_empty, insert_between (benché privato),len, iter, replace (perché sostituisce un
    #elemento in una posizione, quindi non si altera alcun collegamento)

    #-----------------------------------mutators-------------------------------------------------
    def add_first(self, e):
        """Inserisce l’elemento e in testa alla lista e restituisce la Position del nuovo elemento"""
        first = super().add_first(e)
        # aggiunto per garantire la circolarità, in questo modo il primo elemento della lista ha per precedente l'ultimo elemento prima
        # di trailer
        first._node._prev = self._trailer._prev
        self.last()._node._next = self._header._next
        return first

    def add_last(self, e):
        """Inserisce l’elemento e in coda alla lista e restituisce la Position del nuovo elemento"""
        last = super().add_last(e)
        # aggiunto per garantire la circolarità, in questo modo l'ultimo elemento della lista ha per successivo il primo elemento dopo next
        last._node._next = self._header._next
        self.first()._node._prev = self._trailer._prev
        return last

    def add_before(self, p, e):
        """Inserisce un nuovo elemento e prima del nodo nella Position p e restituisce la Position del nuovo elemento"""
        #nel caso in cui p sia la prima position allora si sta inserendo in testa, quindi, occorre aggiornare il campo next di trailer.
        #Questo equivale ad effettuare un inserimento in testa.
        if p == self.first():
            return self.add_first(e)
        else:
            return super().add_before(p,e)

    def add_after(self, p, e):
        """Inserisce un nuovo elemento e dopo il nodo nella Position p e restituisce la Position del nuovo elemento"""
        #nel caso in cui p sia l'ultima position allora si sta inserendo in coda, quindi, occorre aggiornare il campo prev di header.
        #Questo equivale ad effettuare un inserimento in coda
        if p == self.last():
            return self.add_last(e)
        else:
            return super().add_after(p,e)

    def delete(self, p):
        """Rimuove e restituisce l’elemento in Position p dalla lista e invalida p"""
       #Nel caso in cui si voglia cancellare l'ultimo elemento allora è necessario aggiornare poi il prev del trailer in modo tale che punti
       #al nuovo elemento e non al precedente. Il caso duale è quello in cui si cancelli il primo ed occorra aggiornare il next di header così
       #da farlo puntare al nuovo primo elemento.
       # Se invece si cancella una position intermedia allora si ricorre solamente al metodo della classe paterna.
        if p == self.last():
            e = super().delete(p)
            primo = self.first()
            self._trailer._prev = primo._node._prev
            return e
        elif p == self.first():
            e = super().delete(p)
            ultimo = self.last()
            self._header._next = ultimo._node._next
            return e
        else:
            return super().delete(p)


    #------------------------------------accessors---------------------------------------------
    def before(self, p):
        """Restituisce l’elemento nella Position precedente a p, None se p non ha un predecessore e
         ValueError se p non è una position della lista"""
        #nel caso in cui ci sia un solo elemento nella lista si ritorna none. Il confronto con la prima position della lista
        #assicura di non ritornare None quando la dimensione è 1 e ma si passa alla funzione una position non valida
        if  p == self.first() and self.__len__() == 1:
            return None
        else:
            return super().before(p)

    def after(self,p):
        """Restituisce l’elemento nella Position successiva a p, None se p non ha un successore e ValueError se
        p non è una position della lista"""
        if p == self.first() and self.__len__() == 1:
            return None
        else:
            return super().after(p)

    def find(self,e):
        """Restituisce una Position contenente la prima occorrenza dell’elemento e nella lista o None se e non è presente"""
        #scorre la lista fino a trovare la position il cui contenga l'elemento cercato altrimenti ritorna None
        current = self.first()
        i = 0

        while i < self.__len__():
            if e == current.element():
                return current
            else:
                current = self.after(current)
                i += 1
        return None

    def count(self,e):
        """Resituisce il numero di occorrenze di e nella Lista"""
        current = self.first()
        i = 0
        count = 0
        while i < self.__len__():
            if e == current.element():
                count += 1
                current = self.after(current)
                i += 1
            else:
                current = self.after(current)
                i += 1

        return count



    def __iter__(self):
        """Generatore che restituisce gli elementi della lista a partire da quello che è identificato come primo fino a quello che è identificato come ultimo"""
        #si è scelto di fare una condizione sul numero di elementi presenti e non sul
        current = self.first()
        i = 0
        while i < self.__len__():
            yield current.element()
            current = self.after(current)
            i += 1

    def reverse(self):
        """Inverte l’ordine degli elementi nella lista"""
        #nel caso in cui la lista sia ordianta secondo un qualche criterio allora restituisce gli elementi della lista in ordine
        #inverso rispetto ad esso. Viceversa, se non dovesse essere ordinata, allora restituisce gli elementi in ordine inverso
        #rispetto all'inserimento
        current = self.last()
        i = 0
        while i < self.__len__():
            yield current.element()
            current = self.before(current)
            i += 1


if __name__ == "__main__":
    l = CircularPositionalList()
    print(l.is_empty())
    p =l.add_last(60)
    print('Test before e after.....')
    print(l.before(p))
    l.add_last(50)
    print(l.after(p).element())
    # l.add_first(10)
    # for e in l:
    #     print(e)
    print(l.is_empty())
    l.add_first(20)
    print(l.is_empty())
    l.add_first(30)
    l.add_last(40)
    l.add_last(70)
    for e in l:
        print(e)
    #test find
    print('Test find.......')
    p = l.find(60)
    print(p.element())
    p = l.find(90)
    print(p)
    print('Test delete.......')
    #test delete
    print('Test delete 1')
    p = l.add_first(80)
    l.delete(p)
    #print(l.delete(p))
    for e in l:
        print(e)
    print('Test delete 2')
    p = l.add_last(100)
    l.delete(p)
    # print(l.delete(p))
    for e in l:
        print(e)
    print('Test delete 3')
    p = l.add_after(l.first(), 78)
    l.delete(p)
    for e in l:
        print(e)
    print('Test delete 4')
    p = l.add_before(l.first(), 78)
    l.delete(p)
    for e in l:
        print(e)
    print('Test count........')
    print(l.count(30))
    print(l.count(180))




    