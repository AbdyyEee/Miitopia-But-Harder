import tkinter
import tkinter.filedialog
import tkinter.messagebox

from os import remove
from shutil import rmtree

from folder_handling import download_and_move_3ds, download_and_move_switch


TITLE = "Auto Hard Mode Installer"

# TODO: Use custom pop-ups or an alternative to Yes/No for answers to questions
# TODO: Cleaning up module imports
# TODO: Implement JPN version (not supported for now, not properly implemented in the mod and in this script.)
# TODO: Possibbly implement error handling
# TODO: Implement Mac and Linux releases

# Initial prompt
inital_popup = tkinter.messagebox.askokcancel(
    title=f"{TITLE} Version 1.0.0",
    message="""
This installer will automatically install the latest version of the Hard Mode mod for both 3DS and Switch:
Zipped downloads will always still be available on github, this is just a means to have it automatically install.

Before you continue, if you are planning to use this installer for 3DS, I recommend moving existing mod files from
the Miitopia mod directory, 

If you know what you are doing or are a modder, make sure no sarc conflict with any of mine.

** Press "OK" to continue **
""",
)

# Checking game version True = 3DS, False = Switch:
if inital_popup:
    game_version = tkinter.messagebox.askyesno(
        title=TITLE,
        message="""Are you playing on the 3DS version? 
(Yes for 3DS, No for Switch)""",
    )
    # -- 3DS --
    if game_version:
        download_and_move_3ds()
        tkinter.messagebox.askokcancel(
            title=TITLE,
            message="Succesfully installed, launch your version of Miitopia and check if the title-screen has loaded.",
        )
    # -- Switch --
    if not game_version:
        switch_version = tkinter.messagebox.askyesno(
            title=TITLE,
            message="""Are you on Yuzu or Ryujinx?  (
Yes for Yuzu, No for Ryujinx)""",
        )
        if switch_version:
            download_and_move_switch("Yuzu")
            tkinter.messagebox.askokcancel(
                title=TITLE,
                message="Succesfully installed, launch your version of Miitopia and check if the title-screen has loaded.",
            )
        if not switch_version:
            download_and_move_switch("Ryujinx")
            tkinter.messagebox.askokcancel(
                title=TITLE,
                message="Succesfully installed, launch your version of Miitopia and check if the title-screen has loaded.",
            )

# Removing any leftover files
try:
    rmtree("Miitopia But Harder Version 2.0 Final Release Switch Version")
except:
    # zip files are not folders so remove it here
    remove("Miitopia.But.Harder.3DS.Ver.2.0.zip")
    remove("Miitopia.but.Harder.Switch.Ver.2.0.zip")
    rmtree("romfs")
