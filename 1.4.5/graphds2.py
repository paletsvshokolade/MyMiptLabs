import matplotlib.pyplot as plt
import numpy as np

# Ось X: номера гармоник
n = np.array([1, 2, 3, 4, 5, 6, 7])

# ==========================================
# 1. ТЕОРЕТИЧЕСКИЕ ДАННЫЕ (4 массива)
# ==========================================
nu_teor_1010 = np.array([131.53, 263.058, 394.587, 526.116, 656.765, 789.174, 919.47])
nu_teor_1992 = np.array([185.46, 370.92, 556.38, 741.84, 927.3, 1112.761, 1298.221])
nu_teor_1442 = np.array([157.79, 315.58, 473.37, 631.165, 788.956, 946.747, 1104.53])
nu_teor_546  = np.array([97.064, np.nan, 291.192, np.nan, 485.32, np.nan, 679.45])

# ==========================================
# 2. ПРАКТИЧЕСКИЕ ДАННЫЕ (4 массива)
# ==========================================
nu_prakt_1010 = np.array([134.529, 258.47, 393.987, 526.47, 651.987, 798.47, 919.47])
nu_prakt_1992 = np.array([184.47, 365.27, 556.07, 736.77, 923.87, 1114.87, 1297.87])
nu_prakt_1442 = np.array([157.42, 313.3, 473.3, 636.07, 787.95, 946.95, 1104.95])
nu_prakt_546  = np.array([97.0, np.nan, 291.37, np.nan, 489.14, np.nan, 680.15])

# ==========================================
# 3. ПОСТРОЕНИЕ ГРАФИКА
# ==========================================
plt.figure(figsize=(12, 8))

# --- Масса 1010 г (Красный) ---
plt.plot(n, nu_teor_1010, 'r--', label='Теория, M=1010 г')
plt.plot(n, nu_prakt_1010, 'r-o', label='Практика, M=1010 г')

# --- Масса 1992 г (Синий) ---
plt.plot(n, nu_teor_1992, 'b--', label='Теория, M=1992 г')
plt.plot(n, nu_prakt_1992, 'b-o', label='Практика, M=1992 г')

# --- Масса 1442 г (Зеленый) ---
plt.plot(n, nu_teor_1442, 'g--', label='Теория, M=1442 г')
plt.plot(n, nu_prakt_1442, 'g-o', label='Практика, M=1442 г')

# --- Масса 546 г (Оранжевый) ---
plt.plot(n, nu_teor_546, color='orange', linestyle='--', label='Теория, M=546 г')
plt.plot(n, nu_prakt_546, color='orange', marker='o', linestyle='-', label='Практика, M=546 г')

# === ДОБАВЛЯЕМ ЛИНЕЙНЫЙ ТРЕНД ДЛЯ 546 г ===
# Отфильтровываем NaN, иначе polyfit выдаст ошибку
mask = ~np.isnan(nu_prakt_546)
n_valid = n[mask]
nu_valid = nu_prakt_546[mask]

# Считаем линейную регрессию (полином 1-й степени)
coeffs = np.polyfit(n_valid, nu_valid, 1)
trend_546 = np.polyval(coeffs, n_valid)

# Рисуем тренд толстой пунктирной линией
plt.plot(n_valid, trend_546, color='orange', linestyle=':', linewidth=3, label='Тренд (M=546 г)')
# ==========================================

# Настройка осей и заголовка
plt.title('Зависимость частоты ν от номера гармоники n', fontsize=14)
plt.xlabel('Номер гармоники (n)', fontsize=12)
plt.ylabel('Частота ν, Гц', fontsize=12)

plt.xticks(n)
plt.grid(True, linestyle=':', alpha=0.7)
#plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()