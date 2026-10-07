import numpy as np
import matplotlib.pyplot as plt

# Ваши полные массивы данных
h_squared = [
    0.00632025, 0.00555025, 0.00483025, 0.00416025, 0.00354025, 
    0.00297025, 0.00245025, 0.00198025, 0.00156025, 0.00119025, 
    0.00087025, 0.00060025, 0.00038025, 0.00021025, 0.00009025, 
    0.00002025, 0.00000025
]
I_array = [
    0.016206, 0.017529, 0.016458, 0.015652, 0.014865, 
    0.013206, 0.011708, 0.012692, 0.011791, 0.011448, 
    0.011231, 0.010658, 0.010164, 0.010087, 0.010004, 
    0.009846, 0.009695
]

# Выбираем только три точки по индексам 4, -3, -2
indices_for_fit = [16,15,14,13,12,11,10,9,8,7,4,3, 2, 1]
h_fit = [h_squared[i] for i in indices_for_fit]
I_fit = [I_array[i] for i in indices_for_fit]

# Строим линию тренда (полином 1-й степени) только по этим трем точкам
coefficients = np.polyfit(h_fit, I_fit, 1) # y = ax + b
trendline_y = np.polyval(coefficients, h_squared)

# Вывод уравнения в консоль
print(f"Уравнение линии тренда: I = {coefficients[0]:.4f} * h^2 + {coefficients[1]:.6f}")

# --- Построение графика ---
plt.figure(figsize=(9, 6))

# 1. Все экспериментальные точки (серые)
plt.scatter(h_squared, I_array, color='lightgray', edgecolor='black')

# 2. Выбранные три точки (красные, крупнее)
#plt.scatter(h_fit, I_fit, color='red', s=80, zorder=5)

# 3. Линия тренда по трем точкам (синяя)
plt.plot(h_squared, trendline_y, color='blue', linestyle='--', linewidth=2)
plt.ylim(0,0.02)
#plt.title('Зависимость момента инерции I от квадрата расстояния h^2\n(Тренд построен по трем точкам)', fontsize=12)
plt.xlabel('$h^2$, м$^2$', fontsize=12)
plt.ylabel('$I$, кг·м$^2$', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()