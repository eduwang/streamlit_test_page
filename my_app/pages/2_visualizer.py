import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('데이터 시각화 페이지')

uploaded_file = st.file_uploader('CSV 파일을 업로드하세요.', type=['csv'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write('업로드된 데이터:')
        st.dataframe(df)
        
        st.write('데이터 시각화 (첫 번째 열 기준):')
        if len(df.columns) > 1:
            fig, ax = plt.subplots()
            df[df.columns[1]].value_counts().plot(kind='bar', ax=ax)
            st.pyplot(fig)
        else:
            st.warning('시각화를 위한 충분한 데이터가 없습니다.')
    except Exception as e:
        st.error(f'오류 발생: {e}')
else:
    st.info('CSV 파일을 선택해 주세요.')
