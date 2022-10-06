from itertools import combinations, permutations

datas = ["a", "b", "c", "d", "e"]

def powerset(list):
    listPwd = []
    for i in range(len(list)):
        for items in combinations(list, i+1):
            pwd = ""
            for j in permutations(items):
                print(j)
                for item in j:
                    if item:
                        pwd = pwd + item
                    pass
                pass
            print(pwd)
            pass
        listPwd.append(pwd)
        pass
    return listPwd

A = ["60", "7", 'Hi']

for x in powerset(A):
    print(x)