import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------------
# 기본 설정
# -----------------------------------
st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    layout="wide"
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")


# -----------------------------------
# 데이터 불러오기
# -----------------------------------
DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"


@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)


df = load_data()


# -----------------------------------
# 데이터 전처리
# -----------------------------------

# 장르가 여러 개일 경우 첫 번째 장르만 사용
df["genre"] = (
    df["genre"]
    .fillna("알 수 없음")
    .astype(str)
    .str.split("|")
    .str[0]
    .str.strip()
)

# 총 관객을 숫자로 변환
df["total_audi"] = pd.to_numeric(
    df["total_audi"],
    errors="coerce"
).fillna(0)


# ===================================
# 그래프 1
# ===================================
st.header("그래프 1. 장르별 영화 편수")

# 장르별 영화 개수 계산
genre_count = df["genre"].value_counts().reset_index()
genre_count.columns = ["장르", "영화 편수"]


# 도넛 차트
fig1 = px.pie(
    genre_count,
    names="장르",
    values="영화 편수",
    hole=0.45,
    title="장르별 영화 편수"
)

fig1.update_traces(
    textinfo="label+percent",
    hovertemplate=(
        "<b>%{label}</b><br>"
        "영화 편수: %{value}편<br>"
        "비율: %{percent}"
        "<extra></extra>"
    )
)

fig1.update_layout(
    margin=dict(t=60, l=20, r=20, b=20)
)

st.plotly_chart(
    fig1,
    use_container_width=True
)


# 그래프 1 설명 공간
st.subheader("이 그래프로 알 수 있는 것")

st.text_area(
    "내용을 입력하세요.",
    placeholder="이 그래프로 알 수 있는 것을 한 문장으로 작성하세요.",
    height=100,
    key="graph1_explanation"
)


# ===================================
# 그래프 2
# ===================================
st.divider()

st.header("그래프 2. 장르별 영화 총 관객 트리맵")


# 장르 → 영화명 순서로 트리맵 구성
fig2 = px.treemap(
    df,
    path=["genre", "movieNm"],
    values="total_audi",
    title="장르별 영화 총 관객"
)


# 마우스를 올렸을 때 영화명과 총 관객 표시
fig2.update_traces(
    hovertemplate=(
        "<b>%{label}</b><br>"
        "총 관객: %{value:,.0f}명"
        "<extra></extra>"
    )
)

fig2.update_layout(
    margin=dict(t=60, l=20, r=20, b=20)
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# 그래프 2 설명 공간
st.subheader("이 그래프로 알 수 있는 것")

st.text_area(
    "내용을 입력하세요.",
    placeholder="이 그래프로 알 수 있는 것을 한 문장으로 작성하세요.",
    height=100,
    key="graph2_explanation"
)


# ===================================
# 그래프 3 자리
# ===================================
st.divider()

st.header("그래프 3")

st.info("세 번째 그래프를 여기에 추가할 수 있습니다.")

st.subheader("이 그래프로 알 수 있는 것")

st.text_area(
    "내용을 입력하세요.",
    placeholder="이 그래프로 알 수 있는 것을 한 문장으로 작성하세요.",
    height=100,
    key="graph3_explanation"
)
