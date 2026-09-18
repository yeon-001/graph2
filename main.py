# ============================================================
# 그래프 8. 10위권에 있는 영화는 개봉 첫 주 관객도 많은?
# ============================================================

st.divider()

st.header("🔵 그래프 8")

# 필요한 열만 사용
scatter_df = df[
    ["영화명", "days_in_top10", "first_week_audi"]
].copy()

# 숫자형으로 변환
scatter_df["days_in_top10"] = pd.to_numeric(
    scatter_df["days_in_top10"],
    errors="coerce"
)

scatter_df["first_week_audi"] = pd.to_numeric(
    scatter_df["first_week_audi"],
    errors="coerce"
)

# 영화별로 중복되는 데이터가 있다면 영화 하나당 한 점만 사용
scatter_df = (
    scatter_df
    .dropna(subset=["영화명", "days_in_top10", "first_week_audi"])
    .drop_duplicates(subset=["영화명"])
)

fig8 = px.scatter(
    scatter_df,
    x="days_in_top10",
    y="first_week_audi",
    hover_name="영화명",
    title="10위권에 있는 영화는 개봉 첫 주 관객도 많은?",
    labels={
        "days_in_top10": "10위권에 머문 날수",
        "first_week_audi": "개봉 첫 주 관객"
    }
)

fig8.update_traces(
    marker=dict(size=10),
    hovertemplate=
    "영화명: %{hovertext}<br>"
    "10위권에 머문 날수: %{x}일<br>"
    "개봉 첫 주 관객: %{y:,.0f}명"
)

fig8.update_layout(
    xaxis_title="10위권에 머문 날수",
    yaxis_title="개봉 첫 주 관객(명)",
    height=600
)

st.plotly_chart(
    fig8,
    use_container_width=True
)

st.subheader("이 그래프로 알 수 있는 것")

st.text_area(
    "내용을 직접 입력하세요.",
    placeholder="이 그래프로 알 수 있는 것을 여기에 작성하세요.",
    height=100,
    key="graph8_explanation"
)
