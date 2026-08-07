# 코드 단위 검증 기록

## 1. 작성자
- 이름: 양성용
- GitHub ID: dydtlsrl
- 담당 기능: 핵심 지표 및 분석

## 2. 검증 단위
- 기능명: 주문 상세 금액 계산
- 관련 Issue: #(이슈번호)
- 관련 파일: notebooks/02_analysis.ipynb

## 3. 코드 목적
주문 상세(order_items)의 수량과 단가를 곱해 항목별 결제 금액을 계산한다.

## 4. 입력
data/raw/order_items.csv (quantity, unit_price 컬럼)

## 5. AI 활용
- 사용 도구: (Claude)
- 질문 내용: order_items.csv를 상대경로로 읽고 item_amount 컬럼 생성
- AI가 제안한 핵심 내용: pd.read_csv + 곱셈 컬럼 생성

## 6. 실행 전 예상
order_items에 item_amount라는 새 컬럼이 추가되고, 행 수는 원본과 동일할 것이다.

## 7. 실행 코드
(노트북 최종 코드 요약 또는 위치 표기)

## 8. 실제 결과
item_amount 컬럼이 정상 추가됨. head() 출력에서 값 일치 확인.

## 9. 검증 방법
- 정상 조건: item_amount == quantity * unit_price (assert로 확인)
- 예외 조건: (다음 단계에서 결측치/0값 케이스 확인 예정)
- assert 결과: 통과

## 10. AI 코드에서 수정한 부분
(위에서 정리한 Before/After 코드 그대로 붙여넣기)

## 11. 결과 해석
각 주문 상세 항목의 실제 결제 금액을 계산할 수 있게 되어,
이후 매출 집계의 기초 데이터로 사용 가능하다.

## 12. 아직 이해되지 않는 부분