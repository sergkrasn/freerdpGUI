# hook-sys.py
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules('ipaddress')
hiddenimports += collect_submodules('urllib')
hiddenimports += ['pathlib']