# -*- coding: utf-8 -*-

import os
import json
import subprocess as spr
import sys
import tempfile
"""Main module."""

GITHUB_API_KEYS = "https://api.github.com/users/{username}/keys"


def get_public_key(username):
    keys_url = GITHUB_API_KEYS.format(username=username)
    # TODO: python raw does not support using HTTPS out of the box
    # on this OSX with Py 3.5.2, TLSv1_2 does not exist, only TLSv1
    # so as a workaround, call curl here
    # TODO: try wget if curl does not exists,
    # try requests as we will uses it as optinal dependency
    process = spr.Popen(['curl', keys_url], stdout=spr.PIPE, stderr=spr.PIPE)
    stdout, stderr = process.communicate()
    pub_keys = json.loads(stdout.decode())
    return [pub_key['key'] for pub_key in pub_keys]


def get_user_ssh_authorized_path(posix_user=None):
    if posix_user is None:
        home = os.path.expanduser('~')
    else:
        home = os.path.join(os.path.dirname(os.path.expanduser('~')), posix_user)
    return os.path.join(home, '.ssh', 'authorized_keys')


def ensuring_key_authorized(pubkey):
    pubkey = pubkey.strip()
    authorized_keys = get_user_ssh_authorized_path()
    exists = False
    with open(authorized_keys) as f:
        keys = []
        for line in f:
            if line.startswith('ssh-'):
                line = line.strip()
                type_key = ' '.join(line.split(' ')[:2])
                keys.append(type_key)
                if pubkey == type_key:
                    exists = True
    if not exists:
        with open(authorized_keys, 'at') as f:
            f.write('\n')
            f.write(pubkey)
    # TODO might need keep existing metadata of file
    #  $ ls -la ~/.ssh/authorized_keys
    # -rw-------  1 viethung.nguyen  viethung.nguyen  649 Mar 10 11:11 /Users/viethung.nguyen/.ssh/authorized_keys


def add_me_to_cronjob(username, freshness_in_hours=1):
    pythonpath = sys.executable
    crontab = "0 */{} * * * {} holdmykeys --silent {}".format(freshness_in_hours, pythonpath, username)
    try:
        existing_crontabs = spr.check_output(['crontab', '-l']).decode().splitlines()
    except spr.CalledProcessError:
        existing_crontabs = []

    if crontab in existing_crontabs:
        return

    new_crontabs = existing_crontabs + [crontab]
    _, fn = tempfile.mkstemp()
    with open(fn, 'w') as f:
        for line in new_crontabs:
            f.write(line)
            f.write('\n')
            # TODO skip if exists
    spr.call(['crontab', fn])
    try:
        os.remove(fn)
    except Exception:
        pass


def main():
    print(get_user_ssh_authorized_path())
    print('Ensuring all keys in authorized_keys')
    for key in get_public_key('hvnsweeting'):
        ensuring_key_authorized(key)

    print('Adding this tool to run every hour in crontab')
    add_me_to_cronjob('hvnsweeting')


if __name__ == "__main__":
    # TODO args must has --silent to silent when run in cron mode
    main()
