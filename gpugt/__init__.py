import ctypes
from pathlib import Path


def _preload_nvidia_libs():
    try:
        import nvidia.cu13
        lib_dir = Path(nvidia.cu13.__path__[0]) / 'lib'
        if lib_dir.is_dir():
            for f in sorted(lib_dir.iterdir()):
                if '.so' in f.name and not f.name.endswith('.a'):
                    try:
                        ctypes.CDLL(str(f), mode=ctypes.RTLD_GLOBAL)
                    except OSError:
                        pass
    except ImportError:
        pass


_preload_nvidia_libs()
