from list.positional_list import PositionalList
#TdP_collections.

class MyList(PositionalList):
    def __len__(self):
        """Return the number of elements in the list"""
        return self._size

    def before(self, p):
        node = self._validate(p)
        if node._prev ==  self._header._next:
            return self._make_position(self._trailer._prev)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        if node._next == self._trailer._prev:
            return self._make_position(self._header._next)
        return self._make_position(node._next)

    def add_first(self, e):
        first=super().add_first(e)
        first._prev=self._trailer._prev
        last=self.last()
        self._trailer._prev=last
        return self._make_position(first)
       # if self.is_empty():
        #    node = self._insert_between(e, self._header, self._header._next)
         #   node._prev = node
            #node._next = self._header._next
          #  node._next = node
           # self._trailer._prev = node
            #return node
        #node = self._insert_between(e, self._header, self._header._next)
        #node._prev = self._trailer._prev

        #self._trailer._prev=node


        #return node

    def add_last(self, e):
        last=super().add_last(e)
        last.__next=self._header._next

        return self._make_position(last)
        #return last
        #if self.is_empty():
            #node = self._insert_between(e, self._trailer._prev, self._trailer)
            #node._prev = node
            #node._next = node
            #return node
            #return self.add_first(e)
       # node = self._insert_between(e, self._trailer._prev, self._trailer)
        #node._next = self._header._next
        #self._trailer._prev = node già fatta internamente
        #return node

    def add_after(self, p, e):
        node=self._validate(p)
        return super()._insert_between(e,p,p._next)



    def add_before(self, p, e):
        node=self._validate(p)
        return super()._insert_between(e,p._prev,p)

    def find(self, e):
        pass

    def delete(self, p):
        pass

    def clear(self):
        pass

    def count(self, e):
        pass

    def reverse(self):
        pass

    def copy(self):
        pass

    def __add__(self, other):
        pass

    def __contains__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    # def __iter__(self):
    #     pass

    # def __str__(self):
    #     pass

if __name__ == "__main__":
    l = MyList()


    print(l.is_empty())
    l.add_last(60)
    l.add_last(50)
    l.add_last(70)

    l.add_first(10)

    print(l.is_empty())
    l.add_first(20)
    l.add_last(40)

    print(l.is_empty())
    l.add_first(30)
    #first=l.last()
    #l.add_before(first,15)
    print("ciao")
    #print(before.element())



    for e in l:
        print(e)
