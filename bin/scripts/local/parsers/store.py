import argparse

parser = argparse.ArgumentParser(
    prog='stash store',
    usage="""stash store [-n <NOTE>] [-s <STASH>] <TARGET>

    STASH is an alternative to the default stash
    NOTE is a string to append to the stash log

    <checksum> := the md5 checksum of <TARGET>
    <entry> := <checksum>:<timestamp>:<NOTE> <TARGET>

    <TARGET> is copied to <STASH>/<checksum>.md5
    <entry> is appended to <STASH>/<checksum>.log
    """
)

parser.add_argument(
    'target',
)

parser.add_argument(
    '-n', '--note',
    action='store',
    default='none',
)

parser.add_argument(
    '-s', '--stash',
    action='store',
)

parser.add_argument(
    '-d', '--dryrun',
    action='store_true',
)

parser.add_argument(
    '-v', '--verbose',
    action='store_true'
)
