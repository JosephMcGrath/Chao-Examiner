@ECHO OFF
@CALL activate chao_examiner

ROBOCOPY %~dp0\dist %package_local%

DEL %~dp0dist /Q
DEL %~dp0build /Q

TIMEOUT 5

@python setup.py sdist bdist_wheel > build.log
ROBOCOPY %~dp0\dist %package_local%
@ECHO ============================================================================================================================= >> build.log
@pip uninstall chao_examiner -y >> build.log
@ECHO ============================================================================================================================= >> build.log
@pip install --no-index --find-links=file:%~dp0\dist chao_examiner >> build.log

@ECHO Done
@PAUSE
