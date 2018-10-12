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
        elif p == self.last() and self.__len__() == 1:
            e = super().delete(p)
            self._header._next = self._trailer
            self._trailer._prev = self._header
            return e
        elif p == self.first() and self.__len__() == 1:
            e = super().delete(p)
            self._header._next = self._trailer
            self._trailer._prev = self._header
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
        self._header._next = self._trailer
        self._trailer._prev = self._header

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
        while i < j:
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
        node = self.find(p)
        if node != None:
            return True
        else:
            return False

    def __getitem__(self, p):
        """restituisce l'elemento della position p se presente"""
        node = self._validate(p)
        node = self.find(p.element())
        return node.element()

    def __setitem__(self, p, v):
        node = self._validate(p)
        self.replace(p, v)

    def __add__(self, other):
        for e in other:
            self.add_last(e)
        return self

    def copy(self):
        new_list = CircularPositionalList()
        for e in self:
            new_list.add_last(e)
        return new_list

    def __str__(self):
        string = ""
        for e in self:
            string = string + str(e) + ","
        return string[:len(string) - 1]

    def _bubble_sort(self, elementi):
        scambia = True
        count = len(elementi) - 1
        while count > 0 and scambia:
            scambia = False
            for i in range(count):
                if elementi[i] > elementi[i + 1]:
                    scambia = True
                    temp = elementi[i]
                    elementi[i] = elementi[i + 1]
                    elementi[i + 1] = temp
            count = count - 1

    def bubblesorted(self):
        l = []
        for e in self:
            l.append(e)
        self._bubble_sort(l)
        for el in l:
            yield el
        del l


class ScoreBoard:
    def __init__(self, x=10):
        pass

    def __len__(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

    def insert(self, s):
        pass

    def merge(self, new):
        pass

    def top(self, i=1):
        pass

    def last(self, i=1):
        pass

def merge(l1, l2, l_fusion):
    if l1.is_sorted() and l2.is_sorted():
        l1_pos = l1.first()
        l2_pos = l2.first()
        i = 0
        j = 0
        while i < l1.__len__() and j < l2.__len__():
            if l1_pos.element() < l2_pos.element():
                l_fusion.add_last(l1_pos.element())
                l1_pos = l1.after(l1_pos)
                i += 1
            elif l1_pos.element() > l2_pos.element():
                l_fusion.add_last(l2_pos.element())
                l2_pos = l2.after(l2_pos)
                j += 1
            else:
                l_fusion.add_last(l1_pos.element())
                l1_pos = l1.after(l1_pos)
                i += 1
                l_fusion.add_last(l2_pos.element())
                l2_pos = l2.after(l2_pos)
                j += 1
        while i < l1.__len__():
            l_fusion.add_last(l1_pos.element())
            l1_pos = l1.after(l1_pos)
            i += 1
        while j < l2.__len__():
            l_fusion.add_last(l2_pos.element())
            l2_pos = l2.after(l2_pos)
            j += 1
    else:
        raise ValueError('One of the list is not sorted')
