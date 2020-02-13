from local.config import HOME, STASH
STASH.mkdir(parents=True,exist_ok=True)

def do_list():
    """list the files in the stash"""
    for item in STASH.iterdir():
        print(item)

def main(args):
    global ARGS
    ARGS=None
    do_list()
