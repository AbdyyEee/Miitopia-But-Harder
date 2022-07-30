from os import mkdir
from os.path import expanduser, isdir
from shutil import copytree, rmtree
from zipfile import ZipFile

from wget import download

# -- Game IDS --
SWITCH_ID = "01003DA010E8A000"
RYUJINX_SWITCH_ID = "01003da010e8a000"
USA_ID = "00040000001B4E00"
EU_ID = "00040000001B4F00"
# JPN_ID = "0004000000178800" 

# -- Download Links --
LATEST_SWITCH_VERSION = "https://github.com/AbdyyEee/Miitopia-But-Harder/releases/download/Main/Miitopia.but.Harder.Switch.Ver.2.0.zip"
LATEST_3DS_VERSION = "https://github.com/AbdyyEee/Miitopia-But-Harder/releases/download/Main/Miitopia.But.Harder.3DS.Ver.2.0.zip"


def download_and_move_3ds() -> None:
    """Downloads the latest release of the Hard Mode mod on Github and automatically
    extracts and inserts the file into the Citra mod directory.
    """
    # Downloading
    download(LATEST_3DS_VERSION)
    mod_path_3ds = expanduser("~\AppData\Roaming\Citra\load\mods")
    # Unzipping
    with ZipFile("Miitopia.But.Harder.3DS.Ver.2.0.zip") as f:
        f.extractall()
    # USA
    if isdir(fr"{mod_path_3ds}\{USA_ID}"):
        rmtree(fr"{mod_path_3ds}\{USA_ID}\romfs", ignore_errors=True)
        mkdir(fr"{mod_path_3ds}\{USA_ID}\romfs")
        copytree("romfs", fr"{mod_path_3ds}\{USA_ID}\romfs", dirs_exist_ok=True)
    # EU
    if isdir(fr"{mod_path_3ds}\{EU_ID}"):
        rmtree(fr"{mod_path_3ds}\{EU_ID}\romfs", ignore_errors=True)
        mkdir(fr"{mod_path_3ds}\{EU_ID}\romfs")
        copytree("romfs", fr"{mod_path_3ds}\{EU_ID}\romfs", dirs_exist_ok=True)

def download_and_move_switch(emulator: str) -> None:
    """Downloads the latest release of the Hard Mode mod on Github and automatically
    extracts and inserts the file into the Yuzu mod directory.
    
    if the parameter "emulator" is set to "Ryujinx", it will move all the folders into
    the ryujinx mod paths, and vise versa, if it is set to Yuzu, it will do the same action.
    """ 
    # Downloading
    download(LATEST_SWITCH_VERSION)
    yuzu_path = expanduser("~\AppData\Roaming\Yuzu\load")
    ryujinx_path = expanduser("~\AppData\Roaming\Ryujinx\mods\contents")
    # Unzipping
    with ZipFile("Miitopia.But.Harder.Switch.Ver.2.0.zip") as f:
        f.extractall()
    
    match emulator:
        case "Yuzu":
            if isdir(fr"{yuzu_path}\{SWITCH_ID}"):
                rmtree(fr"{yuzu_path}\{SWITCH_ID}\Miitopia But Harder Version 2.0 Final Release Switch Version", ignore_errors=True)
                mkdir(fr"{yuzu_path}\{SWITCH_ID}\Miitopia But Harder Version 2.0 Final Release Switch Version")
                copytree("Miitopia But Harder Version 2.0 Final Release Switch Version", fr"{yuzu_path}\{SWITCH_ID}\Miitopia But Harder Version 2.0 Final Release Switch Version", dirs_exist_ok=True)
        case "Ryujinx":
            if isdir(fr"{ryujinx_path}\{RYUJINX_SWITCH_ID}"):
                rmtree(fr"{ryujinx_path}\{RYUJINX_SWITCH_ID}\Miitopia But Harder Version 2.0 Final Release Switch Version", ignore_errors=True)
                mkdir(fr"{ryujinx_path}\{RYUJINX_SWITCH_ID}\Miitopia But Harder Version 2.0 Final Release Switch Version")
                copytree("Miitopia But Harder Version 2.0 Final Release Switch Version", fr"{ryujinx_path}\{RYUJINX_SWITCH_ID}\Miitopia But Harder Version 2.0 Final Release Switch Version", dirs_exist_ok=True)


        
