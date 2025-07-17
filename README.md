# UTF8_Utilities
# Problem: Some files are mostly utf8 but have some sequences
# that are not readable with utf8 decoders.
# The functions below try to change the sequences into newlines or - or quotes, etc
# in 2 steps, 1. printplaintext() and 2. fixnonreadables()
# Then there are optional functions to split long lines, clean up, and
# write a file with just those line numbers that have unreadable characters.
#
# There are 3 ways to run:
# 1. a. In cell # [6] marked __main__ set the input file name, limit, 
#       limitnbrlines, and MAXFILESIZE.
#    b. Run all the cells above it (1-5) and it.
#    c. Look at the files with .txt appended to your file name in your directory.
#
# 2. a. In the cell # [9] set your input file name at the bottom and run readdecode() with it.
#    b1. Look at the output comments.  Add any encodings you want to try,
#    b2. or Write a line to run runfixundecodables() with your file name.
#    c. Look at the files with .txt appended to your file name in your directory.
#
# 3. You can run just the first few functions, skip splitlonglines()
#    and then run cleanexcessblanklines(), after setting input file name, limit, 
#    limitnbrlines, and MAXFILESIZE.
#
# 4. At the end of this file, see findbadbytes() and writelineandbytenbrs()
#
# Security is helped by printing os.path.basename(file) instead of full path name
#                       not having unvalidated user input in print statements
#                       checking os.path.getsize(file) for a file > MAXFILESIZE Gb
#                       For longer files, change MAXFILESIZE below to a larger number.
#
# These initializations OVER-RIDE CELL - I NEED TO FIX THIS
# Globally used variables:
