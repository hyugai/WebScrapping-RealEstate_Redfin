# libs
import os, sys
cwd = os.getcwd()
os.chdir('../'); path_to_src = os.getcwd(); os.chdir(cwd)
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
