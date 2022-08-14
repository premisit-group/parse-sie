
import argparse
import shlex
import datetime

# -------------------------------------------------------------------------
# Description
#
# -------------------
# About argparse
# -------------------
# Argparse solely purpose is to facilitatet that argument from a
# command-line-triggered, python script, parser the argument thus makes it
# possible from terminal to send in arguments used by the script.
# -------------------------------------------------------------------------

def main():

    # This section prepare the usage of argparse, meaning that one can through
    # terminal add arguments such as sending in info (e.g. filenamne, output, etc)

    parser = argparse.ArgumentParser(description='Parse SIE file format')

    parser.add_argument(
        '--filename', type=argparse.FileType('r'), required=True, nargs='+'
    )
    parser.add_argument(
        '--encoding', default='utf-8',
        choices=['cp850', 'latin-1', 'utf-8', 'windows-1252']
    )

    parser.add_argument('--output', required=False, help='Output CSV filename')

    parser.add_argument(
    '--debug', action='store_true', default=False, help='Display more debug'
    )

    parser.add_argument(
    '--googlesheets', required=False,
    help='Name of Google Sheets to create. Need creds.json. Note that the spreadsheet must exists and the content may be overwritten.'
    )

    args = parser.parse_args()

    # Create th empty skeleton for later.

    account_group = {
        '1': '1 - Tillgångar',
        '2': '2 - Eget kapital och skulder',
        '3': '3 - Rörelsens inkomster och intäkter',
        '4': '4 - Utgifter och kostnader förädling',
        '5': '5 - Övriga externa rörelseutgifter och kostnader',
        '6': '6 - Övriga externa rörelseutgifter och kostnader',
        '7': '7- Utgifter och kostnader för personal, avskrivningar mm.',
        '8': '8 - Finansiella och andra inkomster/intäkter och utgifter/kostnader'
    }

    print(account_group)

# Secures that function main is being run.

if __name__ == "__main__":
    main()
