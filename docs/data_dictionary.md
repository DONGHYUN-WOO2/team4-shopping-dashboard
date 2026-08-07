# 데이터 딕셔너리

## customers.csv (고객, 1200행)

| 컬럼명 | 타입 | 설명 |
|---|---|---|
| customer_id | int64 | 고객 고유 식별자 (PK) |
| name | str | 고객명 |
| gender | str | 성별 |
| age | int64 | 나이 |
| city | str | 거주 도시 |
| signup_date | str → datetime | 가입일 |

## products.csv (상품, 300행)

| 컬럼명 | 타입 | 설명 |
|---|---|---|
| product_id | int64 | 상품 고유 식별자 (PK) |
| product_name | str | 상품명 |
| category | str | 카테고리 (전자기기, 생활가전, 패션, 뷰티, 식품, 도서, 스포츠, 반려동물, 문구, 홈인테리어) |
| price | int64 | 상품 정가 |

## orders.csv (주문, 6000행)

| 컬럼명 | 타입 | 설명 |
|---|---|---|
| order_id | int64 | 주문 고유 식별자 (PK) |
| customer_id | int64 | 주문한 고객 (FK → customers.customer_id) |
| order_date | str → datetime | 주문일 |
| payment_method | str | 결제수단 (간편결제, 신용카드, 계좌이체, 휴대폰결제, 무통장입금) |
| order_status | str | 주문 상태 (배송중, 배송완료, 결제완료, 배송준비, 취소, 환불) |

## order_items.csv (주문 상세, 약 14,600행)

| 컬럼명 | 타입 | 설명 |
|---|---|---|
| order_item_id | int64 | 주문 상세 고유 식별자 (PK) |
| order_id | int64 | 소속 주문 (FK → orders.order_id) |
| product_id | int64 | 주문된 상품 (FK → products.product_id) |
| quantity | int64 | 주문 수량 |
| unit_price | int64 | 주문 당시 단가 |

## 테이블 관계

```
customers (1) ── (N) orders (1) ── (N) order_items (N) ── (1) products
```

- 고객 1명은 여러 주문을 가질 수 있음 (1:N)
- 주문 1건은 여러 품목(order_items)을 가질 수 있음 (1:N)
- 상품 1개는 여러 주문 품목에 등장할 수 있음 (1:N)

## 분석 시 유의사항

- `order_status`가 `취소`, `환불`인 행은 매출 집계 시 제외 필요
- `revenue`(매출)는 `quantity * unit_price`로 계산 (products.price가 아닌 unit_price 사용 — 주문 당시 실제 결제 단가)
