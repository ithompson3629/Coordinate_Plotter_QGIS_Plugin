@echo off
call "C:\Program Files\QGIS 3.28.8\bin\o4w_env.bat"


@echo on
pyrcc5 -o resources.py C:\Users\ithompson\AppData\Roaming\QGIS\QGIS3\profiles\PCA_QGIS_profile\python\plugins\coordinate_plotter\resources.qrc

