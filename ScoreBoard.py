from circular_positional_list import *


class ScoreBoard:
    class Score:
        # la classe score è una classe innestata. Una istanza della classe score sarà poi contenuta come nodo all'interno di una position
        # della circularpositional
        __slots__ = '_nome', '_score', '_date'

        def __init__(self, nome, score, date):
            self._nome = nome
            self._score = score
            self._date = date

        def score(self):
            # ritorna il punteggio associato a un oggetto della classe Score
            return self._score

        def nome(self):
            return self._nome

        def date(self):
            return self._date

        def __lt__(self, other):
            return self._score < other._score

        def __le__(self, other):
            return not self > other

        def __gt__(self, other):
            return self._score > other._score

        def __ge__(self, other):
            return not self < other

        def __eq__(self, other):
            return self._score == other._score

        def __ne__(self, other):
            return not self._score == other._score

        def __str__(self):
            return str(self._score) + " - " + self._nome + " - " + self._date

    # ---------------------------------------metodi di ScoreBoard----------------
    def __init__(self, x=10):
        if not isinstance(x, int):
            raise TypeError('x must be proper int type')
        if x <= 0:
            raise ValueError('x must be greater than zero')
        self._l = CircularPositionalList()
        self._dimension = x

    def __len__(self):
        """Restituisce la dimensione dello Scoreboard"""
        # In questo caso la dimensione dello ScoreBoard >= numero di elementi diversi da None
        return self._dimension

    def size(self):
        """Restituisce il numero di Score presenti nello Scoreboard"""
        return self._l.__len__()

    def is_empty(self):
        """Restituisce True se non ci sono Score nello Scoreboard e False altrimenti"""
        return self.size() == 0

    def _score_validate(self, score):
        if not isinstance(score, self.Score):
            raise TypeError('score must be proper Score type')
        if not isinstance(score.nome(), str):
            raise TypeError('score._name must be proper str type')
        if not isinstance(score.score(), int):
            raise TypeError('score._score must be proper int type')
        if not isinstance(score.date(), str):
            raise TypeError('score._date must be proper str type')

    def top(self, i=1):
        """Restituisce i migliori i Score nello Scoreboard"""
        if 0 < i <= self.size():
            l = []
            score = self._l.first()
            for j in range(0, i):
                l.append(score.element())
                score = PositionalList.after(self._l, score)
            return l
        else:
            raise ValueError("Error Scoreboard index")


    def last(self, i=1):  #new last
        """Restituisce i peggiori i Score nello Scoreboard"""
        if 0 < i <= self.size():
            l = []
            score=self._l.last()
            for j in range(0 , i):
                l.append(score.element())
                score=PositionalList.before(self._l,score)
            l.reverse()
            return l
        else:
            raise ValueError("Error Scoreboard index")

    # -------------------------------------------mutators---------------------------------

    def _score_equal(self, score2):
        for e in self._l:
            if e.score() == score2.score() and e.nome() == score2.nome() and e.date() == score2.date():
                return True
        return False

    def insert(self, s):
        """Inserisce un nuovo Score nello ScoreBoard se e solo se non è peggiore dei risultati correntemente salvati.
         Non incrementa la dimensione dello Scoreboard"""
        # ciclo finchè trovo maggiore. add_before. eccedo dimensione? cancello il primo
        # a parità del campo score, vale l'ordine d'inserimento il più recente viene prima
        self._score_validate(s)
        if self._score_equal(s):
            print("This score already exists.")
            return
        if self.size() == 0:
            self._l.add_first(s)
        else:
            check = self._l.first()
            while check != self._l.last() and s < check.element():
                check = PositionalList.after(self._l, check)
            else:
                if s < check.element():
                    self._l.add_after(check, s)
                else:
                    self._l.add_before(check, s)
            if self.size() > len(self):
                self._l.delete(self._l.last())

    # --------------------------------LE MERGE --------------------------------------------

    def merge(self, new):
        lista = merge(self._l, new._l)  # effettuo il merge
        self._l.clear()
        if lista.__len__() > self._dimension:  # se il merge ritorna una board più grande di dimension-> devo eliminare i peggiori
            count = lista.__len__() - self._dimension
            while count != 0:  # ciclo per cancellare gli elementi in eccesso
                last = lista.last()
                del lista[last]
                count -= 1
        for item in lista:  # aggiungo elementi da NewBoard a self essendo newBoard una circular positional list
            self.insert(item)
        lista.clear()

    def __str__(self):
        return str(self._l)
