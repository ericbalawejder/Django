#!/usr/bin/env python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "progsite.settings")
from logins.models import Fail

import pprint, re, datetime
import support

# get object for pretty-printing the entries
pp = pprint.PrettyPrinter()

# in debugging mode print out lots of extra information
debug = False

# this is the regular expression used for the initial filter
# done by support.getFileLines
filter_expr = ":\s(Failed|Accepted)\s(password|none)"

# this is a regular expression used to match the lines in order
# to extract information
line_expr = r"(\w+\s\d+\s\d+.\d+.\d+) yosemite sshd\[(\d+)\]. (Failed|Accepted) password for (invalid user \w*|\w*) from (\d+.\d+.\d+.\d+)"
line_pattern = re.compile(line_expr)

# get a log file

# use this file for development
#log_file = "auth.log.test"
log_file = "/var/log/auth.log"

# now start processing the log file
print "\n==> processing: {} on {}".format( log_file, datetime.datetime.now() )

# failed entries, a dict with key = ssh process id
entries = {}

# get filtered lines
lines = support.getFileLines( log_file, filter_expr )

for line in lines:
    if debug: print line # debugging only
    
    result = line_pattern.match(line)
    
    access = result.group(1)
    time = support.logtime2datetime(access)
    
    pid = result.group(2)
    
    status = result.group(3)
     
    login = result.group(4)
    if "invalid user" in login:
        realUser = login.split()
        login = realUser[2]

    
    ip = result.group(5)
    
    if pid not in entries:
        entries[pid] = (time, login, ip)
    
    # Remove the entry for pid if you discover "Accepted" status
    if pid in entries and status == "Accepted":
        entries.pop(pid, None)    

if debug: pp.pprint(entries)

if debug: print "\nadd new entries into database\n"

# Loop through entries, adding "new" ones to the database, wherea access time becomes
# the initiated field
for pid in entries: 
    entry = Fail(initiated = entries[pid][0], login = entries[pid][1], ip = entries[pid][2])
    try:
        entry.save()
        print "new entry: " + str(entries[pid])
    except Exception as err:
        print err
