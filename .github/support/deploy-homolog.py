import sys
import re

errors = []

def parseBranches(payload):
    matches = re.search("##\s+branches\s*([^#]*)", payload, re.IGNORECASE + re.MULTILINE)

    # Strip matches by end line character and get an array of branches
    branches = [branch.strip() for branch in matches.group(1).splitlines()]

    # Remove empty branches
    branches = list(filter(None, branches))

    # strip whitespaces from each branch
    return [branch.strip() for branch in branches]

try:
    command = sys.argv[1]
    payload = sys.argv[2]

    if command == 'parse-branches':
        print('\n'.join(parseBranches(payload)))
        exit()

    print('["invalid-command"]')

except IndexError as error:
    print('["error"]')
