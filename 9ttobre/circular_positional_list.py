from TdP_collections.list.positional_list import PositionalList


class CircularPositionalList(PositionalList):

    # già implementate in PositionalList: first, last, is_empty, insert_between (benché privato),len, replace
    #  (perché sostituisce un elemento in una posizione, quindi non si altera alcun collegamento)

    # -----------------------------------mutators-------------------------------------------------
    def add_first(self, e):
        """Inserisce l’elemento e in testa alla lista e restituisce la Position del nuovo elemento"""
        first = super().add_first(e)
        # aggiunto per garantire la circolarità, in questo modo il primo elemento della lista
        # ha per precedente l'ultimo elemento prima di trailer
        first._node._prev = self._trailer._prev
        self.last()._node._next = self._header._next
        return first

    def add_last(self, e):
        """Inserisce l’elemento e in coda alla lista e restituisce la Position del nuovo elemento"""
        last = super().add_last(e)
        # aggiunto per garantire la circolarità, in questo modo l'ultimo elemento della
        # lista ha per successivo il primo elemento dopo next
        last._node._next = self._header._next
        self.first()._node._prev = self._trailer._prev
        return last

    def add_before(self, p, e):
        """Inserisce un nuovo elemento e prima del nodo nella Position p e restituisce la Position del nuovo elemento"""
        # nel caso in cui p sia la prima position allora si sta inserendo in testa, quindi,
        # occorre aggiornare il campo next di trailer. Questo equivale ad effettuare un inserimento in testa.
        if p == self.first():
            return self.add_first(e)
        else:
            return super().add_before(p, e)

    def add_after(self, p, e):
        """Inserisce un nuovo elemento e dopo il nodo nella Position p e restituisce la Position del nuovo elemento"""
        # nel caso in cui p sia l'ultima position allora si sta inserendo in coda, quindi,
        #  occorre aggiornare il campo prev di header. Questo equivale ad effettuare un inserimento in coda
        if p == self.last():
            return self.add_last(e)
        else:
            return super().add_after(p, e)

    def delete(self, p):
        """Rimuove e restituisce l’elemento in Position p dalla lista e invalida p"""
        # Nel caso in cui si voglia cancellare l'ultimo elemento allora è necessario aggiornare poi il prev del trailer in modo tale che punti
        # al nuovo elemento e non al precedente. Il caso duale è quello in cui si cancelli il primo ed occorra aggiornare il next di header così
        # da farlo puntare al nuovo primo elemento.
        # Se invece si cancella una position intermedia allora si ricorre solamente al metodo della classe paterna.
        if p == self.last() and self.__len__() != 1:
            e = super().delete(p)
            primo = self.first()
            self._trailer._prev = primo._node._prev
            return e
        elif p == self.first() and self.__len__() != 1:
            e = super().delete(p)
            ultimo = self.last()
            self._header._next = ultimo._node._next
            return e
        else:
            return super().delete(p)

    # ------------------------------------accessors---------------------------------------------
    def before(self, p):
        """Restituisce l’elemento nella Position precedente a p, None se p non ha un predecessore e
         ValueError se p non è una position della lista"""
        # nel caso in cui ci sia un solo elemento nella lista si ritorna none.
        # Il confronto con la prima position della lista assicura di non ritornare None quando la dimensione è 1
        # e ma si passa alla funzione una position non valida
        if p == self.first() and self.__len__() == 1:
            return None
        else:
            return super().before(p)

    def after(self, p):
        """Restituisce l’elemento nella Position successiva a p, None se p non ha un successore e ValueError se
        p non è una position della lista"""
        if p == self.first() and self.__len__() == 1:
            return None
        else:
            return super().after(p)

    def find(self, e):
        """Restituisce una Position contenente la prima occorrenza dell’elemento e nella lista o None se e non è presente"""
        # scorre la lista fino a trovare la position il cui contenga l'elemento cercato altrimenti ritorna None
        current = self.first()
        i = 0

        while i < self.__len__():
            if e == current.element():
                return current
            else:
                current = self.after(current)
                i += 1
        return None

    def count(self, e):
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
        """Generatore che restituisce gli elementi della lista a partire da quello che è identificato
        come primo fino a quello che è identificato come ultimo"""
        # si è scelto di fare una condizione sul numero di elementi presenti e non sul
        current = self.first()
        i = 0
        while i < self.__len__():
            yield current.element()
            current = self.after(current)
            i += 1

    # modified
    def __delitem__(self, key):
        """Rimuove l’elemento nella position p invalidando la position"""
        # Definisce il comportamento al momento della distruzione di una position. Occorre lanciare eccezione nel caso di
        # input non valido
        self._validate(key)
        self.delete(key)

    def clear(self):
        """Rimuove tutti gli elementi della lista invalidando le corrispondenti Position"""
        # E' importante salvare la dimensione prima di iniziare a ciclare sulla dimensione in quanto questa viene diminuita per
        # ogni cancellazione: questo lascerebbe alcuni elementi nella lista
        i = 0
        current = self.last()
        dim = self.__len__()
        while i < dim:
            self.delete(current)
            current = self.last()
            i += 1

    def _swap(self, first_obj, last_obj):
        temp = first_obj.element()
        self.replace(first_obj, last_obj.element())
        self.replace(last_obj, temp)

    def reverse(self):
        """Inverte l’ordine degli elementi nella lista"""
        i = 0
        j = self.__len__() - 1
        first_obj = self.first()
        last_obj = self.last()
        while i < j :
            self._swap(first_obj, last_obj)
            first_obj = self.after(first_obj)
            last_obj = self.before(last_obj)
            i += 1
            j -= 1

    def is_sorted(self):
        current = self.first()
        for i in range(self.__len__() - 1):
            if self.after(current).element() < current.element():
                return False
            current = self.after(current)
        return True

    def __contains__(self, p):
        """ la validazione viene effettuata nella find"""
        """ restituisce True se la position e' presente nella lista"""
        node=self.find(p)
        if node!=None:
            return True
        else:
            return False

    def __getitem__(self, p):
        """restituisce l'elemento della position p se presente"""
        node=self._validate(p)
        node=self.find(p.element())
        return node.element()

    def __setitem__(self,p,v):
        node=self._validate(p)
        self.replace(p,v)


if __name__ == "__main__":
    l = CircularPositionalList()

    print("Lista vuota?", l.is_empty())
    p = l.add_last(50)
    print('\nTest before e after sul singolo')
    print(l.before(p))
    print(l.after(p))
    l.add_last(60)
    print(l.after(p).element())
    print("\nLista vuota?", l.is_empty())
    l.add_first(40)
    l.add_first(30)
    l.add_last(70)
    l.add_last(80)
    print("\nelementi della lista:")
    for e in l:
        print(e)
    print('\nTesting find.......')
    p = l.find(60)
    print("con successo", p.element())
    p = l.find(90)
    print("senza successo", p)
    print('\nTesting delete.......')
    print('\tdelete con add_first')
    p = l.add_first(20)
    l.delete(p)
    for e in l:
        print(e)
    print('\tdelete con add_last')
    p = l.add_last(100)
    l.delete(p)
    for e in l:
        print(e)
    print('\tdelete con add_after')
    p = l.add_after(l.first(), 78)
    l.delete(p)
    for e in l:
        print(e)
    print('\tdelete con add_before')
    p = l.add_before(l.first(), 78)
    l.delete(p)
    for e in l:
        print(e)
    print('\nTest count........')
    print(l.count(30))
    print(l.count(180))
    print("\nTest circolare")
    print("\tcon add_first")
    # l.add_first(60)
    # l.add_first(50)
    # l.add_first(40)
    # l.add_first(30)
    # l.add_first(20)
    # l.add_first(10)
    p = l.first()
    q = l.last()
    print("Before di first", l.before(p).element())
    print("After di last", l.after(q).element())
    print("\n\tcon add_last")
    # l.add_last(10)
    # l.add_last(20)
    # l.add_last(30)
    # l.add_last(40)
    # l.add_last(50)
    # l.add_last(60)
    p = l.first()
    q = l.last()
    print("Before del first", l.before(p).element())
    print("After del last", l.after(q).element())
    print("\nTesting reverse.......")
    l.reverse()
    for e in l:
        print(e)
    #l.add_last(22)
    print(l.is_sorted())
