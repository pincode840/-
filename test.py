import streamlit as st
import pandas as pd


# 데이터 로딩
df = pd.read_excel('데이터.xlsx')
a = df.columns
df = df.astype(str)

# 사이드바에서 데이터 업로드
st.sidebar.title("데이터 업로드")
uploaded_file = st.sidebar.file_uploader("업로드할 엑셀 파일 선택", type=["xlsx"])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df = df.fillna('없음')
    st.success('데이터를 업로드하였습니다.')

# 저장 버튼
if st.sidebar.button("저장하기"):
    # 엑셀 파일로 데이터프레임 저장
    df.to_excel('데이터.xlsx', index=False)
    st.success('데이터를 데이터.xlsx 파일로 저장했습니다.')


col1, col2 = st.columns([3, 1])

with col1:
    # 오른쪽의 검색 영역
    st.title("검색 앱")
    # 카테고리 선택
    search_category = st.selectbox("검색 카테고리 선택:", a)

    # 번호 입력
    num = st.text_input(f"{search_category}를 입력하세요:")


    def perform_search(data, num, category):
        return data[data[category].str.contains(num, case=False, na=False)]

    # 찾기
    if num:
        data = perform_search(df, num, search_category)
        if not data.empty:
            st.write("검색 결과:")
            st.write(data)
        else:
            st.write("일치하는 데이터가 없습니다.")

    
with col2:
    # 왼쪽의 메모장 영역
    st.title("메모장")
    user_input = st.text_area("메모를 입력하세요:", height=300)