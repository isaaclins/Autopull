@echo off
setlocal
cd ..

echo started file

git add .
echo added files

set /p message="Enter your commit message: "
echo added message

git commit -m "%message%"
echo committed changes
