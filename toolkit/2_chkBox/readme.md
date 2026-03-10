# 체크박스를 이용한 동기/비동기 작업 전환

## 📋 개요
- 체크박스 상태에 따라 동기/비동기 작업을 전환하는 예제
- PySide6 + QtAsyncio를 활용한 UI 반응성 유지 데모

## 🔧 핵심 기능
- ☑️ **체크박스 체크**: 비동기 작업 (UI 반응성 유지)
- ☐ **체크박스 언체크**: 동기 작업 (UI 일시 정지)
- 🚫 **작업 중단**: 새 작업 시작 시 이전 작업 자동 취소

## ⚡ 동기 vs 비동기 차이점
- **동기 작업**: `time.sleep(0.01)` - UI가 1초간 멈춤
- **비동기 작업**: `await asyncio.sleep(0.01)` - UI가 계속 반응

## 🎛️ 사용법
1. 앱 실행 후 클릭 버튼 누르기
2. 체크박스 상태 변경 후 다시 클릭해보기
3. 동기/비동기 차이점 체험하기

## 💡 핵심 배울 점
- `isChecked()` vs `checkState()` 사용법
    * isChecked 가 공식적으로 안내하는 방법
    * checkState는 `PySide6.QtCore.Qt` 모듈을 이용하여도 작업할 수 있음.
        * Qt.CheckState의 값
            * Unchecked - 체크해제
            * PartiallyChecked - 부분체크 (isChecked 에서는 True로 잡힘)
            * Checked - 체크설정
    * setChecked(True/False) - 체크 설정/해제 를 설정함 (단일)
    * setCheckState(Qt.CheckState.{Unchecked, PartiallyChecked, Checked}) - 해제, 부분, 체크 설정함 (세분)
- QtAsyncio를 이용한 비동기 처리
- 비동기 작업 취소 패턴
- UI 스레드 블로킹 방지

## ⚠️ 주의사항
- 비동기 작업 사용 시 반드시 `QtAsyncio.run()` 필요
- `app.exec()` 사용 시 비동기 작업 실행 불가