BEGIN { FS="\t"
	max=0
} {
	if($2 == "" && $3 != "") {
		vals=key=$3
		gsub(/ .*/, "", key)

		if(!features[key])
			features[key] = ++max

		idx=features[key]

		nr=split(vals, tokens, " ")
		for(i=0; i<nr; i++) {
			if(tokens[i] == "count:" || tokens[i] == "inuse:") {
				values[idx, tokens[i]] += tokens[i+1]
			}
		}
	}
} END {
	for(key in features) {
		printf("%d,%d\n",
			values[features[key], "count:"],
			values[features[key], "inuse:"]) > key
	}
}
