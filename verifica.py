from ScoreBoard import *
import unittest

# Run all'esterno della classe.
# Run all'interno di una funzione, determina l'esecuzione di una sola funzione test,
# tralasciando le altre.


class TestProject(unittest.TestCase):
    def test_mutators(self):
        print("---------------- test mutators -----------------")
        l = CircularPositionalList()
        self.assertTrue(l.is_empty())
        print("Lista vuota?", l.is_empty())
        p = l.add_last(50)
        l.add_last(60)
        self.assertFalse(l.is_empty())
        print("\nLista vuota?", l.is_empty())
        l.add_first(40)
        l.add_first(30)
        l.add_last(70)
        l.add_last(80)
        self.assertEqual(l.__str__(), "30,40,50,60,70,80")
        print("\nElementi della lista:")
        print(l)
        p = l.first()
        p = PositionalList.after(l, p)
        l.delete(p)
        p = l.last()
        p = PositionalList.before(l, p)
        with self.assertRaises(TypeError):
            l.delete(10)
        l.delete(p)
        with self.assertRaises(ValueError):
            l.before(p)
        self.assertEqual(l.__str__(), "30,50,60,80")
        print("\nElementi della lista:")
        print(l)
        p = l.first()
        l.add_before(p, 20)
        p = PositionalList.after(l, p)
        l.add_after(p, 40)
        p = l.last()
        l.add_before(p, 70)
        l.add_after(p, 90)
        self.assertEqual(l.__str__(), "20,30,50,40,60,70,80,90")
        print("\nElementi della lista:")
        print(l)
        l.clear()
        self.assertEqual(l.__str__(), "")
        l.add_first(30)
        l.add_last(70)
        l.add_last(80)
        self.assertEqual(l.__str__(), "30,70,80")
        p = l.last()
        l.replace(p, 100)
        p = PositionalList.before(l, p)
        l.replace(p, 90)
        p = PositionalList.before(l, p)
        l.replace(p, 40)
        self.assertEqual(l.__str__(), "40,90,100")
        print("\nElementi della lista:")
        print(l)
        l.clear()
        self.assertEqual(l.__str__(), "")
        l = None

    def test_accessories(self):
        print("---------------- test accessories -----------------")
        l = CircularPositionalList()
        p1 = l.add_first(50)
        print("Elementi della lista:")
        print(l)
        self.assertEqual(l.before(p1), None)
        self.assertEqual(l.after(p1), None)
        print("\nafter e before su una lista a singolo elemento sono risultati None")

        p2 = l.add_last(60)
        print("\nElementi della lista:")
        print(l)
        self.assertEqual(l.before(p2), 50)
        self.assertEqual(l.after(p1), 60)
        print("before e after sono risultati corretti. before: ", l.before(p2), " after: ", l.after(p1))

        l.add_first(40)
        l.add_last(70)
        print("\nElementi della lista:")
        print(l)
        self.assertEqual(l.find(20), None)
        self.assertEqual(l.find(50).element(), 50)
        print("\n La find di 20 ha ritornato", l.find(20), " invece la find su 50 ha ritornato", l.find(50).element())
        self.assertFalse(l.is_sorted())
        print("\nLista ordinata? ", l.is_sorted())
        l.reverse()
        self.assertEqual(l.__str__(), "70,60,50,40")
        print("\nLista invertita:\n", l)
        self.assertTrue(l.is_sorted())
        print("\nLista ordinata? ", l.is_sorted())

        l.add_last(50)
        print("\nElementi della lista:")
        print(l)
        self.assertEqual(l.count(20), 0)
        self.assertEqual(l.count(60), 1)
        self.assertEqual(l.count(50), 2)
        print("Count 20: ", l.count(20), "\nCount 60: ", l.count(60), "\nCount 50: ", l.count(50))

    def test_magic_method(self):
        print("---------------- test magic method -----------------")
        l = CircularPositionalList()
        l2 = CircularPositionalList()
        l.add_last(50)
        l.add_last(60)
        l.add_last(70)
        l.add_first(40)
        l2.add_first(60)
        print("\nElementi della lista1:")
        print(l)
        print("\nElementi della lista2:")
        print(l2)
        p = l.first()
        p2 = l2.first()
        self.assertTrue(p in l)
        self.assertFalse(p2 in l)
        self.assertFalse(5 in l)
        self.assertFalse(None in l)
        print("\nLa contains di position della lista uno è:", p in l)
        print("\nLa contains di position esterne:", p2 in l)
        print("\nLa contains di elementi che non sono position:", 5 in l, None in l)
        del l[p]
        self.assertFalse(p in l)
        p = l.last()
        del l[p]
        self.assertEqual(l.__str__(), "50,60")
        print("\nElementi della lista1 dopo la cancellazione di due elementi:")
        print(l)

        l.add_first(40)
        l.add_last(70)
        p = l.first()
        p = PositionalList.after(l, p)
        self.assertEqual(l[p], 50)
        print("\nGet_item di una position, in questo caso la seconda:", l[p])
        l[p] = 80
        self.assertEqual(l[p], 80)
        self.assertEqual(l.__str__(), "40,80,60,70")
        print("\nset_item di una position, in questo caso la seconda:\n", l)

        l2.clear()
        list_sum = l + l2
        self.assertEqual(list_sum.__str__(), "40,80,60,70")
        print("\nSomma tra la lista l e una vuota:\n", l)
        l2.add_last(100)
        list_sum = l + l2
        self.assertEqual(list_sum.__str__(), "40,80,60,70,100")
        print("\nSomma tra due liste:\n", list_sum)

    def test_bubblesort(self):
        print("---------------- test bubblesort -----------------")
        l = CircularPositionalList()

        list_assert = []
        with self.assertRaises(ValueError):
            for bubble in bubblesorted(l):
                list_assert.append(bubble)
        self.assertEqual(list_assert.__str__(), "[]")
        print("\nElementi della lista dopo bubble con lista vuota:")
        print(list_assert)
        p1 = l.add_first(100)
        for bubble in bubblesorted(l):
            list_assert.append(bubble)
        self.assertEqual(list_assert.__str__(), "[100]")
        print("\nElementi della lista dopo bubble avente un singolo elemento:")
        print(list_assert)
        list_assert.clear()
        p1 = l.add_last(102)
        p1 = l.add_first(103)
        print("\nElementi della lista:")
        print(l)
        for bubble in bubblesorted(l):
            list_assert.append(bubble)
        self.assertEqual(list_assert.__str__(), "[100, 102, 103]")
        print("\nElementi della lista dopo bubble:")
        print(list_assert)
        l.clear()
        list_assert.clear()
        p1 = l.add_first(100)
        l.delete(p1)
        p1 = l.add_last(102)
        p1 = l.add_first(103)
        for bubble in bubblesorted(l):
            list_assert.append(bubble)
        self.assertEqual(list_assert.__str__(), "[102, 103]")
        print("\nElementi della lista dopo il secondo bubble:")
        print(list_assert)
        with self.assertRaises(TypeError):
            for bubble in bubblesorted(5):
                list_assert.append(bubble)
        print("\nEccezione lanciata chiamando bubble passando in input un oggetto che non è una CircularPositionalList")

    def test_merge(self):
        print("---------------- test merge -----------------")
        l1 = CircularPositionalList()
        l2 = CircularPositionalList()
        l3 = CircularPositionalList()
        l_fusion = merge(l1, l2)
        self.assertEqual(l_fusion.__str__(), "")
        print("\nElementi lista_fusion con due liste vuote:")
        print(l_fusion)

        l_fusion = None

        l1.add_last(50)
        l1.add_last(40)
        l1.add_last(30)
        l1.add_last(20)
        l1.add_last(10)

        l_fusion = merge(l1, l3)
        self.assertEqual(l_fusion.__str__(), "50,40,30,20,10")

        print("\nElementi lista_fusion con seconda lista vuota:")
        print(l_fusion)

        l_fusion = None
        l_fusion = merge(l3, l1)
        self.assertEqual(l_fusion.__str__(), "50,40,30,20,10")

        print("\nElementi lista_fusion con prima lista vuota:")
        print(l_fusion)

        l_fusion = None

        # l2 ha più elementi di l1
        l2.add_last(75)
        l2.add_last(65)
        l2.add_last(55)
        l2.add_last(50)
        l2.add_last(45)
        l2.add_last(35)
        l2.add_last(25)
        l2.add_last(15)

        print("\nElementi della lista1:")
        print(l1)
        print("\nElementi della lista2:")
        print(l2)

        l_fusion = merge(l1, l2)
        self.assertEqual(l_fusion.__str__(), "75,65,55,50,50,45,40,35,30,25,20,15,10")
        print("\nElementi della lista_fusion:")
        print(l_fusion)
        l1.clear()
        l2.clear()
        l_fusion.clear()
        # l1 ha più elementi di l2
        l1.add_last(50)
        l1.add_last(40)
        l1.add_last(30)
        l1.add_last(20)
        l1.add_last(10)

        l2.add_last(35)
        l2.add_last(25)
        l2.add_last(15)

        l_fusion = merge(l1, l2)
        self.assertEqual(l_fusion.__str__(), "50,40,35,30,25,20,15,10")

        l_fusion.clear()
        # l1 non è ordinata
        p = l1.add_first(35)
        with self.assertRaises(ValueError):
            l_fusion = merge(l1, l2)

        del l1[p]
        # l2 non è ordinata
        p = l2.add_first(5)
        with self.assertRaises(ValueError):
            l_fusion = merge(l1, l2)

        del l2[p]
        # una delle liste o entrambe non sono CircularPositionalList
        with self.assertRaises(TypeError):
            l_fusion = merge(2, l2)

        with self.assertRaises(TypeError):
            l_fusion = merge(l1, 2)

        with self.assertRaises(TypeError):
            l_fusion = merge(2, 2)

    def test_scoreboard(self):
        print("---------------- test scorboard -----------------")
        with self.assertRaises(TypeError):
            scoreboard = ScoreBoard("ciao")
            scoreboard = ScoreBoard(5.23)
        with self.assertRaises(ValueError):
            scoreboard = ScoreBoard(0)
            scoreboard = ScoreBoard(-1)
        print("\nLa creazione di scoreboard con input un parametri diverso da intero o minore di zero ha fatto "
              "scattare l'eccezione")
        scoreboard = ScoreBoard(2)
        self.assertTrue(scoreboard.is_empty())
        print("\nScoreboard appena creato vuoto?", scoreboard.is_empty())
        score1 = ScoreBoard.Score('marco', 10, '16 settembre')
        score2 = ScoreBoard.Score('marco', 10, '16 settembre')
        score3 = ScoreBoard.Score('marco', 149, '16 settembre')
        scoreboard.insert(score1)
        self.assertFalse(scoreboard.is_empty())
        scoreboard.insert(score2)
        scoreboard.insert(score3)
        self.assertFalse(scoreboard.is_empty())
        # Score uguali non li reinserisce
        self.assertEqual(scoreboard.__str__(), "149 - marco - 16 settembre,10 - marco - 16 settembre")
        print("\nInseriti 3 elementi di cui due uguali, quelli uguali sono inseriti solo una volta:")
        print(scoreboard)

        scoreboard2 = ScoreBoard(5)

        d = ScoreBoard.Score("ugo", 30, "01/08/2018")
        e = ScoreBoard.Score("ugo", 35, "01/08/2018")
        f = ScoreBoard.Score("ugo", 40, "01/08/2018")
        g = ScoreBoard.Score("ugo", 45, "01/08/2018")
        h = ScoreBoard.Score("ugo", 50, "01/08/2018")
        i = ScoreBoard.Score("ugo", 55, "01/08/2018")
        j = ScoreBoard.Score("ugo", 69, "01/08/2018")
        z = ScoreBoard.Score("ugo", 69, "01/08/2018")

        scoreboard2.insert(d)
        scoreboard2.insert(e)
        scoreboard2.insert(f)
        scoreboard2.insert(g)
        scoreboard2.insert(h)
        scoreboard2.insert(i)
        scoreboard2.insert(j)
        scoreboard2.insert(z)
        print("\nLo Score z uguale a j perciò non verrà inserito\n")
        # inserimento più elementi della dimension dello Scoreboard
        self.assertEqual(scoreboard2.__str__(), "69 - ugo - 01/08/2018,55 - ugo - 01/08/2018,50 - ugo - 01/08/2018,"
                                                "45 - ugo - 01/08/2018,40 - ugo - 01/08/2018")

        print("Creato un altro scoreboard di 5 elementi con in ingresso 7 score, "
              "gli elementi con score minori vengono scartati:")
        print(scoreboard2)
        # Recupero i top 3 Score
        top3 = scoreboard2.top(3)
        l = []
        for e in top3:
            l.append(e.__str__())

        self.assertEqual(l.__str__(), "['69 - ugo - 01/08/2018', '55 - ugo - 01/08/2018', '50 - ugo - 01/08/2018']")
        print("\nRecupero i top 3 score:")
        print(l)
        l.clear()

        # Recupero tutti gli elementi dello score tramite top
        top5 = scoreboard2.top(5)
        for e in top5:
            l.append(e.__str__())

        self.assertEqual(l.__str__(), "['69 - ugo - 01/08/2018', '55 - ugo - 01/08/2018', '50 - ugo - 01/08/2018', "
                                      "'45 - ugo - 01/08/2018', '40 - ugo - 01/08/2018']")
        print("\nRecupero tutti gli score tramite top:")
        print(l)
        l.clear()

        # Recupero i last 4 Score
        last4 = scoreboard2.last(4)

        for e in last4:
            l.append(e.__str__())
        self.assertEqual(l.__str__(), "['55 - ugo - 01/08/2018', '50 - ugo - 01/08/2018', '45 - ugo - 01/08/2018', "
                                      "'40 - ugo - 01/08/2018']")
        print("\nRecupero i last 4 score:")
        print(l)
        l.clear()

        # Recupero tutti gli elementi dello score tramite last
        last5 = scoreboard2.last(5)
        for e in last5:
            l.append(e.__str__())

        self.assertEqual(l.__str__(), "['69 - ugo - 01/08/2018', '55 - ugo - 01/08/2018', '50 - ugo - 01/08/2018', "
                                      "'45 - ugo - 01/08/2018', '40 - ugo - 01/08/2018']")
        print("\nRecupero tutti gli score tramite last:")
        print(l)
        l.clear()
        l = None

        # Cerco di recuperare un numero di score pari a 0 o minore di 0
        with self.assertRaises(ValueError):
            top0 = scoreboard2.top(0)
            top_1 = scoreboard2.top(-1)
            last0 = scoreboard2.last(0)
            last_1 = scoreboard2.last(-1)
        print("\nSono scattate le eccezioni di top e last con valori minori o uguali a 0")

        with self.assertRaises(TypeError):
            top0 = scoreboard2.top("ciao")
            last0 = scoreboard2.last("ciao")
        print("\nSono scattate le eccezioni di top e last con input che non sono interi")

        # Cerco di recuperare un numero di score superiore alla size dello Scoreboard
        with self.assertRaises(ValueError):
            top0 = scoreboard2.top(6)
            top_1 = scoreboard2.top(20)
            last0 = scoreboard2.last(6)
            last0 = scoreboard2.last(20)
        print("\nSono scattate le eccezioni di top e last con valori più grandi della dimensione dello scoreboard")

        # Eseguo la merge tra i due scoreboard
        # test con uno degli scoreboard vuoto
        scoreboard3 = ScoreBoard()
        scoreboard.merge(scoreboard3)
        self.assertEqual(scoreboard.__str__(), "149 - marco - 16 settembre,10 - marco - 16 settembre")
        print("\nMerge con secondo Scoreboard vuoto:")
        print(scoreboard)
        # test tra due Scoreboard vuoti
        scoreboard4 = ScoreBoard()
        scoreboard3.merge(scoreboard4)
        self.assertEqual(scoreboard3.__str__(), "")
        print("\nMerge entrambi Scoreboard vuoti:")
        print(scoreboard3)
        # test con due scoreboard
        scoreboard.merge(scoreboard2)
        self.assertEqual(scoreboard.__str__(), "149 - marco - 16 settembre,69 - ugo - 01/08/2018")
        print("\nMerge tra due scoreboard:")
        print(scoreboard)

    def test_copy(self):
        print("---------------- test copy -----------------")
        l1 = CircularPositionalList()
        print("Test mutators su entrambe le liste")
        self.assertTrue(l1.is_empty())
        print("\nLista1 vuota?", l1.is_empty())
        p = l1.add_last(50)
        l1.add_last(60)
        self.assertFalse(l1.is_empty())
        print("\nLista1 vuota?", l1.is_empty())
        l1.add_first(40)
        l1.add_first(30)
        l1.add_last(70)
        l1.add_last(80)
        l2 = l1.copy()
        print("\nLista 1 copiata")
        self.assertEqual(l1.__str__(), "30,40,50,60,70,80")
        print("\nElementi della lista1:")
        print(l1)
        p = l1.first()
        p = PositionalList.after(l1, p)
        l1.delete(p)
        p = l1.last()
        p = PositionalList.before(l1, p)
        with self.assertRaises(TypeError):
            l1.delete(10)
        l1.delete(p)
        with self.assertRaises(ValueError):
            l1.before(p)
        self.assertEqual(l1.__str__(), "30,50,60,80")
        print("\nElementi della lista1:")
        print(l1)
        p = l1.first()
        l1.add_before(p, 20)
        p = PositionalList.after(l1, p)
        l1.add_after(p, 40)
        p = l1.last()
        l1.add_before(p, 70)
        l1.add_after(p, 90)
        self.assertEqual(l1.__str__(), "20,30,50,40,60,70,80,90")
        print("\nElementi della lista1:")
        print(l1)
        l1.clear()
        self.assertEqual(l1.__str__(), "")
        l1.add_first(30)
        l1.add_last(70)
        l1.add_last(80)
        self.assertEqual(l1.__str__(), "30,70,80")
        p = l1.last()
        l1.replace(p, 100)
        p = PositionalList.before(l1, p)
        l1.replace(p, 90)
        p = PositionalList.before(l1, p)
        l1.replace(p, 40)
        self.assertEqual(l1.__str__(), "40,90,100")
        print("\nElementi della lista1:")
        print(l1)
        l1.clear()
        self.assertEqual(l1.__str__(), "")
        l1 = None

        self.assertFalse(l2.is_empty())
        print("\nLista vuota2?", l2.is_empty())
        self.assertEqual(l2.__str__(), "30,40,50,60,70,80")
        print("\nElementi della lista2:")
        print(l2)
        p = l2.first()
        p = PositionalList.after(l2, p)
        l2.delete(p)
        p = l2.last()
        p = PositionalList.before(l2, p)
        with self.assertRaises(TypeError):
            l2.delete(10)
        l2.delete(p)
        with self.assertRaises(ValueError):
            l2.before(p)
        self.assertEqual(l2.__str__(), "30,50,60,80")
        print("\nElementi della lista2:")
        print(l2)
        p = l2.first()
        l2.add_before(p, 20)
        p = PositionalList.after(l2, p)
        l2.add_after(p, 40)
        p = l2.last()
        l2.add_before(p, 70)
        l2.add_after(p, 90)
        self.assertEqual(l2.__str__(), "20,30,50,40,60,70,80,90")
        print("\nElementi della lista2:")
        print(l2)
        l2.clear()
        self.assertEqual(l2.__str__(), "")
        l2.add_first(30)
        l2.add_last(70)
        l2.add_last(80)
        self.assertEqual(l2.__str__(), "30,70,80")
        p = l2.last()
        l2.replace(p, 100)
        p = PositionalList.before(l2, p)
        l2.replace(p, 90)
        p = PositionalList.before(l2, p)
        l2.replace(p, 40)
        self.assertEqual(l2.__str__(), "40,90,100")
        print("\nElementi della lista2:")
        print(l2)
        l2.clear()
        self.assertEqual(l2.__str__(), "")
        l2 = None

        print("\nTest accessories su entrambe le liste")
        l1 = CircularPositionalList()
        l2 = l1.copy()
        print("\nLista 1 copiata")
        p1 = l1.add_first(50)
        print("\nElementi della lista1:")
        print(l1)
        self.assertEqual(l1.before(p1), None)
        self.assertEqual(l1.after(p1), None)
        print("\nafter e before sulla lista1 a singolo elemento sono risultati None")

        p2 = l1.add_last(60)
        print("\nElementi della lista1:")
        print(l1)
        self.assertEqual(l1.before(p2), 50)
        self.assertEqual(l1.after(p1), 60)
        print("\nbefore e after sono risultati corretti. before: ", l1.before(p2), " after: ", l1.after(p1))

        l1.add_first(40)
        l1.add_last(70)
        print("\nElementi della lista1:")
        print(l1)
        self.assertEqual(l1.find(20), None)
        self.assertEqual(l1.find(50).element(), 50)
        print("\nLa find di 20 ha ritornato", l1.find(20), " invece la find su 50 ha ritornato", l1.find(50).element())
        self.assertFalse(l1.is_sorted())
        print("\nLista1 ordinata? ", l1.is_sorted())
        l1.reverse()
        self.assertEqual(l1.__str__(), "70,60,50,40")
        print("\nLista1 invertita:\n", l1)
        self.assertTrue(l1.is_sorted())
        print("\nLista1 ordinata? ", l1.is_sorted())

        l1.add_last(50)
        print("\nElementi della lista1:")
        print(l1)
        self.assertEqual(l1.count(20), 0)
        self.assertEqual(l1.count(60), 1)
        self.assertEqual(l1.count(50), 2)
        print("\nCount 20: ", l1.count(20), "\nCount 60: ", l1.count(60), "\nCount 50: ", l1.count(50))

        p1 = l2.add_first(50)
        print("\nElementi della lista2:")
        print(l2)
        self.assertEqual(l2.before(p1), None)
        self.assertEqual(l2.after(p1), None)
        print("\nafter e before sulla lista2 a singolo elemento sono risultati None")

        p2 = l2.add_last(60)
        print("\nElementi della lista2:")
        print(l2)
        self.assertEqual(l2.before(p2), 50)
        self.assertEqual(l2.after(p1), 60)
        print("\nbefore e after sono risultati corretti. before: ", l2.before(p2), " after: ", l2.after(p1))

        l2.add_first(40)
        l2.add_last(70)
        print("\nElementi della lista2:")
        print(l2)
        self.assertEqual(l2.find(20), None)
        self.assertEqual(l2.find(50).element(), 50)
        print("\nLa find di 20 ha ritornato", l2.find(20), " invece la find su 50 ha ritornato", l2.find(50).element())
        self.assertFalse(l2.is_sorted())
        print("\nLista2 ordinata? ", l2.is_sorted())
        l2.reverse()
        self.assertEqual(l2.__str__(), "70,60,50,40")
        print("\nLista2 invertita:\n", l2)
        self.assertTrue(l2.is_sorted())
        print("\nLista2 ordinata? ", l2.is_sorted())

        l2.add_last(50)
        print("\nElementi della lista2:")
        print(l2)
        self.assertEqual(l2.count(20), 0)
        self.assertEqual(l2.count(60), 1)
        self.assertEqual(l2.count(50), 2)
        print("\nCount 20: ", l2.count(20), "\nCount 60: ", l2.count(60), "\nCount 50: ", l2.count(50))

        l1.clear()
        l1 = None
        l2.clear()
        l2 = None

        print("\nTest magic method su entrambe le liste")
        l1 = CircularPositionalList()
        l2 = l1.copy()
        print("\nLista 1 copiata")
        l_support = CircularPositionalList()

        l1.add_last(50)
        l1.add_last(60)
        l1.add_last(70)
        l1.add_first(40)
        l_support.add_first(60)
        print("\nElementi della lista1:")
        print(l1)
        print("\nElementi della lista support:")
        print(l_support)
        p = l1.first()
        p2 = l_support.first()
        self.assertTrue(p in l1)
        self.assertFalse(p2 in l1)
        self.assertFalse(5 in l1)
        self.assertFalse(None in l1)
        print("\nLa contains di position della lista uno è:", p in l1)
        print("\nLa contains di position esterne:", p2 in l1)
        print("\nLa contains di elementi che non sono position:", 5 in l1, None in l1)
        del l1[p]
        self.assertFalse(p in l1)
        p = l1.last()
        del l1[p]
        self.assertEqual(l1.__str__(), "50,60")
        print("\nElementi della lista1 dopo la cancellazione di due elementi:")
        print(l1)

        l1.add_first(40)
        l1.add_last(70)
        p = l1.first()
        p = PositionalList.after(l1, p)
        self.assertEqual(l1[p], 50)
        print("\nGet_item di una position, in questo caso la seconda:", l1[p])
        l1[p] = 80
        self.assertEqual(l1[p], 80)
        self.assertEqual(l1.__str__(), "40,80,60,70")
        print("\nset_item di una position, in questo caso la seconda:\n", l1)

        l_support.clear()
        list_sum = l1 + l_support
        self.assertEqual(list_sum.__str__(), l1.__str__())
        print("\nSomma tra la lista l e una vuota:\n", list_sum)
        l_support.add_last(100)
        list_sum = l1 + l_support
        self.assertEqual(list_sum.__str__(), "40,80,60,70,100")
        print("\nSomma tra due liste:\n", list_sum)
        l_support.clear()
        list_sum.clear()
        list_sum = None

        l2.add_last(50)
        l2.add_last(60)
        l2.add_last(70)
        l2.add_first(40)
        l_support.add_first(60)
        print("\nElementi della lista2:")
        print(l2)
        print("\nElementi della lista support:")
        print(l_support)
        p = l2.first()
        p2 = l_support.first()
        self.assertTrue(p in l2)
        self.assertFalse(p2 in l2)
        self.assertFalse(5 in l2)
        self.assertFalse(None in l2)
        print("\nLa contains di position della lista due è:", p in l2)
        print("\nLa contains di position esterne:", p2 in l2)
        print("\nLa contains di elementi che non sono position:", 5 in l2, None in l2)
        del l2[p]
        self.assertFalse(p in l2)
        p = l2.last()
        del l2[p]
        self.assertEqual(l2.__str__(), "50,60")
        print("\nElementi della lista2 dopo la cancellazione di due elementi:")
        print(l2)

        l2.add_first(40)
        l2.add_last(70)
        p = l2.first()
        p = PositionalList.after(l2, p)
        self.assertEqual(l2[p], 50)
        print("\nGet_item di una position, in questo caso la seconda:", l2[p])
        l2[p] = 80
        self.assertEqual(l2[p], 80)
        self.assertEqual(l2.__str__(), "40,80,60,70")
        print("\nset_item di una position, in questo caso la seconda:\n", l2)

        l_support.clear()
        list_sum = l2 + l_support
        self.assertEqual(list_sum.__str__(), l2.__str__())
        print("\nSomma tra la lista 2 e una vuota:\n", list_sum)
        l_support.add_last(100)
        list_sum = l2 + l_support
        self.assertEqual(list_sum.__str__(), "40,80,60,70,100")
        print("\nSomma tra due liste:\n", list_sum)
        l_support.clear()
        list_sum.clear()
        list_sum = None


if __name__ == "__main__":
    unittest.main()
