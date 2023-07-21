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

def getBranches(currentList, mergeList):
    matches = re.search("##\s+branches\s*([^#]*)", mergeList, re.IGNORECASE + re.MULTILINE)

    # Strip matches by end line character and get an array of branches
    branches = [branch.strip() for branch in matches.group(1).splitlines()]

    # Remove empty branches
    branches = list(filter(None, branches))

    # percorra branches e verifique as que contém _DELETE_ no nome. Adicione em deleteBranches e remova-as de branches
    deleteBranches = []
    for branch in branches:
        if '_DELETE_' in branch:
            deleteBranches.append(branch.replace('_DELETE_', '').strip())
            branches.remove(branch)

    # Remove deleteBranches from branches
    currentList = [branch.strip() for branch in currentList.splitlines()]
    branches = [branch for branch in currentList if branch not in deleteBranches]
    print(branches)
    return

    # strip whitespaces from each branch
    return [branch.strip() for branch in branches]

try:
    command = sys.argv[0]
    currentList = sys.argv[1]
    mergeList = sys.argv[2]

    if command == 'parse-branches':
        print('\n'.join(parseBranches(currentList)))
        exit()

    if command == 'get-branches':
        getBranches(currentList, mergeList)
        # print('\n'.join(getBranches(currentList, mergeList)))
        exit()

    print('["invalid-command"]')

except IndexError as error:
    print('["error"]')