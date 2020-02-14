import datetime
import os
import shutil
import argparse
import sys
from pathlib import Path, PosixPath

from local.parsers.store import parser
from local.config import STASH
from local.util import md5, append, dry

def store(target):
    """store a file in the stash\n """
    assert target.exists()
    STASH.mkdir(parents=True,exist_ok=True)
    checksum = md5(target)
    dst=STASH/(checksum+'.md5')
    log=STASH/(checksum+'.log')
    stamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    entry='%s:%s:%s %s' % (checksum,stamp,ARGS.note,target)
    dry( shutil.copy, (target,dst), ARGS )
    dry( append, (log,entry), ARGS )

def main(args):
    global ARGS
    ARGS=parser.parse_args(args)
    store(Path(ARGS.target))
