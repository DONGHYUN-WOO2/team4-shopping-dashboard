# 검증 2) 테이블 간 연결 관계(FK) 정합성 확인

- **AI 제안 코드**: `isin().all()`로 orders/order_items의 참조 키가 부모 테이블에 모두 존재하는지 확인
- **검증 방법**: 코드를 실제 실행하여 True/False 결과 직접 확인
- **결과**: `orders → customers`, `order_items → orders`, `order_items → products` 3개 관계 모두 `True`로 출력되어 정상 연결 확인

```python
check1 = orders['customer_id'].isin(customers['customer_id']).all()
print("orders -> customers 연결 정상:", check1)

check2 = order_items['order_id'].isin(orders['order_id']).all()
print("order_items -> orders 연결 정상:", check2)

check3 = order_items['product_id'].isin(products['product_id']).all()
print("order_items -> products 연결 정상:", check3)
```
