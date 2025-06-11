import streamlit as st
import pandas as pd
from scipy import stats

st.title("Uji T Dua Sampel Berpasangan")

uploaded_file = st.file_uploader("Upload file Excel", type=['xlsx'])

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    st.write("Data yang diupload:")
    st.write(data.head())

    try:
        before = data['Sebelum']
        after = data['Sesudah']

        t_stat, p_value = stats.ttest_rel(before, after)

        st.subheader("Hasil Uji T")
        st.write(f"Nilai t-statistik: {t_stat}")
        st.write(f"Nilai p-value: {p_value}")

        alpha = 0.05
        if p_value < alpha:
            st.success("Ada perbedaan signifikan sebelum dan sesudah (tolak H0).")
        else:
            st.info("Tidak ada perbedaan signifikan (gagal tolak H0).")

    except KeyError:
        st.error("Pastikan kolom 'Sebelum' dan 'Sesudah' ada di file Excel.")
