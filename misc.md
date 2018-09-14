#### Err
OSError: dlopen(libusb-1.0.dylib, 6): image not found

#### Err log
```
  File "/Users/jenkins/.local/lib/python2.7/site-packages/adb/adb_commands.py", line 31, in <module>
    from adb import common
  File "/Users/jenkins/.local/lib/python2.7/site-packages/adb/common.py", line 25, in <module>
    import libusb1
  File "/Users/jenkins/.pyenv/versions/2.7.14/lib/python2.7/site-packages/libusb1.py", line 8, in <module>
    from usb1.libusb1 import *
  File "/Users/jenkins/.pyenv/versions/2.7.14/lib/python2.7/site-packages/usb1/__init__.py", line 61, in <module>
    from . import libusb1
  File "/Users/jenkins/.pyenv/versions/2.7.14/lib/python2.7/site-packages/usb1/libusb1.py", line 199, in <module>
    libusb = _loadLibrary()
  File "/Users/jenkins/.pyenv/versions/2.7.14/lib/python2.7/site-packages/usb1/libusb1.py", line 173, in _loadLibrary
    return dll_loader('libusb-1.0' + suffix, **loader_kw)
  File "/Users/jenkins/.pyenv/versions/2.7.14/lib/python2.7/ctypes/__init__.py", line 366, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: dlopen(libusb-1.0.dylib, 6): image not found
```

#### Solution
```
brew rm libusb --force
brew install libusb
```
Ref. https://github.com/vpelletier/python-libusb1/issues/30
