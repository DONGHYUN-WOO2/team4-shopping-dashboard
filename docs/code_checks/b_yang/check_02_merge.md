# 코드 단위 검증 기록

## 1. 작성자
- 이름: 양성용
- GitHub ID: dydtlsrl
- 담당 기능: 핵심 지표 및 분석

## 2. 검증 단위
- 기능명: 데이터 병합 (orders + order_items + products)
- 관련 Issue: #(이슈번호)
- 관련 파일: notebooks/02_analysis.ipynb

## 3. 코드 목적
order_items를 기준으로 orders, products 정보를 병합하여 
주문별 상품/카테고리 정보를 포함한 통합 데이터를 만든다.

## 4. 입력
- data/raw/orders.csv (customer_id, order_date, payment_method, order_status)
- data/raw/products.csv (product_name, category, price)
- order_items (item_amount 포함, 이전 검증 단위에서 생성)

## 5. AI 활용
- 사용 도구: (사용한 도구명)
- 질문 내용: order_items와 orders를 order_id 기준으로, 그 결과와 products를 
  product_id 기준으로 병합하고, 병합 전후 행 수와 category 결측치를 확인하는 코드 요청
- AI가 제안한 핵심 내용: merge()로 두 단계 병합 수행, len() 비교와 isna().sum()으로 검증 코드 포함

## 6. 실행 전 예상
병합 후 행 수는 order_items 원본 행 수(14603)와 같아야 하고, 
category 컬럼에 결측치가 없어야 한다.

## 7. 실행 코드
```python
orders = pd.read_csv(DATA_DIR / "orders.csv")
products = pd.read_csv(DATA_DIR / "products.csv")

before_rows = len(order_items)
merged = order_items.merge(orders, on="order_id", how="left")
merged = merged.merge(products, on="product_id", how="left")
after_rows = len(merged)

print(f"병합 전 행 수: {before_rows}")
print(f"병합 후 행 수: {after_rows}")
print(f"행 수 일치 여부: {before_rows == after_rows}")

missing_category = merged["category"].isna().sum()
print(f"category 결측치 개수: {missing_category}")

merged.head()
```

## 8. 실제 결과
- 병합 전 행 수: 14603
- 병합 후 행 수: 14603
- 행 수 일치 여부: True
- category 결측치 개수: 0
- merged 테이블에 customer_id, order_date, payment_method, order_status, 
  product_name, category, price 컬럼이 모두 정상적으로 추가된 것을 head()로 확인했다.

## 9. 검증 방법
- 정상 조건: before_rows == after_rows 비교 → True로 일치 확인
- 예외 조건: category 컬럼 결측치 개수 확인 → 0으로 확인, 즉 product_id 매칭이 
  누락된 행이 없음을 검증했다.
- 확인 방법: len() 비교, isna().sum() 함수 사용

## 10. AI 코드에서 수정한 부분
AI가 제안한 코드를 수정 없이 그대로 사용했다. 
다만 실제 실행 전 orders.csv와 products.csv의 실제 컬럼명(customer_id, order_date, 
payment_method, order_status, product_name, category, price)이 
AI에게 전달한 정보와 일치하는지 직접 확인한 후 적용했다.

## 11. 결과 해석
주문 상세 데이터(order_items)에 주문 정보(orders)와 상품 카테고리 정보(products)가 
모두 결합되어, 이후 카테고리별 매출 집계, 월별 매출 추이, 주문 상태별 건수 분석 등 
핵심 지표 계산의 기초 데이터가 완성되었다. 
병합 과정에서 행 수 증감이나 결측치가 발생하지 않아 데이터 정합성이 확인되었다.

## 12. 아직 이해되지 않는 부분
merge()의 how="left" 옵션 외에 "inner", "outer" 등 다른 방식을 썼을 때 
결과가 어떻게 달라지는지는 아직 명확히 이해하지 못했다.