@echo off
if exist %1\AGCLoader.swf (
    mkdir %1\AGCLoader && call ffdec\ffdec.bat -export all %1\AGCLoader %1\AGCLoader.swf
)
if exist %1\client.swf (
    mkdir %1\client && call ffdec\ffdec.bat -export all %1\client %1\client.swf
)