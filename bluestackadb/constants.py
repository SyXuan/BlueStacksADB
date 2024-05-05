class Constants:
    # Example file property target
    # "C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Rvc64 --cmd launchAppWithBsx --package "com.playstudios.showstar" --source desktop_shortcut
    # "C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Pie64_10 --cmd launchApp --package "com.playstudios.showstar" --source desktop_shortcut
    BLUESTACKS_PATH = 'C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe'
    BLUESTACKS_INSTANCE = 'Rvc64'
    BLUESTACKS_CMD = 'launchApp' # or launchAppWithBsx will also open the BlueStacks X
    ANDROID_PACKAGE = 'com.playstudios.showstar'
    # Pop!Slots: com.playstudios.popslots
    # MGMSlotsLive: com.playstudios.showstar
    # myVEGAS: com.playstudios.myvegas
    # myKONAMI: com.playstudios.mykonami
    # myVEGASBingo: com.playstudios.myvegas.bingo
    # Tetris: com.n3twork.tetris
    # myVEGASBlackjack: com.playstudios.myvegas.blackjack
    ADB_PATH = 'platform-tools/adb.exe'
    ADB_URL = '127.0.0.1:5555'
    RETRY_COUNT = 5
