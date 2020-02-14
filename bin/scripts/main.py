import os
import sys
from pathlib import Path
from importlib import import_module

ARGS=sys.argv[:]
USAGE=''
SUBCOMMAND=''

ROOT=Path(ARGS.pop(0)).parent
if ARGS and ARGS[0] in 'help --help -h'.split():
    USAGE=ARGS.pop(0)
if ARGS:
    SUBCOMMAND = ARGS.pop(0)

def usage():
    print('Subcommands:')
    for item in os.listdir(ROOT/'local/commands'):
        if item.endswith('.py') and not item.startswith('_'):
            print( '\t%s' % item.split('.')[0] )

def main():
    def undocumented(*x): print( 'subcommand %s is undocumented' % SUBCOMMAND )
    def unimplemented(*x): print( 'subcommand %s is unimplemented' % SUBCOMMAND )
    try:
        module = import_module('local.commands.%s' % SUBCOMMAND)
    except ModuleNotFoundError:
        module = None

    client_main =  getattr(module, 'main', None)
    client_usage = getattr(module, 'help', None)

    if not SUBCOMMAND:
        usage()
    elif USAGE:
        (client_usage or undocumented)()
    else:
        (client_main or unimplemented)(ARGS)

main()

