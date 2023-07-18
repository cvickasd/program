import subprocess

# Specify the application you want to open
application = 'C:/Users/ТАЛГАТ/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'
application2 = r"C:\Users\ТАЛГАТ\AppData\Local\Programs\Microsoft VS Code\Code.exe"

try:
    # Open the application using the default system behavior
    subprocess.Popen(application)
    subprocess.Popen(application2)
except FileNotFoundError:
    print(f"Could not find the '{application}' application.")
