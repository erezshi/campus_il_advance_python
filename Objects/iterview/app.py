import os
# import glob

P = os.environ["PATH"]
All_PATHS = P.split(':')
# print(All_PATHS)
# os.listdir('/Applications/Visual Studio Code.app/Contents/Resources/app/bin')
# print(glob.glob('/usr/local/bin/*'))
# print(os.listdir('/usr/local/bin/'))
# files = [ f for f in os.listdir('/usr/local/bin/') if os.isfi]
mypath  = '/usr/local/bin/'
files = [ f for f in os.listdir(mypath) if os.path.isfile(mypath + f) and len(f) <= 2 ]
# import os
# mypath  = '/usr/local/bin/'
# print(os.path.isfile(mypath + 'wget'))

# print(files)
# all_files = [ p for p in All_PATHS]
# print 


# files_filtered = [ f for f in os.listdir(p) for p in All_PATHS if os.path.isfile(p + f) and len(f) <= 2]

# files_filtered = [ f for p in All_PATHS for f in os.listdir(p) if os.path.isfile(p + f) and len(f) <= 2]
files_filtered = [ f for f in os.listdir(p) for p in All_PATHS ]
print(files_filtered)