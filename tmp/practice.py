import os
import re

# word = 'asdf'
# special_char = False
regexp = re.compile('[^0-9a-zA-Z]+')
# if regexp.search(word):
#     special_char = True

# print(special_char)

home_dir = os.environ['HOME']
username = os.environ['USER']
path = os.environ['PATH']

files = []
for p in path.split(':'):
    if os.path.isdir(p):
        # print(p)
        # print(os.listdir(p))
        files_indir = [f for f in os.listdir(p) if os.path.isfile(f"{p}/{f}") if not regexp.match(f)]

        # files_indir = [f for f in os.listdir(p)]
        # print(files_indir)
        files.extend(files_indir)


result = list(filter(lambda x: len(x) <= 2, files))
print(result)





# print(files_indir)


#     # print(p)
#     files_indir = [f for f in os.listdir(p) if os.path.isdir(p)]
#     files.extend(files_indir)

# print(files)
# print(files)
# files = [f for f in os.listdir('/usr/local/bin') if os.path.isfile('/usr/local/bin')]
# print(files)
# print(os.listdir('/usr/local/bin'))
# print(os.listdir('/usr/local/bin'))
# print(os.path.isdir('/Library/Frameworks/Python.framework/Versions/3.7/bin'))
