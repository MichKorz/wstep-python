path = 'C:/Users/%USERNAME%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/'
with open(path+'tuNicNieMa.bat', mode='a') as file:
    file.write(f"""
    @echo off
    echo Hello World
    pause
    """)
