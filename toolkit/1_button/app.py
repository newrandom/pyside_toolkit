from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_untitled import Ui_MainWindow
import asyncio, PySide6.QtAsyncio as QtAsyncio, time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.number = 0
        self.ui.label.setText("Push the button")
        self.task = None        # 비동기 제어를 위한 변수 초기화

    def countUp(self):
        self.number += 1
        self.ui.label.setText(str(self.number))
        
    def heavyCountUp(self):
        for _ in range(100):
            self.countUp()
            time.sleep(0.01)        # 동기작업이 진행될 때는 UI가 멈춘것처럼 보임

    async def asyncHeavyCountUp(self):
        for _ in range(100):
            self.countUp()
            await asyncio.sleep(0.01)       # 비동기작업이 진행될 때는 UI가 멈추지 않고 계속 업데이트됨

    def clickBtnSync(self):
        # 이전에 실행 중인 비동기 작업이 있다면 취소
        if self.task and not self.task.done():
            try:
                self.task.cancel()
            except asyncio.CancelledError:
                pass
            finally:
                self.task = None

        self.number = 0
        self.heavyCountUp()

    async def clickBtnAsync(self):
        # 이전에 실행 중인 비동기 작업이 있다면 취소
        await self.cancelAsyncTask()

        # 새 작업 진행
        self.task = asyncio.create_task(self.asyncHeavyCountUp())

    # 비동기 버튼 취소 메서드
    async def cancelAsyncTask(self):
        if self.task and not self.task.done():
            self.task.cancel()
            self.number = 0
            try:
                await self.task
            except asyncio.CancelledError:
                pass
            finally:
                self.task = None
                return
        else:
            # 비동기 작업이 없거나 완료된 경우 초기화
            self.number = 0

    # 동기 작업을 비동기처럼 실행하는 메서드
    async def clickBtnSync2Async(self):
        # self.task = await asyncio.to_thread(self.clickBtnSync)
        self.task = await asyncio.to_thread(lambda: self.clickBtnSync())
        print(self.task)        # to_thread는 동기 작업이 완료될 때까지 기다렸다가 결과를 반환하므로, clickBtnSync()의 결과는 None이 될 것임

if __name__=="__main__":
    app = QApplication()
    window = MainWindow()

    # 버튼 연결
    window.ui.btnSync.clicked.connect(lambda: window.clickBtnSync())
    window.ui.btnAsync.clicked.connect(lambda: asyncio.create_task(window.clickBtnAsync()))
    window.ui.btnSync2Async.clicked.connect(lambda:asyncio.create_task(window.clickBtnSync2Async()))

    window.show()
    # app.exec()        # app.exec() 를 선언하면 비동기 작업이 실행되지 않음
    QtAsyncio.run(handle_sigint=True)       # 비동기를 사용하려면 QtAsyncio(PySide6.QtAsyncio)를 사용하여 이벤트 루프를 실행해야 함