help and usage message:
    python matcher.py -h

example usages and outputs:
    $ python matcher.py KMP pokopokpopk ok
    [1, 5]

    $ python matcher.py FA "mo @#%* &^% 3 {}" " "
    [2, 7, 11, 13]