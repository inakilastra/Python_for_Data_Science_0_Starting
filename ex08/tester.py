from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

# Prueba con la función personalizada ft_tqdm
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# Prueba con la función tqdm original para comparación
for elem in tqdm(range(333)):
    sleep(0.005)
print()
