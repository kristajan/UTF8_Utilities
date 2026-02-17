#!/usr/bin/env python
# coding: utf-8

# In[4]:


from IPython.display import HTML


# In[8]:


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
if __name__ == '__main__':
    import os
    MAXFILESIZE = 2 * 1024 * 1024 * 1024  # 2 Gb
    ENCODER = 'utf-8'
    limit = 60  # approximate maximum line lenth
    limitnbrlines = 1000000  # for testing to limit number of lines processed
    #path = '../../IBMAIEngineering/Course1-ML'
    #file = 'alltrans'
    path = './'
    file = 'resetpath.sh'
    infile = os.path.join(path, file)

import datetime
def prnow():  # shortcut
    print(datetime.datetime.now())


# In[2]:


# convert the byte lines to strings
# that is, when a non-readable character is encountered, 
# output it like \\u2010 or \\xe2\\x80\\x90 etc
# the str() function does this, how nice
def printplaintext(infile):
    import os
    file_size = os.path.getsize(infile)
    if file_size > ( MAXFILESIZE):
        raise IOError("printplaintext(): IOError File " + os.path.basename(infile) + " is over ", MAXFILESIZE)
        return
    outfile = f"{infile}.txt"
    plainfile = os.path.join(os.getcwd(), outfile)
    lnnbr = 0
    limitlines = limitnbrlines  # can change this for testing
    print(f"printplaintext: {infile=} {limitlines=}")
    try:
        #print("printplaintext: trying open 'rb'")
        with open(infile, 'rb') as fin:
            # count number of lines in infile and then seek back to beginning
            line_count = sum(1 for line in fin)
            fin.seek(0,0)
            print(f"printplaintext: {line_count=}")
            with open(plainfile, 'w+') as fout:
                while(lnnbr < limitlines) and (lnnbr <= line_count):
                    lnnbr += 1  # in this case, increment before trying
                    try:
                        ln = fin.readline()
                        if len(ln) == 0:
                            print(f"len(ln) is 0, so break/done, {lnnbr=}")
                            break
                        # When we do readline(), each line has an appended newline.
                        # But because we read binary, it becomes 2 chars \ and n
                        # So we need to append a real newline since we will
                        # readline() utf8 in the next function.
                        fout.write(str(ln) + '\n')
                    except Exception as e:
                        print(f"printplaintext: Exception {e=}")
                        return
    except Exception as e:
        print(f"printplaintext: Exception {e=}")
    print('printplaintext: plainfile name is ', os.path.basename(outfile))
    return(plainfile)


# In[3]:


# Read the plaintext file which has 4-7 character \xdd and \\udddd
# and replace them with estimates of what they mean.
def do_subs(text, replacements):
    # a safe way to do 1 regex at a time use a for loop, faster than many other ways
    import re
    cnt = 0
    for old, new in replacements.items():
        cnt = cnt + 1
        text = re.sub(old, new, text)
    return text

# infile is expected to be from printplaintext()
def fixnonreadables(infile):
    import os
    import re
    file_size = os.path.getsize(infile)
    if file_size > (MAXFILESIZE):
        raise IOError("fixnonreadables(): IOError File " + os.path.basename(infile) + " is over ", MAXFILESIZE)
        return
    lnnbr = 0
    limitlines = limitnbrlines  # CHANGE THIS FOR LONGER FILES
    #print(f"fixnonreadables: {infile=} {limitlines=}")
    outfile = f"{infile}.txt"
    fixedfile = os.path.join(os.getcwd(), outfile)
    # trim off binary stuff
    replacements = {r"^b'" : "" ,
        r'^b"' : "" ,
        r"\\n'$" : "" ,
        r'\\n"$' : '' ,
        r'\\\\n' : '' ,
        r"\\xe2\\x80\\x9[0-5]" : "-" ,
        r"\\xe2\\x80\\x9[6]" : "|" ,
        r"\\xe2\\x80\\x9[7]" : "_" ,
        r"\\xe2\\x80\\x9[89ab]" : "'" ,
        r"\\xe2\\x80\\x9[cdef]" : '"' ,
        r"\\xe2\\x80\\x[0-9]{2}" : '\n' ,
        r"\\xc2\\xa9" : "CR" ,  # Copyright
        r"\\x1b\[C\\x1b" : "SECTN" ,  # Section header, #1b is an escapt
        r"\\x16" : "-" ,
        r"\\x[0-9a-fA-F]{2}" : "?"  ,
        r"\\\\u201[012345]" : "-" ,
        r"\\\\u201[6]" : "|" ,
        r"\\\\u201[7]" : "_" ,
        r"\\\\u201[89ab]" : "'" ,
        r"\\\\u201[cdef]" : '"'  ,
        r"\\\\u[0-9a-fA-F]{8}" : "?" ,
        r"\\\\u[0-9a-fA-F]{4}" : "?" ,
        r"\\\\u[0-9a-fA-F]{3}" : "?" ,
        r"\\r" : '' ,
        r"\\" : '' }
    try:
        with open(infile, 'r', encoding=ENCODER) as fin:
            # count number of lines in infile and then seek back to beginning
            line_count = sum(1 for line in fin)
            fin.seek(0,0)
            print(f"fixnonreadables: {line_count=} {limitlines=}")
            with open(fixedfile, 'w+') as fout:
                while(lnnbr < limitlines) & (lnnbr <= line_count):
                    lnnbr += 1  # in this case, increment just for trying for safety
                    try:
                        ln = fin.readline()
                        newln = str(ln)  # Make it 1 long string so re can operate on it
                        # DO SUBS HERE
                        newln = do_subs(newln, replacements)
                        fout.write(newln)  # here don't need newline since readline() has it
                    except Exception as e:
                        print(f"fixnonreadables: Exception {e=}")
                        return
                ## end while
            ## end open write
        ## end open read
    except Exception as e:
        print(f"fixnonreadables: Exception {e=}")
        return
    finally:
        print('fixnonreadables: returning file ', os.path.basename(outfile))
        return fixedfile


# In[4]:


# Another problem with the transcripts is that some lines
# are very long, making it hard to read.
# So split/break very long lines into 'limit' number of characters.
# If the break is in the middle of a word, then let the line go a bit longer
# to include the whole word.  Then concatenate the remainder of the line
# that is approximately 'limit' number of chaacters onto the beginning
# of the next line, so that we don't have excess newlines.
# To find the previous word boundary would be more complicated.

# split a line, but keep the delimiters.
#https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators
def splitkeep(s, delimiter):  # Stack Overflow
   splt = s.split(delimiter)
   return [substr + delimiter for substr in splt[:-1]] + [splt[-1]]

# Split very long lines into 'limit' number of characters
# For testing or safety, in the calling code, limit the number of lines
# processed to limitnbrlines.  Here it is initialized to satisfy the global
# in the next function.
def splitlonglines(infile, limit, limitlines=limitnbrlines):
    import os
    import re
    incount = 0
    outcount = 0
    remainder = ''  # so short remaining parts of lines are concated w/ next line
    #limitlines = 10  ## for testing only process this number of lines
    #limit = 40  ## testing max length of each output line
    inputfile = os.path.basename(infile)
    print(f"splitlonglines: {inputfile=} {limit=} {limitlines=}")
    file_size = os.path.getsize(infile)
    if file_size > (MAXFILESIZE):
        raise IOError("splitlonglines(): IOError File " + os.path.basename(infile) + " is over ", MAXFILESIZE)
        return
    outfile = f"{infile}.txt"
    # Here, we could either use os.path.dirname(infile)
    # or just use current working directory
    splitfile = os.path.join(os.getcwd(), outfile)
    with open(infile, 'r', encoding=ENCODER) as f:  # Exceptions caught by system
        # count number of lines in infile and then seek back to beginning
        # to validate that the file is not too big.
        line_count = sum(1 for line in f)
        f.seek(0,0)
        print(f"splitlonglines: {line_count=}")
        inlines = f.readlines()
        print(f"splitlonglines: number of inlines = {len(inlines)=}")
    with open(splitfile, 'w+', encoding=ENCODER) as fout:  # Exceptions caught by system
        remainder = ''
        for ln in inlines:
            incount += 1
            # print(f"{len(ln)=} {incount=} {ln=}")  # for debugging short file only
            if incount > limitlines:  # for testing
                #print(f"splitlonglines: ln[limit:]={ln[limit:]=}")  # for debugging
                fout.write(remainder)  # since might have it leftover, should have \n
                outcount += 1
                break  # we are done
            # Here we will concat the remainder with the next line unless next is newline
            # This is to make it look nicer.  Otherwise there are short lines between
            # the limit length lines.
            if not ln.strip():  # test for blank line
                if len(remainder) > 1:   # it is blank
                    # write the last part of the line by itself with the new \n line
                    # print(f"{len(ln)=} {incount=} {ln=}")  # debugging
                    fout.write(remainder + ln)  # keep the blank line
                    outcount += 1
                    remainder = ''
                    continue  # next line 
                else:  # keep the blank line
                    fout.write(ln)
                    outcount += 1
                    continue  # next line
            else:  # not a blank line
                if len(remainder) > 1: 
                    # still in the loop, concat rest of line to next line
                    # This is to make it look nicer.  Otherwise there are short lines between
                    # the limit length lines.
                    ln = remainder[:-1] + ' ' + ln  # remove \n from remainder & concat
                    #print(f"{len(ln)=} {incount=} {ln=}")
                    remainder = ''
            while len(ln) > limit:  ## the max lenth of each line plus or minus 1 word
                #print(f"{len(ln)=} {incount=} {ln=}")
                match = re.search(r'[\S]+[\s]' , ln[limit:])  # word boundary and word start
                if match:
                    #print(f"splitlonglines:start={match.start()=} end={match.end()=}") #testing
                    newlim = match.end() + limit
                else:
                    newlim = limit
                #print(f"splitlonglines: {newlim=}")  # for testing short file only
                outline = ln[0:newlim]
                fout.write(outline + '\n')  # must add newline here
                outcount += 1
                #print(f"len of outline = {len(outline)=}")  # for debugging only
                #print( "splitlonglines: 0123456789 123456789 123456789 123456789 1234567890 123456789 12345678")
                #print(f"splitlonglines: {outline}")
                ln = ln[newlim:]  # cut out the matched part of the line
            remainder = ln  # we will concat to front of next line, might seem to throw off counts
        if len(remainder) > 0:  # last part of text in the file
            fout.write(remainder)  # here there is still a newline at the end already
            outcount += 1
    print(f"splitlonglines: {incount=} {outcount=} approximate, may reflect some joins")
    print("splitlonglines: returning output file ", os.path.basename(outfile))
    fout.close()
    return splitfile


# In[5]:


# Some of converting unreadable bytes may have left blank lines
# so remove most of them.
def cleanexcessblanklines(infile):
    import os
    import re
    file_size = os.path.getsize(infile)
    if file_size > (MAXFILESIZE):
        raise IOError("cleanexcessblanklines(): IOError File " + os.path.baename(infile) + " is over ", MAXFILESIZE)
        return
    lnnbr = 0
    outcount = 0
    # calling code should set limitnbrlines as a global.
    limitlines = limitnbrlines  # make this short for testing
    ln = ''
    outfile = f"{infile}.txt"
    cleanfile = os.path.join(os.getcwd(), outfile)
    try:
        with open(infile, 'r', encoding=ENCODER) as fin:
            line_count = sum(1 for line in fin)  # count number of lines and seek back to beginning
            fin.seek(0,0)
            print(f"cleanexcessblanklines: {line_count=} {limitlines=} set by calling code!!!")
            lastlineblank = 0  # a flag
            with open(cleanfile, 'w+') as fout:
                while(lnnbr <= limitlines) & (lnnbr <= line_count):
                    lnnbr += 1  # in this case, increment just for trying for safety
                    if lnnbr > limitlines:
                        print('cleanexcessblanklines: done limitlines = ', limitlines)
                        break  # done
                    try:
                        ln = fin.readline()
                        newln = str(ln)  # must be string so re can operate on it or strip
                        if not newln.strip():  # still a blank line
                            if lastlineblank == 1:  # skip it
                                continue
                            else:  # write it and set flag
                                fout.write(newln)
                                outcount += 1
                                lastlineblank = 1
                        else:
                            fout.write(newln)
                            outcount += 1
                            lastlineblank = 0
                    except Exception as e:
                        print(f"cleanexcessblanklines: Exception {e=}")
                        return
    except Exception as e:
        print(f"cleanexcessblanklines: Exception {e=}")
    print(f"cleanexcessblanklines: {lnnbr=} {outcount=} returning file ", os.path.basename(outfile))
    return cleanfile


# In[ ]:


# The problem with transcripts file is unicode types of newlines, or literal backslashes
# Mostly in the range \u2010 to \u201f may also appear as \\xe2\\x80\\x9[0-0a-f]
# Other undecodable bytes are changed to newlines.
if __name__ == '__main__':
    import os
    import time
    get_ipython().system('python --version')
    prnow()

    MAXFILESIZE = 2 * 1024 * 1024 * 1024  # 2 Gb
    ENCODER = 'utf-8'
    #path = '../../IBMAIEngineering/Course1-ML'
    #file = 'alltrans'
    path = './'
    file = 'testin.txt'
    infile = os.path.join(path, file)
    limit = 60  # approximate maximum line lenth
    limitnbrlines = 1000000  # for testing to limit number of lines processed

    numslist = []  # in future, this will collect err nbrs for UnicodeDecodeError if we run readdecode
    plainfile = printplaintext(infile)
    time.sleep(0.1)  # make sure each file is written in order
    fixedfile = fixnonreadables(plainfile)
    time.sleep(0.1)  # make sure each file is written in order
    splitfile = splitlonglines(fixedfile, limit, limitnbrlines)
    time.sleep(0.1)  # make sure each file is written in order
    cleanfile = cleanexcessblanklines(splitfile)
    # After printplaintext(), or that plus fixdecodeerror()
    # run findbackslash to see line numbers having backslashes
    myfile = findbackslash(plainfile)
    myfile = findbackslash(fixedfile)
    prnow()

