from pathlib import Path

import streamlit as st

from src.analysis import (
    load_merged_data,
    calculate_core_metrics,
    calculate_category_sales,
    calculate_monthly_sales,
)

from src.charts import (
    show_category_sales_chart,
    show_monthly_sales_chart,
)

DATA_DIR = Path("data/raw")

st.set_page_config(
    page_title="쇼핑몰 데이터 분석 대시보드",
    page_icon="🛒",
    layout="wide",
)

st.title("🛒 쇼핑몰 데이터 분석 대시보드")
st.write("주문 및 상품 데이터를 분석한 결과를 확인할 수 있습니다.")

merged_df = load_merged_data(DATA_DIR)

st.subheader("데이터 확인")
st.write(merged_df.head())
st.write("데이터 크기:", merged_df.shape)

metrics = calculate_core_metrics(merged_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "총 주문 수",
    f"{metrics['total_orders']:,}건"
)

col2.metric(
    "총 주문 수량",
    f"{metrics['total_quantity']:,}개"
)

col3.metric(
    "총 주문 금액",
    f"{metrics['total_amount']:,.0f}원"
)

col4.metric(
    "평균 주문 금액",
    f"{metrics['average_order_amount']:,.0f}원"
)

category_sales = calculate_category_sales(filtered_df)
monthly_sales = calculate_monthly_sales(filtered_df)

st.subheader("카테고리별 매출")
show_category_sales_chart(category_sales)

st.subheader("월별 주문 금액")
show_monthly_sales_chart(monthly_sales)

st.subheader("필터 적용 데이터")

st.dataframe(
    filtered_df,
    use_container_width=True,
)

category_options = sorted(
    merged_df["category"].dropna().unique()
)

selected_categories = st.sidebar.multiselect(
    "카테고리 선택",
    options=category_options,
    default=category_options,
)

status_options = sorted(
    merged_df["order_status"].dropna().unique()
)

selected_statuses = st.sidebar.multiselect(
    "주문 상태 선택",
    options=status_options,
    default=status_options,
)

filtered_df = merged_df[
    merged_df["category"].isin(selected_categories)
    & merged_df["order_status"].isin(selected_statuses)
]

if filtered_df.empty:
    st.warning("선택한 조건에 해당하는 데이터가 없습니다.")
    st.stop()

metrics = calculate_core_metrics(filtered_df)
