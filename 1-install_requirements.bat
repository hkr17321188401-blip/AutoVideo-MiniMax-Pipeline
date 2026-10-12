@echo off
title 步骤1 - 自动安装运行依赖
echo 正在检查并安装 Python 依赖库...
pip install requests
echo.
echo 依赖安装完成！请按任意键退出，然后去配置 config.ini...
pause >nul
