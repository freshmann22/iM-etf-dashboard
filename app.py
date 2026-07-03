"""ETF 서비스 정적 프로토타입을 Streamlit Cloud에 배포하기 위한 래퍼.

실제 로직은 전부 index.html(HTML/CSS/JS)에 있으며, 이 파일은 해당 정적 파일을
그대로 읽어 화면에 렌더링만 한다. 더미데이터/인터랙션 수정은 index.html에서 한다.
"""

import os

import streamlit as st
import streamlit.components.v1 as components

INDEX_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

st.set_page_config(page_title="ETF 서비스", page_icon="📊", layout="centered")

with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=900, scrolling=True)
