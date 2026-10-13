import matplotlib.pyplot as plt
import numpy as np

# 1. Входные данные
M_grams = np.array([1010, 1992, 1442, 546])
nu1_prakt = np.array([134.529, 184.47, 157.42, 97.0])

# 2. Перевод в СИ
M_kg = M_grams / 1000.0
g = 9.81
F = M_kg * g  # Сила в Ньютонах

# 3. Расчет u и u^2
# u = nu1 * 2L, где 2L = 1 м, поэтому u = nu1
u = nu1_prakt
u_squared = u**2

# 4. Линейная регрессия (y = kx + b)
# Мы ищем зависимость u^2 = (1/rho_l) * F
coeffs = np.polyfit(F, u_squared, 1)
k = coeffs[0]  # Коэффициент наклона
b = coeffs[1]  # Свободный член (в идеале должен быть близок к 0)

# 5. Расчет погонной плотности
rho_l = 1 / k  # в кг/м

# 6. Построение графика
plt.figure(figsize=(10, 6))

# Точки эксперимента
plt.scatter(F, u_squared, color='red', s=60, label='Экспериментальные точки')

# Линия тренда
x_fit = np.linspace(0, max(F)*1.1, 100)
y_fit = k * x_fit + b
plt.plot(x_fit, y_fit, 'b--', label=f'Линейный тренд: \(u^2 = {k:.2f} \cdot F + {b:.2f}\)')

# Оформление
plt.title('Зависимость квадрата скорости u^2 от силы натяжения F', fontsize=14)
plt.xlabel('Сила натяжения F, Н', fontsize=12)
plt.ylabel('Квадрат скорости u^2, (м/с)^2', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)

# Добавляем текст с результатом на график
#plt.text(0.05, 0.95, f'Коэф. наклона \(k = {k:.2f}\)\n\(\u03C1_l = 1/k = {rho_l:.6f}\) кг/м\n\(\u03C1_l = {rho_l*1000:.3f}\) г/м', 
#         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top',
#         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

#plt.legend()
plt.tight_layout()
plt.show()

print(f"Коэффициент наклона k = {k:.2f}")
print(f"Погонная плотность rho_l = {rho_l:.6f} кг/м = {rho_l*1000:.3f} г/м")