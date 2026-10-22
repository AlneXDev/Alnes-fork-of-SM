import ctypes, os, sys

# Preload OpenSSL DLLs so _ssl.pyd resolves the correct exports.
# On Python 3.14, PyInstaller can collect mismatched OpenSSL DLLs from
# the cryptography wheel (libssl-3-x64.dll / libcrypto-3-x64.dll) instead
# of the DLLs that _ssl.pyd was built against (libssl-3.dll /
# libcrypto-3.dll from the base Python installation).
_candidates = []
_meipass = getattr(sys, '_MEIPASS', None)
if _meipass:
    _candidates.append(_meipass)
    _candidates.append(os.path.join(_meipass, '_internal'))
_exe_dir = os.path.dirname(sys.executable)
if _exe_dir:
    _candidates.append(_exe_dir)
    _candidates.append(os.path.join(_exe_dir, '_internal'))

for _base in _candidates:
    for _name in ("libcrypto-3.dll", "libssl-3.dll"):
        _path = os.path.join(_base, _name)
        if os.path.exists(_path):
            try:
                ctypes.WinDLL(_path)
            except Exception:
                pass
