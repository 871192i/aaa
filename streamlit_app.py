import streamlit as st

@st.cache_resource(show_spinner=False)
def load_model():
    # โค้ดโหลดโมเดลหรือทรัพยากร
    return "โมเดลโหลดสำเร็จ"

# ฟังก์ชันสำหรับล้างแคช
def clear_cache():
    st.cache_data.clear()  # ล้างแคชที่มาจาก @st.cache_data
    st.cache_resource.clear()  # ล้างแคชที่มาจาก @st.cache_resource

if st.button("Clear Cache"):
    clear_cache()
    st.success("Cache cleared!")

st.title("🎈 My jekkiss a sdfasdfas app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
