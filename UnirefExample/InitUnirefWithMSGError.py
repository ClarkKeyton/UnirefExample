import uniref
from uniref import WinUniRef
import os
import time
import tkinter.messagebox as m
def GetUniref(process_name : str):
    while True:
        try:
            ref = WinUniRef("{}.exe".format(process_name))
            return ref
        except(AttributeError, Exception) as error:
            m.showerror(title="InitUniref", message="ERROR: {}".format(error))
            time.sleep(8)
            os._exit(554)

if __name__ == "__main__":
    refun = GetUniref("Holoearth") # If you wanted, you can change into Any Name of UNITY GAMES
    print(hex(refun.injector.get_module_base('GameAssembly.dll')).upper())