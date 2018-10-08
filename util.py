from random import randint

#Genera una lista casuale di n valori interi compresi tra a e b inclusi
def randList(a,b,n):
    lst = list()
    for i in range(n):
        lst.append(randint(a,b))
    return lst

#Genera una lista casuale di n valori interi distinti compresi tra a e b inclusi
def rand_keys_list(n,a,b):
    lst = list()
    i = 0
    while i < n:
        key = randint(a,b)
        if key not in lst:
            lst.append(key)
            i += 1
    return lst

#Genera una stringa casuale di n caratteri
def random_string(n):
    alphabet = 'abcdefghijklmnopqrstuvxwyz'
    rnd_str = ''
    for i in range(n):
        pos = randint(0,25)
        rnd_str += alphabet[pos]
    return rnd_str


#Genera una lista di n stringhe  casuali di lunghezza compresa tra min_len e  max_len inclusi
def rand_words_list(n, min_len, max_len):
    lst = []
    for i in range(n):
        length = randint(min_len,max_len)
        rnd_str = random_string(length)
        lst.append(rnd_str)
    return lst


#Genera un dizionario casule di n elementi con
# chiavi: valori interi compresi tra a e b inclusi
# elementi: stringhe casuali di lunghezza compresa tra min_len e  max_len inclusi
def rand_dict(n, a=1, b=999999, min_len=4, max_len=8):
    keys = rand_keys_list(n,a,b)
    values = rand_words_list(n, min_len, max_len)
    rnd_dt = {}
    for i in range(n):
        rnd_dt[keys[i]] = values[i]
    return rnd_dt

if __name__ == '__main__':
    print(random_string(4))
    print(rand_words_list(10, 3, 9))
    rd = rand_dict(10, 1, 20)
    print(rd)