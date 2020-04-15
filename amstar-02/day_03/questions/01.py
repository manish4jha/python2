## ------- Question {Sathish Kumar}
## difference between union and zip


>>> 
>>> 
>>> s1 = {'red', 'green', 'blue' }
>>> s2 = {'black', 'white', 'grey' }
>>> s1.union(s2)
{'black', 'white', 'green', 'grey', 'blue', 'red'}
>>> s1 | s2
{'black', 'white', 'green', 'grey', 'blue', 'red'}
>>> list(zip(s1, s2))
[('blue', 'black'), ('green', 'white'), ('red', 'grey')]
>>> s1
{'blue', 'green', 'red'}
>>> s2
{'black', 'white', 'grey'}
>>> 
