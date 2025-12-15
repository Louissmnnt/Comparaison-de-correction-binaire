# Ce document permet l'import de la matrice polaire caractéristique de l'algorithme éponyme

import numpy as np

Polar_8bits = np.array([[1,0,0,0,0,0,0,0],
                        [1,1,0,0,0,0,0,0],
                        [1,0,1,0,0,0,0,0],
                        [1,1,1,1,0,0,0,0],
                        [1,0,0,0,1,0,0,0],
                        [1,1,0,0,1,1,0,0],
                        [1,0,1,0,1,0,1,0],
                        [1,1,1,1,1,1,1,1]])

u = np.array([1, 0, 1, 0, 0, 0, 0, 0])  # exemple (bits gelés inclus)

x = u @ G8 % 2
print(x)
