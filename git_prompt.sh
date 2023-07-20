cl_none="\e[m"
cl_red="\e[0;31m"
cl_green="\e[0;32m"
cl_yellow="\e[0;93m"
cl_orange="\e[0;33m"
cl_blue="\e[0;34m"
cl_cyan="\e[36m"
cl_bg="\e[37;42m"

pointer=$(printf '\xe2\x86\x92\x20')

computer_name="\h"
username="\u"
currentdir="\w"
linebreak="\n"

function git_prompt_info() {
   if [ ! -d "./.git" ]; then
      printf "`whoami`:"
      return
   fi

    branch=`git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'`
    origin=`git branch -r | grep -oh origin/$branch`
    result=''

    if [ "$branch" != '' ]; then
        sp="\x20"

        result="${cl_orange}[${branch}"

        if [ "$origin" != '' ]; then
            behind=`git rev-list --count HEAD..origin/${branch}`
            ahead=`git rev-list --count origin/${branch}..HEAD`

            if [ "$behind" != "0" ]; then
                result="${result}${sp}${cl_red}\xE2\x87\xA3${behind}${cl_none}"
            fi

            if [ "$ahead" != "0" ]; then
                result="${result}${sp}${cl_none}\xE2\x87\xA1${ahead}"
            fi

            if [ "$behind $ahead" = "0 0" ]; then
                result="${result}${sp}${cl_green}\xE2\x9C\x94${cl_none}"
            fi
        fi

        diffs=`git status --porcelain | wc -l`

        if [ "${diffs}" != "0" ]; then
            result="${result}${sp}${cl_red}\xE2\x8b\x86${diffs}${cl_none}"
        fi

        result="${result}${cl_orange}]${cl_none}${sp}"
    fi

    if [ "$result" != "" ]
    then
        printf $result
    fi
}

gitinfo=$(git_prompt_info)

PS1="${linebreak}${gitinfo}${cl_cyan}${currentdir}${cl_none}${linebreak}${pointer}"
PROMPT_FULL=$PS1
PROMPT_SIMPLE="${linebreak}${gitinfo}${linebreak}${pointer}"
