```python
import streamlit as st
import pandas as pd
import plotly.express as px


# --------------------------------------------------
# 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="영화 데이터 그래프 도감 2 - 분포와 관계",
    layout="wide"
)

st.title("영화 데이터 그래프 도감 2 - 분포와 관계")


# --------------------------------------------------
# 데이터 불러오기
# --------------------------------------------------
DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 장르: 세로막대(|)로 여러 장르가 있는 경우 첫 번째 장르만 사용
    df["genre"] = (
        df["genre"]
        .fillna("알 수 없음")
        .astype(str)
        .str.split("|")
        .str[0]
        .str.strip()
    )

    return df


df = load_data()


# --------------------------------------------------
# 그래프 1. 장르별 영화 편수
# --------------------------------------------------
st.header("그래프 1. 장르별 영화 편수")

genre_count = (
    df["genre"]
    .value_counts()
    .reset_index()
)

genre_count.columns = ["장르", "영화 편수"]

fig = px.pie(
    genre_count,
    names="장르",
    values="영화 편수",
    hole=0.45,
    title="장르별 영화 편수"
)

fig.update_traces(
    textinfo="label+percent",
    hovertemplate=(
        "<b>%{label}</b><br>"
        "영화 편수: %{value}편<br>"
        "비율: %{percent}"
        "<extra></extra>"
    )
)

fig.update_layout(
    legend_title="장르",
    margin=dict(t=60, l=20, r=20, b=20)
)

st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------
# 그래프에서 알 수 있는 것
# --------------------------------------------------
st.subheader("이 그래프로 알 수 있는 것")

st.text_area(
    "내용을 입력하세요.",
    placeholder="이 그래프로 알 수 있는 것을 한 문장으로 작성하세요.",
    height=100,
    key="graph1_explanation"
)


# --------------------------------------------------
# 다음 그래프를 위한 구역
# --------------------------------------------------
st.divider()

st.header("그래프 2")
st.info("다음 그래프를 이 구역에 추가할 수 있습니다.")

st.subheader("이 그래프로 알 수 있는 것")

st.text_area(
    "내용을 입력하세요.",
    placeholder="이 그래프로 알 수 있는 것을 한 문장으로 작성하세요.",
    height=100,
    key="graph2_explanation"
)


st.divider()

st.header("그래프 3")
st.info("다음 그래프를 이 구역에 추가할 수 있습니다.")

st.subheader("이 그래프로 알 수 있는 것")

st.text_area(
    "내용을 입력하세요.",
    placeholder="이 그래프로 알 수 있는 것을 한 문장으로 작성하세요.",
    height=100,
    key="graph3_explanation"
)
```
