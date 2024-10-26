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

import streamlit as st
from datetime import datetime

def calculate_age(day, month, year, use_buddhist_year):
    if use_buddhist_year:  # ถ้าเป็น พ.ศ. แปลงเป็น ค.ศ.
        year -= 543

    birth_date = datetime(year, month, day)
    today = datetime.today()

    # คำนวณปี เดือน วัน
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += (birth_date.replace(month=birth_date.month + 1, day=1) - birth_date).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# ส่วน UI
st.title("Age Calculator (คำนวณอายุ)")

# Input UI
day = st.number_input("วัน", min_value=1, max_value=31, value=1)
month = st.number_input("เดือน", min_value=1, max_value=12, value=1)
year = st.number_input("ปี", min_value=1900, max_value=datetime.now().year + 543, value=2518)

# ใช้ radio button แทน checkbox
era = st.radio("เลือกประเภทปี:", ["พ.ศ.", "ค.ศ."])
use_buddhist_year = (era == "พ.ศ.")

# ปุ่มคำนวณ
if st.button("คำนวณอายุ"):
    try:
        years, months, days = calculate_age(day, month, year, use_buddhist_year)
        st.success(f"อายุของคุณ: {years} ปี {months} เดือน {days} วัน")
    except ValueError:
        st.error("วันที่ไม่ถูกต้อง! กรุณาตรวจสอบข้อมูลอีกครั้ง")


