import streamlit as st
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Uji T Dua Sampel Berpasangan (Paired T-Test)")
st.write("Upload file Excel berisi dua kolom: 'Sebelum' dan 'Sesudah'")

# Upload file
uploaded_file = st.file_uploader("Pilih file Excel (.xlsx)", type="xlsx")

if uploaded_file is not None:
    try:
        data = pd.read_excel(uploaded_file)

        if 'Sebelum' in data.columns and 'Sesudah' in data.columns:
            before = data['Sebelum']
            after = data['Sesudah']

            # Tampilkan data
            st.subheader("Data yang Diunggah:")
            st.dataframe(data)

            # Uji T
            t_stat, p_value = stats.ttest_rel(before, after)

            st.subheader("Hasil Uji T")
            st.write(f"t-statistik: {t_stat:.4f}")
            st.write(f"p-value: {p_value:.4f}")

            alpha = 0.05
            if p_value < alpha:
                st.success("Ada perbedaan signifikan sebelum dan sesudah (tolak H0).")
            else:
                st.warning("Tidak ada perbedaan signifikan (gagal tolak H0).")

            # Visualisasi
            st.subheader("Visualisasi Data")
            fig, ax = plt.subplots()
            sns.boxplot(data=[before, after])
            ax.set_xticklabels(['Sebelum', 'Sesudah'])
            ax.set_title("Boxplot Data Sebelum & Sesudah")
            st.pyplot(fig)

        else:
            st.error("Kolom 'Sebelum' dan 'Sesudah' tidak ditemukan di file Excel.")

    except Exception as e:
        st.error(f"Terjadi error saat membaca file: {e}")
