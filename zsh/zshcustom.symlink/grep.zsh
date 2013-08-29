grep_() { grep $@ -r -i -I --color='always' * }
find_() { find ./ -name "*$@*" }
