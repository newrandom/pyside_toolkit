@REM make venv for windows

call python -m venv venv
call .\venv\scripts\activate
call pip install -r requirements.txt

pause