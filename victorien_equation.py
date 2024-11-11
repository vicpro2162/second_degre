import cmath  # Importation de la bibliothèque cmath pour les calculs avec des nombres complexes

# Demande des valeurs des coefficients a, b et c à l'utilisateur
print('Entrez la valeur de a:')
a = int(input())  
print('Entrez la valeur de b:')
b = int(input())
print('Entrez la valeur de c:')
c = int(input())  

# Vérification si a est égal à 0, dans ce cas ce n'est pas une équation du second degré
a<0 or a>0 
while a = 0:
    print("Ce n'est pas une équation du second degré. Veuillee entrer une valeur de a différent de 0")
else:
# Affichage de l'équation 
   equation = f"{a}x²" + (f" +{b}x" if b > 0 else f"" if b == 0 else f" {b}x") + (f" +{c}" if c > 0 else f"" if c == 0 else f" {c}")
   print(equation)  

# Définition de la fonction solution pour résoudre l'équation du second degré
def solution(a, b, c):
    D = b**2 - 4*a*c  # Calcul du discriminant
    if D > 0:
        # Si le discriminant est positif, il y a deux solutions réelles
        sol1 = (-b + cmath.sqrt(D)) / (2*a)
        sol2 = (-b - cmath.sqrt(D)) / (2*a)
        # Arrondir les parties réelle et imaginaire des solutions à 2 chiffres après la virgule
        return round(sol1.real, 2) + round(sol1.imag, 2)*1j, round(sol2.real, 2) + round(sol2.imag, 2)*1j
    elif D == 0:
        # Si le discriminant est zéro, il y a une solution réelle double
        sol = -b / (2*a)
        return round(sol, 2),
    else:
        # Si le discriminant est négatif, il y a deux solutions complexes
        sol1 = (-b + cmath.sqrt(D)) / (2*a)
        sol2 = (-b - cmath.sqrt(D)) / (2*a)
        # Arrondir les parties réelle et imaginaire des solutions à 2 chiffres après la virgule
        return round(sol1.real, 2) + round(sol1.imag, 2)*1j, round(sol2.real, 2) + round(sol2.imag, 2)*1j

# Appel de la fonction solution avec les coefficients a, b et c
solutions = solution(a, b, c)
# Affichage des solutions de l'équation
print("Les solutions de votre équation sont:", solutions)
