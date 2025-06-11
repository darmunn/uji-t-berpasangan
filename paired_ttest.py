# paired_ttest.py

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca file Excel (data harus ada di folder yang sama)
filename = 'data_uji.xlsx'
data = pd.read_excel(filename)

# Membaca kolom Before dan After dari file Excel
before = data['Before'].to_numpy()
after = data['After'].to_numpy()

# Menampilkan data
print("Data yang dibaca dari file Excel:")
print(data)

# Menghitung selisih
data['Difference'] = after - before

# Ringkasan statistik
print("\nRingkasan Statistik:")
print(data.describe())

# Uji normalitas (Shapiro-Wilk)
shapiro_before = stats.shapiro(before)
shapiro_after = stats.shapiro(after)

print("\nUji Normalitas (Shapiro-Wilk):")
print(f"Before: Statistic={shapiro_before.statistic:.4f}, p-value={shapiro_before.pvalue:.4f}")
print(f"After : Statistic={shapiro_after.statistic:.4f}, p-value={shapiro_after.pvalue:.4f}")

# Melakukan uji t dua sampel berpasangan
t_stat, p_value = stats.ttest_rel(before, after)

print("\nHasil Paired Sample T-Test:")
print(f"T-Statistic = {t_stat:.4f}")
print(f"P-Value     = {p_value:.4f}")

# Interpretasi hasil uji
alpha = 0.05
if p_value < alpha:
    print("Kesimpulan: Ada perbedaan signifikan (tolak H0).")
else:
    print("Kesimpulan: Tidak ada perbedaan signifikan (gagal tolak H0).")

# Visualisasi hasil dengan boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(data=pd.melt(data[['Before', 'After']]), x='variable', y='value', palette='Set2')
plt.title('Perbandingan Nilai Sebelum dan Sesudah')
plt.xlabel('Kondisi')
plt.ylabel('Nilai')
plt.grid(True)
plt.show()
