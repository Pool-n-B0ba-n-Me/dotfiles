#! /usr/bin/env python 

import os, sys
import shutil

HOME = os.getenv('HOME')
cnt = 0

# Remove a file that has path dst
# Can remove file, directory, and symlinks
def removeFile(dst):
    if os.path.islink(dst): # remove link
        print "Removing %s" % dst
        os.unlink(dst)
    elif os.path.exists(dst):
        if os.path.isdir(dst): # remove dir
            print "Removing %s" % dst
            shutil.rmtree(dst)
        if os.path.isfile(dst): # remove file
            print "Removing %s" % dst
            os.unlink(dst)

# Point dst to src with symlink
# Remove dst first if it exists
def makelink(src, dst):
    removeFile(dst) 
    os.symlink(src, dst)
    global cnt
    cnt = cnt + 1
    print "[%d]\t%s -> %s" % (cnt, dst, src)

def install():
    current_path = os.path.abspath(os.path.dirname(__file__))
    print "Installing from %s\n" % current_path
    for dirpath, dirnames, filenames in os.walk(current_path):
        # all directories
        for subdirname in dirnames:
            # custom in oh-my-zsh needs to be handled differently
            if subdirname.endswith('zshcustom.symlink'):
                src = os.path.join(dirpath, subdirname)
                dst = os.path.join(HOME, '.oh-my-zsh/custom')
                makelink(src, dst)
            elif subdirname.endswith('.symlink'):
                src = os.path.join(dirpath, subdirname)
                dst = os.path.join(HOME, '.' + subdirname[:-8])
                makelink(src, dst)
        # all non-directory files
        for filename in filenames:
            if filename.endswith('.symlink'):
                src = os.path.join(dirpath, filename)
                dst = os.path.join(HOME, '.' + filename[:-8])
                makelink(src, dst)

def backup():
    pass

def uninstall():
    current_path = os.path.abspath(os.path.dirname(__file__))
    print "Uninstalling from %s\n" % current_path
    for dirpath, dirnames, filenames in os.walk(current_path):
        for subdirname in dirnames:
            if subdirname.endswith('.symlink'):
                dst = os.path.join(HOME, '.' + subdirname[:-8])
                removeFile(dst)
        for filename in filenames:
            if filename.endswith('.symlink'):
                dst = os.path.join(HOME, '.' + filename[:-8])
                removeFile(dst)

COMMANDS = {
    'install': {
        'description': 'Install dot files',
        'func': install,
    },
    'backup': {
        'description': 'Backup dot files',
        'func': backup,
    },
    'uninstall': {
        'description': 'Uninstall all dot files',
        'func': uninstall
    }
}

def usage():
    print "Usage: ./dotfiles.py command [options]"
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        usage()
    
    if sys.argv[1] not in COMMANDS:
        print "ERROR: Command '%s' not found" % sys.argv[1]
        usage()
    
    COMMANDS.get(sys.argv[1])['func']()

if __name__ == '__main__':
    main()
