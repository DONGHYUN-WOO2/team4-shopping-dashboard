# 팀 프로젝트 계획

## 프로젝트 개요
- 프로젝트명: 온라인 쇼핑몰 데이터 요약 대시보드
- 목표: GitHub 협업과 AI 코드 단위 검증을 통해 쇼핑몰 데이터를 분석하고 Streamlit 대시보드로 시각화한다.
- 기간: 2026-08-06 ~ 2026-08-6 (1day)

## 역할 분담

| 담당자(GitHub ID) | 역할 | 담당 범위 |
|---|---|---|
| choi | 데이터 점검 및 전처리 | notebooks/01_data_check.ipynb, src/data_loader.py, docs/data_dictionary.md |
| dydtlsrl | 핵심 지표 및 분석 | notebooks/02_analysis.ipynb, src/analysis.py, docs/analysis_summary.md |
| noh | Streamlit 화면 및 시각화 | app.py, src/charts.py |
| woo | 통합, 테스트 및 문서화 | README.md, requirements.txt, docs/team_plan.md, docs/integration_test.md |

## 일정(마일스톤)

| 단계 | 내용 | 기한 | 상태 |
|---|---|---|---|
| 1 | 데이터 구조 파악 및 정제 | | 완료 |
| 2 | 데이터 병합 및 전처리 | | 완료 |
| 3 | 분석/시각화 | | 진행 중 |
| 4 | 결과 통합 및 리포트 작성 | | 진행 중 |

## 협업 규칙
- 브랜치 전략: 작업 목적마다 새 브랜치 생성 (feature/, fix/, refactor/, docs/ 접두어 사용), main에 직접 커밋하지 않음
- 커밋 컨벤션: feat(기능), fix(수정), docs(문서), refactor(구조개선), chore(설정), test(검증) 접두어 사용
- 코드 리뷰 방식: PR 생성 후 팀원 1명 이상 리뷰, 리뷰 반영 후 작성자 외 팀원이 Merge
