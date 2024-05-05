import bluestackadb
from bluestackadb import Utils

print('\nRunning BlueStacks instance')
instance = bluestackadb.BAInstance(
    target_instance='Rvc64',
    target_package='com.android.package.name',
)
instance.run()

Utils.count_down(60)
print('\nClicking on the right top corner of the screen')
instance.click_percentage(0.97, 0.05)

Utils.count_down(10)
print('\nStop the BlueStacks instance')
instance.stop()
