def trouver_maximum(liste):
    if not liste:
        return None
    
    max_val = liste[0]
    for n in liste:
        if n > max_val:
            max_val = n
    return max_val

# Bach t-testi l-khidma (ikhtiyari):
test_liste = [12, 45, 2, 89, 34]
print("Le maximum est:", trouver_maximum(test_liste))