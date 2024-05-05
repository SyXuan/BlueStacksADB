import time

import bluestackadb
from bluestackadb import Utils

STEP_TIME = 60

print('\nRunning BlueStacks instance')
instance = bluestackadb.BAInstance(
    target_instance='Rvc64',
)
instance.run()
pid = instance.pid
Utils.count_down(30)

# Pop!Slots: com.playstudios.popslots
# MGMSlotsLive: com.playstudios.showstar
# myVEGAS: com.playstudios.myvegas
# myKONAMI: com.playstudios.mykonami
# myVEGASBingo: com.playstudios.myvegas.bingo
# Tetris: com.n3twork.tetris
# myVEGASBlackjack: com.playstudios.myvegas.blackjack

# Type 1 - Click right top corner of the screen 1 hour
type1 = {
    'Pop!Slots': 'com.playstudios.popslots',
    'MGMSlotsLive': 'com.playstudios.showstar',
    'myVEGAS': 'com.playstudios.myvegas',
    'myKONAMI': 'com.playstudios.mykonami',
}

# Type 2 - 

for key, value in type1.items():
    print(f'\nOpening {key}')
    instance.set_package(value)
    instance.run()

    start = time.time()
    while time.time() - start < STEP_TIME:
        Utils.count_down(10)
        print('\nClicking on the right top corner of the screen')
        instance.click_percentage(0.97, 0.05)
        current_time = Utils.seconds_to_time(int(time.time() - start))
        remaining_time = Utils.seconds_to_time(STEP_TIME - int(time.time() - start))
        if remaining_time < 0:
            remaining_time = 0
        print(f'Current step running for {current_time}. Remaining {remaining_time}')

    Utils.count_down(10)

instance.stop(pid)
