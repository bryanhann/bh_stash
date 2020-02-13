import sys
import os
from pathlib import Path
print( sys.argv )
root=Path(sys.argv[0]).parent
print(44, root)
try:
    script = sys.argv[1]
except IndexError:
    script = 'help'
args = sys.argv[2:]

def help():
    print( 'usage: stash <subcommand>\n')
    print('Subcommands:')
    for item in os.listdir(root/'local/commands'):
        if item.endswith('.py') and not item.startswith('_'):
            print( '\t%s' % item.split('.')[0] )
if script=='help':
    help()
    exit()

try:
    exec( 'import local.commands.%s as foo' % script)
except ModuleNotFoundError:
    print('unknown subcommand: %s' % script )
    exit()
if script=='help':
    os.chdir( root )
foo.main(args)
print(88, foo, script)
