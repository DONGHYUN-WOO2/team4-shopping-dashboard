"""
분석 담당(B) - 핵심 지표 및 매출 분석 함수 모음
Streamlit 앱(app.py)에서 이 함수들을 import해서 재사용한다.
"""

import pandas as pd
from pathlib import Path
from src.data_loader import load_all_data


def load_merged_data(data_dir: Path = None) -> pd.DataFrame:
    """
    A(data_loader)의 load_all_data()를 재사용해 4개 데이터를 불러오고,
    item_amount 계산 후 order_items + orders + products + customers를 병합한다.
    """
    customers, orders, order_items, products = load_all_data(data_dir)

    order_items["item_amount"] = order_items["quantity"] * order_items["unit_price"]

    merged = order_items.merge(orders, on="order_id", how="left")
    merged = merged.merge(products, on="product_id", how="left")
    merged = merged.merge(customers, on="customer_id", how="left")

    return merged


def calculate_core_metrics(merged_df: pd.DataFrame) -> dict:
    """
    병합된 데이터프레임에서 핵심 지표를 계산해 딕셔너리로 반환한다.
    (전체 주문 수, 총 주문 수량, 총 주문 금액, 평균 주문 금액, 주문 상태별 건수)
    """
    total_orders = merged_df["order_id"].nunique()
    total_quantity = merged_df["quantity"].sum()
    total_amount = merged_df["item_amount"].sum()
    order_amount = merged_df.groupby("order_id")["item_amount"].sum()
    average_order_amount = order_amount.mean()
    status_counts = merged_df.drop_duplicates("order_id")["order_status"].value_counts()

    return {
        "total_orders": total_orders,
        "total_quantity": total_quantity,
        "total_amount": total_amount,
        "average_order_amount": average_order_amount,
        "status_counts": status_counts,
    }


def calculate_category_sales(merged_df: pd.DataFrame) -> pd.DataFrame:
    """카테고리별 매출 합계를 계산해 내림차순으로 반환한다."""
    result = (
        merged_df.groupby("category", as_index=False)["item_amount"]
        .sum()
        .sort_values("item_amount", ascending=False)
    )
    result.columns = ["category", "total_sales"]
    return result


def calculate_monthly_sales(merged_df: pd.DataFrame) -> pd.DataFrame:
    """월별 주문 금액 합계를 계산해 시간순으로 반환한다."""
    df = merged_df.copy()
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)
    result = (
        df.groupby("order_month", as_index=False)["item_amount"]
        .sum()
        .sort_values("order_month")
    )
    result.columns = ["order_month", "total_sales"]
    return result