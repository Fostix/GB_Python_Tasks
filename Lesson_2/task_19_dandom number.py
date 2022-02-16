# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел.

import time

mixer = str(time.time())
mixer = int(mixer.replace('.', '')) % 100

print(mixer)