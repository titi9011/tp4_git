from copy import copy

test_dic = {'thierry': 0}

test_dic2 = copy(test_dic)

del test_dic['thierry']
print(test_dic2)