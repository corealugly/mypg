__author__ = 'corealugly'

import hashlib
import argparse
import sys
import getpass
#import pygtk
import gtk
import time

def main():
        DEF_TIME=10  #delay before clear bufer

        parser = argparse.ArgumentParser(description='update db OSHS')
        # parser.add_argument('-p', '--password', type=str, help='enter password')
        parser.add_argument('-p', '--password', action="store_true", help='enter password')
        parser.add_argument('-n', '--insert_n', action="store_true", help='insert line break character')
        parser.add_argument('-t', '--time', type=int, help='delay before clear bufer')
        args = parser.parse_args()
        if len(sys.argv) == 1:
                parser.print_help()
                exit(1)

        if args.password:
            password = getpass.getpass()
            if args.insert_n: password += "\n"

            hasher = hashlib.sha512()
            hasher.update(password)
            hash_password = hasher.hexdigest()

            clipboard = gtk.clipboard_get()
            clipboard.set_text(hash_password)
            clipboard.store()

            if args.time:  DEF_TIME = args.time
            time.sleep(DEF_TIME)
            clipboard.clear()


if __name__ == "__main__":
    main()

