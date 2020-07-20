def une_drole_de_recursion(liste):
    n = len(liste)
    if n == 0:
            return True
    
    avant = une_drole_de_recursion(liste[0:-1])
    if n < 3:
        return avant and liste[n-1] == 1
    else:
        return avant and liste[n-1] == liste[n-2] + liste[n-3]