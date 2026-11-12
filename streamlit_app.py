import streamlit as st

st.set_page_config(page_title="Transportation of Holy Quran", page_icon="📖")

st.title("📖 Transportation of Holy Quran")
st.write("Quran Pak ki free home delivery - Lahore")

st.header("1. Apna Order Likhen")

name = st.text_input("Apna Naam")
phone = st.text_input("Mobile Number")
address = st.text_area("Poora Address - Lahore")

quran_type = st.selectbox("Quran Pak Kis Tarah Ka Chahiye?",
    ["Simple Quran Pak", "Quran Pak with Urdu Tarjuma", "Quran Pak with Tajweed (Colored)", "Hafizi Quran - 15 Lines", "Quran Pak - Big Size (Buzurgon ke liye)"])

quantity = st.number_input("Kitne Quran Pak Chahiye?", min_value=1, max_value=20, value=1)

delivery = st.radio("Delivery Kab Chahiye?", ["Aaj hi - Urgent", "Kal", "2-3 Din Mein"])

if st.button("Order Confirm Karen ✅"):
    if name and phone and address:
        st.success(f"Shukriya {name}! Aapka order mil gaya.")
        st.write(f"**Quran:** {quran_type}")
        st.write(f"**Quantity:** {quantity}")
        st.write(f"**Delivery:** {delivery}")
        st.write(f"**Address:** {address}")
        st.info("Hum aapko jald call kar ke confirm karenge. JazakAllah!")
    else:
        st.error("Please Naam, Mobile aur Address poora likhen.")

st.markdown("---")
st.write("📞 Contact: 0300-XXXXXXX | Lahore, Pakistan")
st.write("Free Delivery - Lahore ke andar")
