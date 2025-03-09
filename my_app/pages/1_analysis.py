import streamlit as st
import pandas as pd

st.title('통계 분석 페이지')

uploaded_file = st.file_uploader('CSV 파일 업로드', type=['csv'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write('기본 통계 분석 결과:')
        st.write(df.describe())
    except Exception as e:
        st.error(f'오류 발생: {e}')
else:
    st.info('CSV 파일을 선택해 주세요.')
