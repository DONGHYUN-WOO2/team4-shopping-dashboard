# AI 코드 검증 01 - 카테고리 필터

## 1. 검증 기능

Streamlit 사이드바에서 사용자가 선택한 카테고리에 따라 데이터가 정상적으로 필터링되는지 확인한다.

## 2. AI 활용 내용

AI에게 `st.sidebar.selectbox()`를 이용하여 전체 카테고리 또는 특정 카테고리를 선택할 수 있는 필터 구현 방법을 질문하고 코드를 참고하였다.

## 3. 검증 코드

```python
categories = sorted(merged_df["category"].dropna().unique())

selected_category = st.sidebar.selectbox(
    "카테고리",
    ["전체"] + list(categories)
)

filtered_df = merged_df.copy()

if selected_category != "전체":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]
```

## 4. 예상 결과

* "전체"를 선택하면 전체 데이터가 표시되어야 한다.
* 특정 카테고리를 선택하면 해당 카테고리의 데이터만 남아야 한다.
* 필터 변경에 따라 이후 지표와 차트에 사용되는 데이터도 변경되어야 한다.

## 5. 실제 결과

Streamlit을 실행하여 "전체"와 개별 카테고리를 각각 선택해 확인하였다. "전체" 선택 시 전체 데이터가 표시되었으며, 특정 카테고리 선택 시 해당 카테고리의 데이터만 필터링되는 것을 확인하였다.

## 6. 검증 결과

예상 결과와 실제 결과가 일치하였다. 카테고리 필터가 정상적으로 동작함을 확인하였다.

**검증 결과: PASS**
