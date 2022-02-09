@echo off
set JAVA_HOME=%JAVADIR%%1
setx JAVA_HOME "%JAVADIR%%1" /M
echo New java version should now be %JAVADIR%%1, run java -version in a new shell if you want to check if this is correct.
PAUSE
