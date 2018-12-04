BEGIN {
   #first_relay=1 # these values are passed by zabbix_mailflow
   #last_relay=4
   idx=-1
   eating=0
}

/^Received/ {
   eating=1
   headers[++idx]=$0
   next
}

/^[[:space:]]/ {
  if (eating)
      headers[idx] = headers[idx] $0;
   next
}

/^Subject/ {
   subject=$0
   next
}

{
   eating=0
    next
}
END {
   # get the date from the subject header
   gsub(/.*:[[:space:]]/, "", subject)

   for (i=first_relay; i<=last_relay && i<=idx; i++) {
      # spaces and tabs to 1 space
      gsub(/[ \t][ \t]*/, " ", headers[i])

      # strip all information we don't need
      gsub(/.*;[[:space:]]/, "", headers[i])
      gsub(/\(.*\)/, "", headers[i])

      # convert date in received headers to epoch
      cmd = "date +%s -d\"" headers[i] "\"";
      cmd | getline headers[i];
      close(cmd)

      # print only the difference between the subject and the headers
      printf("%s - %d\n", headers[i] - subject, i)
   }

   printf("%s - %d\n", subject, i++)
}
