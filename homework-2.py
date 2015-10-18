
# coding: utf-8

# # Introduction to Python
# # Homework #2
# # Due Friday, Sept 25, 1:45pm in Courseworks

# # Academic Honesty
# * The computer science department has strict polices. Check
# the department [web page](http://www.cs.columbia.edu/education/honesty) for details. 
# - Do not look at anybody else's source code. Do not show anybody
# your source, or leave your source where somebody could see it.
# You MUST write your own code.
# - For this class, feel free to discuss issues with other people, but suggest waiting an hour or two after a discussion, before writing your code.
# -  Cases of non original source will be refered to the Judical Committee.
# 
# 

# ## Tips

# ### Generators

# In[139]:

# you can terminate a generator by using 'return',
# or falling off the end of the generator
def g1():
    yield(1)
    yield(2)
    return
    yield(3)

def g2():
    yield(1)
    yield(2)

# an easy way to get the elements from a 
# FINITE length generator will return is to use 'list'
print(list(g1()))
print(list(g2()))       


# In[140]:

# if a generator calls a 2nd generator for elements, 
# and the 2nd generator finishes, the 1st one will finish as well
def g3(g):
    while True:
        yield(next(g))

for i in g3(g2()):
    print(i)


# ### String

# In[40]:

# split will "tokenize", and get rid of white space

' foo     bar zip         zap  '.split()


# In[51]:

# replace can remove unwanted chars
'dont, want, the, commas,'.replace(',','')


# In[65]:

# convert strings to numbers

[int('2343'), float('2.34')]


# ### Arithmetic

# In[1]:

# integer quotient, integer remainder, floating divide
[14//5, 14 % 5, 14 / 5]


# In[149]:

# 'bin' function converts an int into a binary string
[bin(11), bin(234)]


# In[24]:

# 1 and 0 function as True and False in an 'if' statement
[True if 1 else False, True if 0 else False]


# # Problem 1a - decimals
# - define a 'decimals' generator function, that 'generates' the decimal digits of 1/n, where n is an integer greater than 1
# - if the decimal expansion terminates, like 1/8 = .125, the generator should terminate. otherwise, like for 1/3=.333..., the generator should never stop
# - use long division to compute the expansion - it is very simple

# In[5]:

def decimals(n):
    result = 1 / n
    show = str(result)[2:]
    for i in show:
        yield(int(i))


# In[6]:

list(decimals(8))


# In[7]:

d = decimals(3)
[next(d) for x in range(10)]


# # Problem 1b - genlimit
# - define 'genlimit(g, limit)', which generates at most 'limit' number of values from a generator 'g'

# In[51]:

def genlimit(g, limit):
    for i in range(limit):
        yield(next(g))


# In[52]:

print(list(genlimit(decimals(3), 5)))
print(list(genlimit(decimals(8), 5)))


# # Problem 2 - Deal With Repeated Decimals
# - genlimit is useful, but never sure what we're missing with an arbitrary limit
# - since 1/n is a rational number, its decimal expansion must eventually repeat(unlike irrational numbers like PI)
# - write 'decimals2', a variant of 'decimals' 
# - if the decimal expansion is finite, it should just return the finite set of digits
# - if the decimal expansion repeats, it should return the digits up to the point it starts repeating. then the final yield should be the repeating sequence of digits
# 

# In[74]:

import textwrap
def decimals2(n):
    llist = []
    ilist = []
    l2list = []
    i2list = []
    count = 1
    l = 10 // n
    i = 10 % n
    while (i not in ilist or (l not in llist and i !=0)):
        llist.append(l)
        ilist.append(i)
        l = i * 10 // n
        i = i * 10 % n
    while (i not in i2list and i):
        l2list.append(l)
        i2list.append(i)
        l = i * 10 // n
        i = i * 10 % n
    if l2list:
        llist.append(l2list)
    return(llist)
        
    

for j in range(2, 30): 
    # ugly hack needed because lines don't wrap in pdf version
    d = list(decimals2(j))
    print('   Expansion of 1/' + str(j) + ':')
    print( textwrap.fill(str(d), 80))


# # Problem 3a - select
# - define a function 'select(l, selectors)', where 'l' and 'selectors' lists of the same length
# - 'select' returns new list which consists of the elements of l that have a True value in the corresponding selectors element

# In[59]:

def select(l, selector):
    newlist = []
    for i in range(len(l)):
        if selector[i]:
            newlist.append(l[i])
    return(newlist)


# In[60]:

select(range(5), [0, 1, '', "foo", True])


# # Problem 3b - nbitIntToDigits
# - define a function 'nbitIntToDigits(i, n)'
# - returns a list of the digits(ints, not strings) in a binary representation of 'i'
# - pad with '0's on the left if needed to generate n bits

# In[61]:

def nbitIntToDigits(i,n):
    List = []
    temp = bin(i)
    length = len(temp)-2
    if length < n:
        List = [0] * (n-length)
    for k in temp[2:]:
        List.append(int(k))
    return(List)


# In[62]:

[nbitIntToDigits(3, 2), nbitIntToDigits(3, 6), nbitIntToDigits(11, 4)]


# # Problem 3c - powerSet
# - define a function 'powerSets(l)' that returns all possible subsets of 
# the elements of l, including the empty list and the original list
# - for a list of length n, how many elements are in the powerSet list?
# 

# In[39]:

import itertools
def powerSet(l):
    List = []
    for i in range(len(l)+1):
        ll = itertools.combinations(l, i)
        for ii in ll:
            List.append(list(ii))
    return(List)


# In[40]:

powerSet(['avery', 'math', 'butler'])


# In[41]:

powerSet(['avery', 'math', 'butler', 'dodge'])


# # Problem 4 - Decrypting Government Data
# - Your job is to summarize this gov data about oil consumation
# - The format of the file rather bizzare - note that each line has data
# for two months, in two different years! (Plus I had to edit the file to make it parseable)
# - Fortunately, Python is great for untangling and manipulating data.
# - Write a generator that produces a summary line for a year's data on each 'next' call
# - The generator should read the lines of the oil file in a lazy fashion - it
# should only read 13 lines for every two years of output. Note a loop can have
# any number of 'yield' calls in it.
# - Your generator probably wants to throw away the first 7 lines when it starts.
# - The summary line produced should include the total consumption over the year(sum up
# the per month consumption), and the min, max, and avg price for the year.
# - In addition to the 'oil' generator function, my solution had a separate helper function, 'report' 
# to make the summary string:
# 
# 
# - def report(years, data, leftside):
#     - years is the two years the 13 lines cover, like ['2014', '2013']
#     - data is the 13 lines covering two years
#     - leftside is True if i'm extracting the 'left' half of the data,
# false if extracting from the right. 
# 
# - Download the 'oil.txt' file from Courseworks/week2

# In[175]:

def oil(path):
    with open(path) as f:
        years = []
        for _ in range(7):
            next(f)
        lines = f.readlines()
        ll = lines[1]
        for i in range(0, len(lines), 14):
            flag = lines[i].split()
            years += flag
        List = []
        Left = []
        Total = []
        count = 0 
        while count < (len(years)):
            if count % 2 == 0:
                temp = lines[1].split()
                total = int(temp[1].replace(',',''))
                for line in range(2,14):
                    ll = lines[line].split()
                    left = ll[5]
                    List.append(left)
                List = list(map(float, List))
                Max = max(List)
                Min = min(List)
                Ave = sum(List)/len(List)
                Text = "%s: quan: total=%d prices: max = %f min = %f avg = %f" %(years[count], total, Max, Min, Ave)
                count += 1
            else:
                temp = lines[1].split()
                total = int(temp[8].replace(',',''))
                for line in range(2,14):
                    ll = lines[line].split()
                    right = ll[12]
                    List.append(right)
                List = list(map(float, List))
                Max = max(List)
                Min = min(List)
                Ave = sum(List)/len(List)
                Text = "%s: quan: total=%d prices: max = %f min = %f avg = %f" %(years[count], total, Max, Min, Ave)
                count += 1
                lines = lines[14:]
            
            yield(Text)


# In[176]:

# change this path to where you put 'oil.txt' on your machine
path = '/Users/XW/Desktop/python/oil.txt'
o = oil(path)


# In[177]:

next(o)


# In[178]:

next(o)


# In[179]:

next(o)


# In[180]:

for s in list(o):
    print(s)


# # Problem 5a - countBases
# - define 'countBases(dna)' - returns the number of 'A', 'C', 'G', 'T' in a DNA strand

# In[49]:

import re
def countBases(dna):
    bases = 'ACGT'
    List = []
    for i in bases:
        rec=re.compile(i)
        l = rec.findall(dna)
        List.append(len(l))
    return(List)


# In[50]:

bases = 'ACGT'
dna = 'CATCGATATCTCTGAGTGCAC'


# In[51]:

countBases('AC')


# In[52]:

countBases(dna)


# # Problem 5b - reverseComplement
# - define 'reverseComplement(dna)' 
# - swaps A <-> T, C <-> G, and returns the new DNA in reverse order

# In[67]:

def reverseComplement(dna):
    List = ''
    for i in dna:
        if i == 'A':
            i = 'T'
        elif i == 'T':
            i = 'A'
        elif i == 'C':
            i = 'G'
        elif i == 'G':
            i = 'C'
        List += i
    l = List[::-1]
    return(l)


# In[68]:

reverseComplement('ACGT')


# In[69]:

reverseComplement(dna)

