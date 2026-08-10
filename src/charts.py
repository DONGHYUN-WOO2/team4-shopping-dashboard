import streamlit as st


def show_category_sales_chart(category_sales):
    st.bar_chart(
        category_sales,
        x="category",
<<<<<<< HEAD
        y="total_sales",
=======
        y="total_sales"
>>>>>>> b3b7c3310d0822a9bc09cd825c66a752ba51c617
    )


def show_monthly_sales_chart(monthly_sales):
    st.line_chart(
        monthly_sales,
        x="order_month",
<<<<<<< HEAD
        y="total_sales",
=======
        y="total_sales"
>>>>>>> b3b7c3310d0822a9bc09cd825c66a752ba51c617
    )