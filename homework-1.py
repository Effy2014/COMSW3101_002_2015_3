
# coding: utf-8

# # Introduction to Python - Homework #1
# - Due Friday 9/18 at 1:45
# - Submit on Courseworks - do not email

# # Academic Honesty
# * The computer science department has strict polices. Check
# the department [web page](http://www.cs.columbia.edu/education/honesty) for details. 
# - Do not look at anybody else's source code. Do not show anybody
# your source, or leave your source where somebody could see it.
# You MUST write your own code.
# - For this class, feel free to discuss issues with other people, but suggest waiting an hour or two after a discussion, before writing your code.
# -  Cases of non original source will be refered to the Judical Committee.
# 

# # Tips
# 

# - Make SURE you are running Python 3.4, and not 2.7

# In[1]:

# the 3.4.3 is the version
import sys
sys.version


# - isinstance

# In[2]:

# 'isinstance' is a little more concise then 'type' in some situations
type(234) == int
isinstance(234, int)


# - 'list' will force a lazy eval
# 

# In[3]:

e = enumerate(['a','b','c'])
print(e)
list(e)


# - Lazy function types
# - the 'type' of a lazy function's output is the name of the function

# In[4]:

[isinstance(range(10), range), isinstance(zip([0,1,2]),zip)]


# - a common way to recurse thru a nested list is to split the list into the 0th element, and the rest of the list. 'rcount' shows an example

# In[5]:

# count the number of elements in a nested list
def rcount(l):
    if l == []:
        return(0)
    if isinstance(l, list):
        return rcount(l[0]) + rcount(l[1:])
    else:
        # not a list
        return(1)

rcount([3,4,[3,4,[4,2,3],3],3])


# - can set multiple vars from a list or tuple

# In[6]:

x, y, z = [1,2,3]
x


# In[7]:

z


# # Problem 1a
# - write a function(dp) that computes standard 'dot products' 
# - example: dp([1,2,3], [4,5,6]) = $$1 * 4 + 2 * 5 + 3 * 6 = 32$$
# - if one vector is longer than the other, the extra elements on the right are ignored

# In[22]:

def dp(tv0, tv1):
    sum = 0 
    for i in list(range(min(len(tv0), len(tv1)))):
        sum += tv0[i]*tv1[i]
    return sum


# In[23]:

# test vectors for Problem 1 a,b,c,d
tv0 = [1,2,3]
tv1 = [4,5,6,7,8,9]


# In[24]:

# the 7,8,9 elements are ignored
dp(tv0, tv1)


# # Problem 1b
# - write 'shortlong', a function that takes two vectors, and returns in a list the short vector, the short vector length, the long vector, and the long vector length

# In[30]:

def shortlong(tv0, tv1):
    if len(tv0) == min(len(tv0), len(tv1)):
        return [tv0, len(tv0), tv1, len(tv1)]
    else:
        return [tv1, len(tv1), tv0, len(tv0)]


# In[31]:

shortlong(tv0, tv1)


# In[32]:

shortlong(tv1, tv0)


# # Problem 1c
# - write a more flexible version of dp, 'odp'
# - odp takes an extra 'offset' arg, which moves the shorter vector to the right
# - odp(tv0, tv1, 2) = $$1 * 6 + 2 * 7 + 3 * 8 = 44$$
# - use 'shortlong'

# In[47]:

def odp(tv0, tv1, const):
    List = shortlong(tv0, tv1)
    tv0new = List[0]
    tv1new = List[2]
    sum = 0
    for i in range(min(len(tv0), len(tv1))):
        sum += tv0new[i]*tv1new[i+const]
    return sum


# In[48]:

[odp(tv0, tv1, 0), odp(tv0, tv1, 1), odp(tv0, tv1, 2)]


# # Problem 1d
# - another version of dp, 'pdp' 
# - pdp takes a pad arg
# - if one vector is shorter, it is padded on the right with the pad value
# - pdp(tv0, tv1,1) = dp([1,2,3,1,1,1], [4,5,6,7,8,9])
# - use 'shortlong'

# In[67]:

def pdp(tv0, tv1, const):
    List = shortlong(tv0, tv1)
    tv0new = List[0]
    tv1new = List[2]
    sum = 0
    for i in range(len(tv1new)):
        if i < len(tv0new):  
            sum += tv0new[i]*tv1new[i]
        else:
            sum += tv1new[i]*const
    return sum
tv0 = [1,2,3]
tv1 = [4,5,6,7,8,9]


# In[68]:

[pdp(tv0, tv1, 0), pdp(tv0, tv1, 1), pdp(tv0, tv1,2)]


# # Problem 2
# - write a run length encoder
# - convert a list into a list of [val, numberOfRepeats]

# In[3]:

def rle(List):
    if List == []:
        return []
    else:
        Set = set(List)
        L = []
        for e in Set:
            count = 0
            while e in List:
                count +=1
                List.remove(e)
            L.append([e, count])
        return L


# In[4]:

rle([])


# In[5]:

rle([5])


# In[6]:

rle([2,2])


# In[7]:

rle([1,2])


# In[8]:

rle([10,10,20,33,33,33,33,10,1,30,30,7])


# # Problem 3
# - write a function(partition), that divides a list into segments
# - arg 'l' is the input list
# - arg 'n' is the length of each segment. if there are not enough list elements to make a final segment of length n, they are discarded
# - arg 'overlap' is how many list elements should overlap btw adjacent segments
# - remember range is range(inclusive, exclusive), range[0,2] => [0,1]

# In[137]:

def partition(l, n, overlap=None):
    if overlap == None:
        overlap = 0
    total = (len(l)-n) // (n-overlap) +1
    L = []
    for i in list(range(total)):
        L.append(l[i*(n-overlap):n+i*(n-overlap)])
    return L
        


# In[132]:

partition(range(10),2, 0)


# In[133]:

partition(list(range(10)), 2, 0)


# In[134]:

partition(list(range(10)),2, 0)


# In[135]:

partition(list(range(10)),2,1)


# In[138]:

partition(list(range(10)),4)


# In[31]:

partition(list(range(10)),4,3)


# In[32]:

partition(range(10),4,3)


# # Problem 4a
# - write 'expandlazy' - if given a 'lazy' range, zip, or enumerate, expand it into a list
# - non lazy values are returned unchanged
# 

# In[80]:

expandlazy = lambda x: x if type(x) is int or type(x) is str else list(x)


# In[81]:

[expandlazy(234), expandlazy(range(3)), expandlazy('asdf'), expandlazy(enumerate(['a','b','c']))]


# # Problem 4b
# - write 'expandlazylist' - expand any lazy elements of a list

# In[125]:

def expandlazylist(x):
    L = []
    for i in x:
        if type(i) is int or type(i) is  str:
            L.append(i)
        else:
            L.append(list(i))
    return L


# In[126]:

ll = [1,2,3, range(4), 5, zip([1,2,3], [4,5]), 'asdf', enumerate(['a', 'b', 'c'])]
ll


# In[127]:

expandlazylist(ll)


# # Problem 5
# - 'flatten' turns a nested list into a linear one
# - use recursion like 'rcount' above
# - one way to think about it is it 'erases' all the brackets, except the two outermost ones
# 

# In[49]:

flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]


# In[50]:

flatten( [1,[2,3,4,[5,6,[7,8],9],11]])


# In[51]:

flatten([1,2,3,[4,56],[44,55],7,8])

