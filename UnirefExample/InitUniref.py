import uniref
from uniref import WinUniRef
import os
import time
def GetUniref():
    while True:
        try:
            ref = WinUniRef("Holoearth.exe")
            return ref
        except(AttributeError, Exception) as error:
            print("Waiting For The Launch Holoearth...")
            time.sleep(8)
            os.system("cls")

if __name__ == "__main__":
    GetUniref()