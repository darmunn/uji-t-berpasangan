import pandas as pd
from scipy import stats

file_path = 'data_uji.xlsx'  
data = pd.read_excel(file_path)

before = data['Sebelum']
after = data['Sesudah']

t_stat, p_value = stats.ttest_rel(before, after)

print("Hasil Uji T Dua Sampel Berpasangan")
print("-----------------------------------")
print(f"Nilai t-statistik: {t_stat}")
print(f"Nilai p-value: {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Kesimpulan: Ada perbedaan signifikan sebelum dan sesudah (tolak H0).")
else:
    print("Kesimpulan: Tidak ada perbedaan signifikan (gagal tolak H0).")
