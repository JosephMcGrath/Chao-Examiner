@ECHO OFF
call activate chao_examiner

ECHO.
ECHO : : : : : : : : : : : : : : : : : : : : : : : : : : : :
ECHO.

python -m coverage run -m pytest

ECHO.
ECHO : : : : : : : : : : : : : : : : : : : : : : : : : : : :
ECHO.

@PAUSE
