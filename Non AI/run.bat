@echo on
set loopcount=132
:loop
"C:\Users\Parth\AppData\Local\Programs\Python\Python36\python.exe" "C:\Users\Parth\Code\Projects\Python\Pygame\Grid\Grid-test\Non AI\BreathFirstSearch.py"
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop

