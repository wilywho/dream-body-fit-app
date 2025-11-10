import streamlit as st

# ===============================
# Fungsi utama
# ===============================
def latihan_dan_menu(fatPercentageNow, genderIn):
    # Output berupa dictionary agar bisa ditampilkan di Streamlit
    hasil = {}

    if genderIn == "Pria":
        if 6 <= fatPercentageNow <= 13:
            hasil["kategori"] = "🏋️ Atletis"
            hasil["pesan"] = "Pertahankan pola latihan dan pola makan anda saat ini."
            hasil["latihan"] = [
                "Strength Training (Upper & Lower Body Split, 4–5x/minggu)",
                "HIIT Cardio (2x/minggu)",
                "Mobility & Stretching setiap hari"
            ]
            hasil["menu"] = [
                "Sarapan: Oatmeal + telur rebus + pisang",
                "Makan Siang: Nasi merah + dada ayam + sayur hijau",
                "Makan Malam: Ikan panggang + brokoli + kentang rebus"
            ]
            hasil["kalori_intake"] = 2800
            hasil["kalori_outtake"] = 2500

        elif 14 <= fatPercentageNow <= 17:
            hasil["kategori"] = "💪 Bugar"
            hasil["pesan"] = "Pertahankan pola latihan dan makan sehat untuk menjaga performa."
            hasil["latihan"] = [
                "Strength Training 3–4x/minggu",
                "Cardio 3x/minggu (lari, sepeda, atau berenang)",
                "Core Training 2x/minggu"
            ]
            hasil["menu"] = [
                "Sarapan: Telur orak-arik + roti gandum + alpukat",
                "Makan Siang: Nasi merah + ayam bakar + sayur tumis",
                "Makan Malam: Tahu + tempe + sayur bening + buah"
            ]
            hasil["kalori_intake"] = 2500
            hasil["kalori_outtake"] = 2200

        elif 18 <= fatPercentageNow <= 24:
            hasil["kategori"] = "⚖️ Rata-rata/Wajar"
            hasil["pesan"] = "Masih bisa ditingkatkan dengan pola latihan dan makan seimbang!"
            hasil["latihan"] = [
                "Full Body Workout (3–4x/minggu)",
                "Cardio ringan–sedang (30–45 menit, 4x/minggu)",
                "Yoga atau stretching 2x/minggu"
            ]
            hasil["menu"] = [
                "Sarapan: Smoothie buah + oats + yogurt rendah lemak",
                "Makan Siang: Nasi merah + dada ayam + sayuran kukus",
                "Makan Malam: Sup sayur + tahu tempe + buah potong"
            ]
            hasil["kalori_intake"] = 2200
            hasil["kalori_outtake"] = 2500

        elif fatPercentageNow >= 25:
            hasil["kategori"] = "🚨 OBESITAS"
            hasil["pesan"] = "Segera perbaiki gaya hidup Anda!"
            hasil["latihan"] = [
                "Jalan cepat atau bersepeda 5x/minggu (45–60 menit)",
                "Latihan ringan (bodyweight: squat, push-up, plank 3x/minggu)",
                "Kurangi duduk terlalu lama, aktif bergerak setiap jam"
            ]
            hasil["menu"] = [
                "Sarapan: Telur rebus + buah + air putih",
                "Makan Siang: Nasi merah + ayam kukus + sayur rebus",
                "Makan Malam: Sup bening + tahu tempe + sayuran"
            ]
            hasil["kalori_intake"] = 1800
            hasil["kalori_outtake"] = 2600

    elif genderIn == "Wanita":
        if 14 <= fatPercentageNow <= 20:
            hasil["kategori"] = "🏋️ Atletis"
            hasil["pesan"] = "Pertahankan pola latihan dan pola makan anda saat ini."
            hasil["latihan"] = [
                "Strength Training (Upper & Lower Body Split, 4–5x/minggu)",
                "HIIT Cardio (2x/minggu)",
                "Mobility & Stretching setiap hari"
            ]
            hasil["menu"] = [
                "Sarapan: Oatmeal + telur rebus + pisang",
                "Makan Siang: Nasi merah + dada ayam + sayur hijau",
                "Makan Malam: Ikan panggang + brokoli + kentang rebus"
            ]
            hasil["kalori_intake"] = 2000
            hasil["kalori_outtake"] = 1800

        elif 21 <= fatPercentageNow <= 24:
            hasil["kategori"] = "💪 Bugar"
            hasil["pesan"] = "Pertahankan pola latihan dan makan sehat untuk menjaga performa."
            hasil["latihan"] = [
                "Strength Training 3–4x/minggu",
                "Cardio 3x/minggu (lari, sepeda, atau berenang)",
                "Core Training 2x/minggu"
            ]
            hasil["menu"] = [
                "Sarapan: Telur orak-arik + roti gandum + alpukat",
                "Makan Siang: Nasi merah + ayam bakar + sayur tumis",
                "Makan Malam: Tahu + tempe + sayur bening + buah"
            ]
            hasil["kalori_intake"] = 1800
            hasil["kalori_outtake"] = 2000

        elif 25 <= fatPercentageNow <= 31:
            hasil["kategori"] = "⚖️ Rata-rata/Wajar"
            hasil["pesan"] = "Masih bisa ditingkatkan dengan pola latihan dan makan seimbang!"
            hasil["latihan"] = [
                "Full Body Workout (3–4x/minggu)",
                "Cardio ringan–sedang (30–45 menit, 4x/minggu)",
                "Yoga atau stretching 2x/minggu"
            ]
            hasil["menu"] = [
                "Sarapan: Smoothie buah + oats + yogurt rendah lemak",
                "Makan Siang: Nasi merah + dada ayam + sayuran kukus",
                "Makan Malam: Sup sayur + tahu tempe + buah potong"
            ]
            hasil["kalori_intake"] = 1600
            hasil["kalori_outtake"] = 1900

        elif fatPercentageNow >= 32:
            hasil["kategori"] = "🚨 OBESITAS"
            hasil["pesan"] = "Segera perbaiki gaya hidup Anda!"
            hasil["latihan"] = [
                "Jalan cepat atau bersepeda 5x/minggu (45–60 menit)",
                "Latihan ringan (bodyweight: squat, push-up, plank 3x/minggu)",
                "Kurangi duduk terlalu lama, aktif bergerak setiap jam"
            ]
            hasil["menu"] = [
                "Sarapan: Telur rebus + buah + air putih",
                "Makan Siang: Nasi merah + ayam kukus + sayur rebus",
                "Makan Malam: Sup bening + tahu tempe + sayuran"
            ]
            hasil["kalori_intake"] = 1400
            hasil["kalori_outtake"] = 2000

    else:
        hasil["error"] = "Input gender tidak valid. Pilih Pria/Wanita."

    return hasil


# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="Dream Body Fit", page_icon="💪", layout="centered")

st.title("🏋️ Dream Body Fit App")
st.write("Selamat datang di **Aplikasi Fitness Pemula**! 🚀")
st.write("Masukkan datamu di bawah ini untuk mendapatkan rekomendasi latihan dan pola makan pribadi.")

# Form Input
with st.form("fitness_form"):
    st.subheader("🧍 Profil Anda")
    nameIn = st.text_input("Nama Lengkap:")
    genderIn = st.selectbox("Jenis Kelamin:", ["Pria", "Wanita"])
    ageIn = st.number_input("Usia (tahun):", min_value=10, max_value=100, value=25)
    heightIn = st.number_input("Tinggi Badan (cm):", min_value=100, max_value=250, value=170)
    weightIn = st.number_input("Berat Badan (kg):", min_value=30, max_value=200, value=65.0)
    fatPercentageNow = st.number_input("Fat Percentage Sekarang (%):", min_value=1.0, max_value=60.0, value=20.0)
    targetFatPercentage = st.number_input("Target Fat Percentage Impian (%):", min_value=1.0, max_value=60.0, value=15.0)

    # 👇 tombol submit HARUS berada di dalam blok with st.form()
    submit = st.form_submit_button("Lihat Rekomendasi 💪")

if submit:
    hasil = latihan_dan_menu(fatPercentageNow, genderIn)

    if "error" in hasil:
        st.error(hasil["error"])
    else:
        st.subheader(f"📊 Hasil Analisis untuk {nameIn}")
        st.markdown(f"**Kategori:** {hasil['kategori']}")
        st.markdown(f"**Pesan:** {hasil['pesan']}")
        
        st.markdown("### 🏋️ Pola Latihan Rekomendasi:")
        for l in hasil["latihan"]:
            st.write(f"- {l}")

        st.markdown("### 🍽️ Menu Harian Contoh:")
        for m in hasil["menu"]:
            st.write(f"- {m}")

        defisit = hasil["kalori_outtake"] - hasil["kalori_intake"]
        st.markdown("### 🔥 Estimasi Kalori Harian:")
        st.write(f"Intake (masuk): {hasil['kalori_intake']} kkal")
        st.write(f"Outtake (keluar): {hasil['kalori_outtake']} kkal")
        st.write(f"Defisit kalori: **{defisit} kkal**")

