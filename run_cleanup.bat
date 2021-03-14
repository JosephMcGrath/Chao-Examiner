@ECHO OFF
call activate chao_examiner

ECHO.
ECHO : : : : : : : : : : : : : : : : : : : : : : : : : : : :
ECHO.

python -m black .

ECHO.
ECHO : : : : : : : : : : : : : : : : : : : : : : : : : : : :
ECHO.

python -m pylint src/chao_examiner

ECHO.
ECHO : : : : : : : : : : : : : : : : : : : : : : : : : : : :
ECHO.

python -m mypy src/chao_examiner

ECHO.
ECHO : : : : : : : : : : : : : : : : : : : : : : : : : : : :
ECHO.

@PAUSE
