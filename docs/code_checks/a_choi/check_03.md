# 검증 3) 공통 데이터 로딩 함수 재사용성 검증

- **AI 제안 코드**: `src/data_loader.py`에 `load_all_data()` 함수 작성, 노트북에서 `sys.path.append(절대경로)`로 import
- **검증 방법**: 코드를 실행해 실제 shape 값 출력 확인
- **결과 1차**: 파일이 빈 상태(0 byte)로 저장되어 `ImportError` 발생 → 파일 내용 재작성 후 커널 재시작하여 정상 동작 확인 — `customers(1200,6)`, `orders(6000,5)`, `order_items(14603,5)`, `products(300,4)` 정상 반환
- **결과 2차**: 노트북에 하드코딩된 절대경로(`c:\dev\team4-shopping-dashboard\src`)가 다른 컴퓨터에서는 동작하지 않을 위험 발견 → `Path.cwd().parent / 'src'`로 수정하여 노트북 위치 기준 상대경로 자동 탐색되도록 개선, 재실행하여 정상 동작 확인
- **결론**: 팀원 컴퓨터에서도 `notebooks/src` 폴더 구조만 동일하면 재사용 가능한 상태로 최종 확정
