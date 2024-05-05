# BlueStacksADB

This is a simple python script to interact with BlueStacks using ADB.

## Overview

- [BlueStacksADB](#bluestacksadb)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Arguments](#arguments)
  - [License](#license)

## Requirements

- Python 3.9+
- Testing BlueStacks version: 10.10.7.1001
- BlueStacks Multi-instance Manager
- [ADB tools](https://developer.android.com/tools/adb)

## Installation

Clone the repository and install the requirements.

```bash
git clone https://github.com/SyXuan/BlueStacksADB.git
cd BlueStacksADB
pip install -r requirements.txt
pip install -e .
```

## Usage

Start an Android app on BlueStacks.

```python
from bluestacksadb import BAInstance

instance = BAInstance(
    target_instance='Rvc64',
    target_package='com.android.package.name',
)

instance.run()
```

Get the screen size of BlueStacks.

```python
screen_size = instance.get_screen_size()
print(screen_size)
```

Click the screen on BlueStacks. The coordinates are normalized to the screen size.
For example, if the screen size is 1920x1080, then 0.9, 0.1 is the point at (1920 * 0.9, 1080 * 0.1).

```python
instance.click(0.9, 0.1)
```

Stop the BlueStacks instance.

```python
instance.stop()
```

## Arguments

- `target_instance`: The instance name of BlueStacks. Default is `Rvc64` (Android 11).
- `target_package`: The package name of the Android app.
- `bluestacks_path`: The path to the BlueStacks installation directory. Default is `C:\Program Files\BlueStacks_nxt\HD-Player.exe`.
- `bluestacks_cmd`: The command to start BlueStacks. Default is `launchApp`.
- `adb_path`: The path to the ADB executable. Default is `platform-tools/adb.exe`.
- `adb_url`: The URL of the ADB server. Default is `127.0.0.1:5555`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
