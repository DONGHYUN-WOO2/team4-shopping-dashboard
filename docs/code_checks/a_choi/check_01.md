# 검증 1) 결측치 확인 반복문 오류 수정

- **AI 제안 코드**: `for name, df in df.items():` 로 4개 데이터프레임의 결측치 순회 출력
- **검증 방법**: 코드를 그대로 실행
- **결과**: 딕셔너리 변수명이 `dfs`인데 반복문에서 `df.items()`로 잘못 참조되어 오류 발생 확인
- **조치**: `df.items()` → `dfs.items()`로 수정 후 재실행하여 4개 데이터셋의 결측치가 정상 출력됨을 확인

```python
# 수정 전 (오류)
for name, df in df.items():
    print(f"\n--- {name} ---")
    print(df.isna().sum())

# 수정 후 (정상)
for name, df in dfs.items():
    print(f"\n--- {name} ---")
    print(df.isna().sum())
```
