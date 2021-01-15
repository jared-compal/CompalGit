import os
import glob
file_dir = "C:\Program Files (x86)\Steam\steamapps\*.acf"
List = []
type = '.acf'

# '228980' SteamWorks
# '250820' SteamVR
# '410570' GunJack
# '450390' The LAb
# '826480' VR GirlFriend
#  file example: manifest_xxxxxx.acf

def CheckInstalledGame():
    for file in glob.glob(file_dir):
        str = os.path.basename(file)
        str = str[12:].replace(type,'')
        if str != '228980' and str != '250820':
            List.append(str)
    print(List)
    return List
# uncommnet CheckInstalledGame() for testing
# CheckInstalledGame()
