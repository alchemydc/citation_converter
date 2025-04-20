@echo off

REM Create directories if they don't exist
if not exist "input" mkdir input
if not exist "output" mkdir output

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install requirements
pip install -r requirements.txt

REM Copy sample citations file if input is empty
if not exist "input\citations.txt" (
    copy samples\citations.txt input\citations.txt
    echo Created sample citations file in input\citations.txt
)

echo Setup complete! Virtual environment is activated and dependencies are installed.
echo A sample citations file has been placed in input\citations.txt
