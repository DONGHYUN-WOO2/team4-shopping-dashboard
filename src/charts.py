import streamlit as st


def show_category_sales_chart(category_sales):
    st.bar_chart(
        category_sales,
        x="category",
        y="total_sales"
    )


def show_monthly_sales_chart(monthly_sales):
    st.line_chart(
        monthly_sales,
        x="order_month",
        y="total_sales"
    )