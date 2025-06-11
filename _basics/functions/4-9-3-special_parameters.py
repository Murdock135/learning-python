"""
The symbols '/' and '*' can be used to indicate what type of argument 
(positional or keyword or both) is allowed for a particular argument.
- Arguments before / are positional (order matters)
- Arguments after * are keyword only.

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
"""

def func1(arg1, arg2, /):
    print(arg1, arg2)
    
func1('b','a')
func1('a', 'b')

