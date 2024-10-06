import os, sys

# import src
cwd = os.getcwd()
os.chdir('src/'); path_to_src = os.getcwd(); 
os.chdir(cwd)
if path_to_src not in sys.path:
    sys.path.append(path_to_src)
from draft import *

url = 'https://www.redfin.com/city/30818/TX/Austin'
eles = split_HomesData(url)
eles = [ele+'}' for ele in eles]

# fix v1:
# pattern = r':"[^"]+"[^,"]+"[^"]+"'
for ele in eles:
    test = re.sub(r':"[^"]+"[^,"]+"[^"]+"', ':""', ele)
    print(eval(test))
# fix 2: try replace the group with desired value 