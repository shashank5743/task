import os
BASEDIR ='/Users/shashank/Downloads'
 
def list_files(somedir):
    files = []
    for item in os.listdir(somedir):
        itempath = os.path.join(somedir,item)
        if os.path.isfile(itempath):
            files.append(itempath)
    return files
 
def list_dirs(somedir):
    dirs = []
    for item in os.listdir(somedir):
        itempath = os.path.join(somedir, item)
        if os.path.isdir(itempath):
            dirs.append(itempath)
    return dirs
 
def traverse(somedir):
    results = list_files(somedir)
    for directory in list_dirs(somedir):
        results += traverse(directory)
    return results
 
for a in traverse(BASEDIR):
    print (a)
