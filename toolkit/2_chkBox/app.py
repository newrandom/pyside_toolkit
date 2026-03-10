from PySide6.QtWidgets import QApplication, QMainWindow 
from ui.ui_untitled import Ui_MainWindow
import asyncio, PySide6.QtAsyncio as QtAsyncio, time
from PySide6.QtCore import Qt

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
            time.sleep(0.01)

    async def asyncHeavyCountUp(self):
        for _ in range(100):
            self.countUp()
            await asyncio.sleep(0.01)

    def clickBtn(self):
        # 기존 작업 실행 여부 확인하기
        if self.task is not None and not self.task.done():
            try:
                self.task.cancel()
            except asyncio.CancelledError:
                pass
            finally:
                self.task = None

        self.number = 0

        # chkBox 상태 확인하기
        # if self.ui.chkAsync.checkState() == Qt.CheckState.Checked:
        if self.ui.chkAsync.isChecked():
            self.task = asyncio.create_task(self.asyncHeavyCountUp())
            # self.ui.chkAsync.setCheckState(Qt.CheckState.PartiallyChecked)        # isChecked 에 포함됨
            self.ui.chkAsync.setChecked(False)  # 체크박스 상태 초기화
        else:
            self.heavyCountUp()

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()

    window.ui.btnClick.clicked.connect(window.clickBtn)

    window.show()

    QtAsyncio.run()