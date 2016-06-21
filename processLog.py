#!/usr/bin/env python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "progsite.settings")
from logins.models import Fail

import pprint, re, datetime
import support

# get object for pretty-printing the entries
pp = pprint.PrettyPrinter()

# in debugging mode print out lots of extra information
debug = True

# this is the regular expression used for the initial filter
# done by support.getFileLines
filter_expr = ":\s(Failed|Accepted)\s(password|none)"

# this is a regular expression used to match the lines in order
# to extract information
# line_expr = r"....."
# line_pattern = re.compile(line_expr)

# get a log file

# use this file for development
log_file = "auth.log.test"

# now start processing the log file

print "\n==> processing: {} on {}".format( log_file, datetime.datetime.now() )

# failed entries, a dict with key = ssh process id
entries = {}

# get filtered lines
lines = support.getFileLines( log_file, filter_expr )

for line in lines:
    if debug: print line # debugging only

    '''
    Use line_patteren to extract from each filtered line the following:

       access = the time stamp at the begining of the line
		(apply support.logtime2datetime to extracted string)
       status = "Accepted" or "Failed"
       pid    = the sshd process id
       login  = the login (assume no internal blanks)
       ip     = the ip address

    You want to do this first time only:

       entries[pid] = (access, login, ip)

    Delete the entry for pid if you discover "Accepted" status
    '''

if debug: pp.pprint(entries)

if debug: print "\nadd new entries into database\n"

'''
Loop through entries , adding "new" ones into the database, where access time becomes
the initiated field.

The uniqueness of the initiated field prevents duplicate entries

print any new entries, one per line, in format like:
    new entry: ( initiated, login, ip)

in debugging mode, print other information to help
''' 

print "hello"

