#!/usr/bin/python3

# Entry-point for running from the CLI when not installed via Pip, Pip will handle the console_scripts entry_points's from setup.py
# It's recommended to use `pip3 install changedetection.io` and start with `changedetection.py` instead, it will be linkd to your global path.
# or Docker.
# Read more https://github.com/dgtlmoon/changedetection.io/wiki

from mb_changedetectionio import mb_changedetection

if __name__ == '__main__':
    mb_changedetection.main()
