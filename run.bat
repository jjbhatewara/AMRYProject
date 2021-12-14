c:\
@REM cd c:/venvs/amry/Scripts/Activate
start ../venvs/amry/Scripts/python.exe "manage.py " runserver 0.0.0.0:8000
@REM start python manage.py runserver
timeout 10
@REM start http://127.0.0.1:8000/
pause 