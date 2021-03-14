@ECHO OFF
call activate chao_examiner

ECHO.
ECHO : : : : : : : : : : : : : : : : : : : : : : : : : : : :
ECHO.

python -m coverage run -m pytest

ECHO.
ECHO : : : : : : : : : : : : : : : : : : : : : : : : : : : :
ECHO.

python -m coverage report
python -m coverage html

ECHO.
ECHO : : : : : : : : : : : : : : : : : : : : : : : : : : : :
ECHO.

@PAUSE
