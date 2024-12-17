import streamlit as st

# 標題
st.title("我的第一個 Streamlit 應用程式")

# 副標題
st.header("歡迎使用 Streamlit")

# 輸入文字
name = st.text_input("請輸入你的名字", "訪客")

# 按鈕
if st.button("按我"):
    st.success(f"你好，{name}！歡迎來到 Streamlit！")

# 數字輸入及計算
number = st.slider("請選擇一個數字", 1, 100, 50)
st.write(f"你選擇的數字是：{number}")
st.write(f"數字的平方是：{number**2}")
