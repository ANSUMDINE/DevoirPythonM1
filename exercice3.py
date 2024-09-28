class Exo:
    def puissance(self, x, n):
        # Cas de base
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.puissance(x, -n)
        # Cas où n est pair
        elif n % 2 == 0:
            half_power = self.puissance(x, n // 2)
            return half_power * half_power
        # Cas où n est impair
        else:
            return x * self.puissance(x, n - 1)

# Exemples d'utilisation
exo = Exo()
print(exo.puissance(2, 3))  # Retourne 8
print(exo.puissance(2, 1))  # Retourne 2
print(exo.puissance(2, 0))  # Retourne 1
print(exo.puissance(2, -3)) # Retourne 0.125
