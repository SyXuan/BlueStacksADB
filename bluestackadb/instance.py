import sys
import time
import subprocess

from .constants import Constants

# Example file property target
# "C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Rvc64 --cmd launchAppWithBsx --package "com.playstudios.showstar" --source desktop_shortcut
# "C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Pie64_10 --cmd launchApp --package "com.playstudios.showstar" --source desktop_shortcut
# BLUESTACKS_PATH = 'C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe'
# BLUESTACKS_INSTANCE = 'Rvc64'
# BLUESTACKS_CMD = 'launchApp' # or launchAppWithBsx will also open the BlueStacks X
# ANDROID_PACKAGE = 'com.playstudios.showstar'
# ADB_PATH = 'C:\\BingSyuan\\platform-tools-latest-windows\\platform-tools\\adb.exe'
# ADB_URL = '127.0.0.1'
# ADB_PORT = '5555'


class BAInstance:
    def __init__(
            self,
            target_instance=Constants.BLUESTACKS_INSTANCE,
            target_package=Constants.ANDROID_PACKAGE,
            bluestacks_path=Constants.BLUESTACKS_PATH,
            bluestacks_cmd=Constants.BLUESTACKS_CMD,
            adb_path=Constants.ADB_PATH,
            adb_url=Constants.ADB_URL
    ):
        self.bluestacks_path = bluestacks_path
        self.bluestacks_cmd = bluestacks_cmd
        self.adb_path = adb_path
        self.adb_url = adb_url
        self.target_instance = target_instance
        self.target_package = target_package
        self.pid = None
        self.width = None
        self.height = None

    def set_package(self, package):
        self.target_package = package
        print(f'Set package to {self.target_package}')

    def run(self):
        print(f'Running {self.target_package} on {self.target_instance}')
        result = subprocess.Popen(
            [
                self.bluestacks_path,
                '--instance',
                self.target_instance,
                '--cmd',
                self.bluestacks_cmd,
                '--package',
                self.target_package,
                '--source',
                'desktop_shortcut',
            ],
            # text=True
        )
        self.pid = result.pid
        print(f'PID: {self.pid}')
        return result

    def connect(self):
        print(f'Connecting to {self.adb_url}')
        # Use adb to power on the device
        result = subprocess.run(
            [
                self.adb_path,
                'connect',
                f'{self.adb_url}',
            ],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return result

    def stop(self, pid=None):
        if pid is None:
            pid = self.pid
        pid = str(pid)
        # Use taskkill to stop the process
        print(f'Stopping PID: {pid}')
        result = subprocess.run(
            [
                'taskkill',
                '/F',
                '/PID',
                pid,
            ],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return result

    def get_window_size(self, retry=Constants.RETRY_COUNT):
        print(f'Getting window size...')
        try:
            self.connect()
            # Get the window size
            result = subprocess.run(
                [
                    self.adb_path,
                    'shell',
                    'wm',
                    'size',
                ],
                capture_output=True,
                text=True
            )
            print(result.stdout)
            # Physical size: 960x540
            self.width, self.height = result.stdout.split(': ')[1].split('x')
            self.width = int(self.width)
            self.height = int(self.height)
            print(
                f'Get window size. Width: {self.width}, Height: {self.height}')
            return result
        except Exception as e:
            if retry > 0:
                print(f'Error: {e}. Retrying...')
                time.sleep(1)
                return self.get_window_size(retry - 1)
            else:
                print(f'Error: {e}. Unable to get window size')
                return None

    def click_percentage(self, x, y):
        '''
        Click on the screen based on percentage
        Example: click_percentage(0.97, 0.05) will click on the top right corner

        Args:
        x: float, 0 to 1
        y: float, 0 to 1
        '''
        if self.width is None or self.height is None:
            print(f'Window size is not set. Getting window size...')
            self.get_window_size()

        x = int(x * self.width)
        y = int(y * self.height)
        print(f'Clicking on the screen at {x}, {y}')

        result = subprocess.run(
            [
                self.adb_path,
                'shell',
                'input',
                'tap',
                str(x),
                str(y),
            ],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        return result


if __name__ == '__main__':
    '''
    Arguments
    -run: Run the app
    -stop: Stop the app
    -connect: Connect to the device
    -window-size: Get the window size
    -click-percentage: Click on the screen based on percentage
    '''
    if len(sys.argv) < 2:
        print('Please provide an argument')
        sys.exit(1)

    app = BAInstance()
    if sys.argv[1] == '-run':
        instance = sys.argv[2] if len(
            sys.argv) > 2 else Constants.BLUESTACKS_INSTANCE
        package = sys.argv[3] if len(
            sys.argv) > 3 else Constants.ANDROID_PACKAGE
        app = BAInstance(target_instance=instance, target_package=package)
        app.run()
    elif sys.argv[1] == '-stop':
        pid = sys.argv[2]
        app.stop(pid)
    elif sys.argv[1] == '-connect':
        app.connect()
    elif sys.argv[1] == '-window-size':
        app.get_window_size()
    elif sys.argv[1] == '-click-percentage':
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        app.click_percentage(x, y)
    else:
        print('Invalid argument')
        sys.exit(1)
