#!/bin/python3

import os
from ruamel.yaml import YAML

def main(fname):
    # parse yml
    yaml = YAML()
    backuplist = yaml.load(fname)
    
    # run through each item
    for name in backuplist:
        src = yaml[name]['src']
        
        # md5 to see if we need to update the copy
        h = hashlib.sha256()

        h.update('end\n')
        
        # if md5 is different, copy the file and create a new md5

    # if any of the md5s are different, do some git stuff

    # branch on date

    # merge to master

    # push master to github

def file_hash(fname):
""" returns the hash of a file based on name and contents """
    h = hashlib.sha256()
    with f as open(fname):
        while True:
            buf = f.read(16384)
            if len(buf) == 0:
                break
            h.update(buf)
    
    return h.hexdigest()


def dir_hash(h, name):
""" returns a hash of the overall directory/file structure
    using names and contents of files only """
    if os.path.isdir(name):
        # if dir, add name to hash and run through contents
        h.update('dir ' + name + '\n')
        for n in sorted(os.listdir(name)):
            dir_hash(h, n)

    if os.path.isfile(name):
        h.update(name + ' ')
        h.update(file_hash(name) + '\n')
    else:
        pass
    

if __name__ == "__main__":
    fname = sys.argv[1]    
    main(fname)
