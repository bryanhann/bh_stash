import hashlib
import datetime
import os
import shutil
import argparse
import sys
from pathlib import Path, PosixPath

def md5(path):
    a=hashlib.md5()
    a.update(path.read_bytes())
    return a.hexdigest()

def walk(item):
    item = Path(item)
    if not item.exists():
        return
    if item.is_symlink():
        return
    if item.is_file():
        yield item
        return
    for subitem in item.iterdir():
        for xx in walk(subitem):
            yield xx

def append(log,entry,*x):
    with open(log, 'a') as fd:
        fd.write( entry + '\n' )

def dry( cmd, arglist, OPT ):
    out = "%s%s" % (cmd.__name__, repr(arglist) )
    if OPT.dryrun: 
        print( 'dryrun> %s' % out )
    elif OPT.verbose:
        print( 'verbose> %s' % out )
    if not OPT.dryrun:
        cmd(*arglist)
