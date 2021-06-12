# function returns 2D array, so consider that when setting base cases





#[],  zero ways to create hello
print(allConstruct('hello', ['cat', 'dog', 'mouse']))  

#[[]],  1 way to create  '', which is taking a empty []
print(allConstruct('', ['cat', 'dog', 'mouse']))   #[[]]