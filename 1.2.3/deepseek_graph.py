import matplotlib.pyplot as plt
import numpy as np

# Ваши массивы (вставьте сюда данные выше)
h_squared = [0.00632025, 0.00555025, 0.00483025, 0.00416025, 0.00354025, 0.00297025, 0.00245025, 0.00198025, 0.00156025, 0.00119025, 0.00087025, 0.00060025, 0.00038025, 0.00021025, 0.00009025, 0.00002025, 0.00000025]
I_array = [0.016206, 0.017529, 0.016458, 0.015652, 0.014865, 0.013206, 0.011708, 0.012692, 0.011791, 0.011448, 0.011231, 0.010658, 0.010164, 0.010087, 0.010004, 0.009846, 0.009695]

plt.figure(figsize=(8, 6))

# Строим точки эксперимента
plt.scatter(h_squared, I_array, color='red', label='Экспериментальные точки')

# Строим линию тренда (аппроксимация полиномом 1-й степени, т.е. прямой)
# Игнорируем точку с индексом 1 (выброс), для этого создадим маски
h_clean = [h_squared[i] for i in range(len(h_squared)) if i != 1]
I_clean = [I_array[i] for i in range(len(I_array)) if i != 1]

coeffs = np.polyfit(h_clean, I_clean, 1) # y = ax + b
trendline = np.polyval(coeffs, h_squared)

plt.plot(h_squared, trendline, color='blue', linestyle='--' )

plt.title('Зависимость момента инерции I от квадрата расстояния h^2')
plt.xlabel('h^2, м^2')
plt.ylabel('I, кг·м^2')
plt.grid(True, linestyle=':', alpha=0.6)
plt.ylim(0,0.017)
plt.show()