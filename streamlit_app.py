import streamlit as st
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

st.title("Uji T Dua Sampel Berpasangan dengan Multi-Visualisasi")

uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file:
    try:
        data = pd.read_excel(uploaded_file)
        st.write("Data yang diunggah:")
        st.write(data)

        if 'Sebelum' in data.columns and 'Sesudah' in data.columns:

            # Hitung paired t-test
            before = data['Sebelum']
            after = data['Sesudah']
            t_stat, p_value = stats.ttest_rel(before, after)

            st.subheader("Hasil Uji T Dua Sampel Berpasangan")
            st.write(f"Nilai t-statistik: {t_stat}")
            st.write(f"Nilai p-value: {p_value}")

            alpha = 0.05
            if p_value < alpha:
                st.write("Kesimpulan: Ada perbedaan signifikan sebelum dan sesudah (tolak H0).")
            else:
                st.write("Kesimpulan: Tidak ada perbedaan signifikan sebelum dan sesudah (gagal tolak H0).")

            # Pilih jenis visualisasi
            st.subheader("Visualisasi Data")
            chart_type = st.selectbox("Pilih jenis visualisasi:", ["Boxplot", "Histogram", "Barplot", "Lineplot"])

            fig, ax = plt.subplots()

            if chart_type == "Boxplot":
                data.boxplot(column=["Sebelum", "Sesudah"], ax=ax)
                ax.set_title("Boxplot Sebelum vs Sesudah")

            elif chart_type == "Histogram":
                ax.hist(before, bins=10, alpha=0.5, label="Sebelum")
                ax.hist(after, bins=10, alpha=0.5, label="Sesudah")
                ax.set_title("Histogram Sebelum dan Sesudah")
                ax.legend()

            elif chart_type == "Barplot":
                means = [before.mean(), after.mean()]
                ax.bar(["Sebelum", "Sesudah"], means, color=["skyblue", "salmon"])
                ax.set_title("Rata-rata Sebelum dan Sesudah")

            elif chart_type == "Lineplot":
                ax.plot(before, label="Sebelum", marker='o')
                ax.plot(after, label="Sesudah", marker='x')
                ax.set_title("Perubahan per Subjek")
                ax.legend()

            st.pyplot(fig)

        else:
            st.error("File Excel harus memiliki kolom 'Sebelum' dan 'Sesudah'.")

    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
