@echo off
SET PATH=%PATH%;"C:\Python27\";"C:\Jenkins\TDEBT_CMD_TEST\"
C:\Python27\python.exe "Run_HID_TESTS.py"
echo %JENKINS_HOME%
exit %errorlevel%