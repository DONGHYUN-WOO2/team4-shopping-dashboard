# AI 코드 검증 03 - 매출 차트 출력

## 1. 검증 기능

분석 함수에서 계산된 카테고리별 매출과 월별 주문 금액이 Streamlit 차트로 정상적으로 출력되는지 확인한다.

## 2. AI 활용 내용

AI에게 분석 결과 DataFrame을 `st.bar_chart()`와 `st.line_chart()`를 사용하여 시각화하는 방법을 질문하고 코드를 참고하였다.

## 3. 검증 코드

```python
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
```

`app.py`에서는 다음과 같이 분석 결과를 전달하였다.

```python
category_sales = calculate_category_sales(filtered_df)
monthly_sales = calculate_monthly_sales(filtered_df)

show_category_sales_chart(category_sales)
show_monthly_sales_chart(monthly_sales)
```

## 4. 예상 결과

* 카테고리별 매출이 막대그래프로 표시되어야 한다.
* 월별 주문 금액이 선그래프로 표시되어야 한다.
* 카테고리 차트의 X축은 category, Y축은 total_sales가 되어야 한다.
* 월별 차트의 X축은 order_month, Y축은 total_sales가 되어야 한다.
* 필터를 변경하면 두 차트도 함께 변경되어야 한다.

## 5. 실제 결과

Streamlit 실행 결과 카테고리별 매출은 막대그래프로, 월별 주문 금액은 선그래프로 정상 출력되었다. 사이드바 필터를 변경했을 때 선택된 조건에 맞게 차트 결과도 변경되는 것을 확인하였다.

## 6. 검증 결과

두 차트 모두 예상한 컬럼을 기준으로 정상적으로 출력되었으며 필터 결과도 반영되었다.

**검증 결과: PASS**
