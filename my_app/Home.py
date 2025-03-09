import streamlit as st
import pandas as pd

st.set_page_config(page_title='CSV 파일 뷰어', layout='centered')

st.title('CSV 파일 업로드 및 데이터 테이블 보기')

uploaded_file = st.file_uploader('CSV 파일을 업로드하세요.', type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        st.success('파일이 성공적으로 업로드되었습니다!')
        st.write('데이터 미리보기:')
        st.dataframe(df)
    except Exception as e:
        st.error(f'오류 발생: {e}')
else:
    st.info('CSV 또는 Excel 파일을 선택해 주세요.')
