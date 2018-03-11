# -*- coding: utf-8 -*-

"""Console script for holdmykeys."""
import argparse
import sys

from .holdmykeys import get_public_key, add_me_to_cronjob, ensuring_key_authorized


def print_or_silent(msg, silent=True):
    if silent:
        return
    else:
        print(msg)


def main(args=None):
    argp = argparse.ArgumentParser()
    argp.add_argument('username', help='GitHub username to get SSH public keys.')
    argp.add_argument('--silent', help='Run silently without output.',
                      action='store_true')
    args = argp.parse_args()
    silent = args.silent
    import functools
    myprint = functools.partial(print_or_silent, silent=silent)

    myprint('Ensuring all keys in authorized_keys')
    username = args.username
    for key in get_public_key(username):
        ensuring_key_authorized(key)

    myprint('Adding this tool to run every hour in crontab')
    add_me_to_cronjob(username)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
