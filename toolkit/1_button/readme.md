# 동기, 비동기 버튼
- 해당 앱에서는 pushButton과 label 을 이용하여 동기, 비동기 작업을 나타내는 것을 보여준다.
- 동기작업만 사용하는 경우에는 app.exec() 를 사용해도 가능하나
    * time.sleep(n)과 같이 스레드 점유작업인 경우에는 멈춘 것 처럼 보일 수 있음.
- 비동기 작업을 사용해야 하는 경우에는 app.exec()를 사용하면 비동기 작업이 실행될 수 없다.
- 이때 `import PySide6.QtAsyncio` 모듈을 이용하면 동기, 비동기 모두 사용이 가능한 것으로 보인다.
    * `import PySide6.QtAsyncio as QtAsyncio`
    * `QtAsyncio.run()`