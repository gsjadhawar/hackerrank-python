"""
Syntax 1
L = [variable for variable in iterable]
"""

L = [x for x in range(10)]
print(L)

"""
Syntax 2
L = [f(x) for x in iterable] 
"""
L = [x**2 for x in range(10)]
print(L)

"""
Syntax 3
L = [x for x in iterable if C(x)]
    s1 - split iterable in its constituents elements
    s2 - apply condition C on all of them and shortlist those which have satisfied the condition.
    s3 - apply the function in our case f(x) = x 
        on all the elements shortlisted in s2 and form the list out of them.
"""

L = [x for x in range(1, 21) if x % 3 == 1]
print(L)

"""
Syntax 4 
L = [f(x) for x in iterable if C(x)]
"""

L = [x**2 for x in range(1,21) if x % 3 == 1]
print(L)

"""
Syntax 5 - two variable version
L = [(x,y) for x in iter1 for y in iter2]
Evaluation : 
    S1 - Split all elements in iter1 --> tmp1
         Split all elements in iter2 --> tmp2
    S2 - Take cartesian product of tmp1 and tmp2 
         and form a list of it.
"""

L = [(x, y) for x in range(1, 5) for y in "Hello"]
print(L)


"""
Syntax 6 - 
Two Variable version 
L = [(f1(x), f2(y)) for x in iterable for y in iterable]
Evaluation:
    S1: Spilt iter1 into the constituents elements --> tmp1
        Spilt iter2 into the constituents elements --> tmp2 
    S2: apply function f1 on all elements in tmp1 --> f1_tmp1
        apply function f2 on all elements in tmp2 --> f2_tmp2 
    S3: L =  [ f1_tmp1 * f2_tmp2 ]
"""