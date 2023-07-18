import subprocess

# Specify the application you want to open
applications = 'C:/Users/ТАЛГАТ/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'

try:
    # Open the application using the default system behavior
    subprocess.Popen(applications)
except FileNotFoundError:
    print(f"Could not find the '{applications}' application.")