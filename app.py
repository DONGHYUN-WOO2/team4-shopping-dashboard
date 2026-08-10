from pathlib import Path

import streamlit as st
from pathlib import Path

from src.data_loader import load_all_data
customers, orders, order_items, products = load_all_data()

from src.analysis import (
    load_merged_data,
    calculate_core_metrics,
    calculate_category_sales,
    calculate_monthly_sales
)

from src.charts import (
    show_category_sales_chart,
    show_monthly_sales_chart,
)

DATA_DIR = Path("data/raw")
merged_df = load_merged_data(DATA_DIR)


#Streamlit 기본 화면을 만들고 프로젝트 제목과 설명 표시하기
st.set_page_config(
    page_title="쇼핑몰 데이터 분석 대시보드",
    page_icon="🛒",
    layout="wide",
)

st.title("🛒 쇼핑 데이터 분석 대시보드")
st.write("쇼핑 데이터를 조건별로 조회하고 분석 결과를 확인하는 대시보드입니다.")

#사이드바에 필터 구현
st.sidebar.header("필터")

categories = sorted(merged_df["category"].dropna().unique())
selected_category = st.sidebar.selectbox(
    "카테고리",
    ["전체"] + list(categories)
)

statuses = sorted(merged_df["order_status"].dropna().unique())
selected_status = st.sidebar.selectbox(
    "주문 상태",
    ["전체"] + list(statuses)
)

filtered_df = merged_df.copy()

if selected_category != "전체":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]

if selected_status != "전체":
    filtered_df = filtered_df[
        filtered_df["order_status"] == selected_status
    ]

#데이터가 없을 때 안내 메시지 표시
if filtered_df.empty:
    st.warning("선택한 조건에 해당하는 데이터가 없습니다.")
    st.stop()

#핵심 지표 표시
metrics = calculate_core_metrics(filtered_df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "전체 주문 수",
        f"{metrics['total_orders']:,}"
    )

with col2:
    st.metric(
        "총 주문 수량",
        f"{metrics['total_quantity']:,}"
    )

with col3:
    st.metric(
        "총 주문 금액",
        f"{metrics['total_amount']:,.0f}원"
    )

with col4:
    st.metric(
        "평균 주문 금액",
        f"{metrics['average_order_amount']:,.0f}원"
    )

#차트 구현
category_sales = calculate_category_sales(filtered_df)
monthly_sales = calculate_monthly_sales(filtered_df)

st.subheader("카테고리별 매출")
show_category_sales_chart(category_sales)

st.subheader("월별 주문 금액")
show_monthly_sales_chart(monthly_sales)


#필터 결과를 표로 표시
st.subheader("필터 확인")
st.dataframe(filtered_df)


