# 코드 단위 검증 기록

## 1. 작성자
- 이름: 양성용
- GitHub ID: dydtlsrl
- 담당 기능: 핵심 지표 및 분석

## 2. 검증 단위
- 기능명: 핵심 지표 계산 (전체 주문 수, 총 주문 금액, 평균 주문 금액, 주문 상태별 건수)
- 관련 Issue: #(이슈번호)
- 관련 파일: notebooks/02_analysis.ipynb

## 3. 코드 목적
쇼핑몰 현황을 요약할 수 있는 핵심 지표를 계산하고, Streamlit에서 재사용 가능한
함수 형태로 제공한다.

## 4. 입력
merged (order_items + orders + products 병합 데이터, item_amount 포함)

## 5. AI 활용
- 사용 도구: (사용한 도구명)
- 질문 내용: 전체 주문 수, 총 주문 수량, 총 주문 금액, 평균 주문 금액,
  주문 상태별 건수를 계산하는 코드 요청
- AI가 제안한 핵심 내용: nunique(), sum(), groupby(), value_counts() 활용

## 6. 실행 전 예상
전체 주문 수는 order_id 고유값 개수와 같아야 하고, 총 주문 금액은 item_amount
합계와 같아야 하며, 평균 주문 금액은 총액/주문수와 일치해야 한다.

## 7. 실행 코드
​```python
def calculate_core_metrics(merged_df):
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
        "status_counts": status_counts
    }
​```

## 8. 실제 결과
(본인 화면에 나온 실제 숫자로 채우기: 예 - 전체 주문 수: 6000, 총 주문 금액: ...원)

## 9. 검증 방법
- 정상 조건: total_amount == merged["item_amount"].sum() → assert 통과
- 예외 조건: 수동 계산한 평균값과 함수 결과값 비교 → 일치 확인
- 확인 방법: assert 구문, print 비교

## 10. AI 코드에서 수정한 부분
AI가 제안한 개별 계산 코드를 calculate_core_metrics() 함수로 묶어
재사용 가능하도록 구조화했다. 이는 Streamlit 앱에서 반복 호출이 필요하기 때문이다.

## 11. 결과 해석
전체 주문 현황(건수, 금액, 평균)과 주문 상태 분포를 한눈에 파악할 수 있게 되었다.
이 지표들은 Streamlit 대시보드의 st.metric()에 바로 활용될 예정이다.

## 12. 아직 이해되지 않는 부분
없음