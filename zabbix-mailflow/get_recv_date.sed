sed -n '/Mon\|Tue\|Wed\|Thu\|Fri\|Sat\|Sun/{; s/.*;[[:space:]]*\(.*\)/\1/; s/\(.*\)(.*)/\1/;p}'
