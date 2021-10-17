# basicbintree

### A basic binary tree Python library, with a simple ASCII `print_tree()`

Requires Python 3.7

This Library is good at generating the most compact ASCII representation
of a complete binary tree for illustration purposes
(which is the reason why it came into being).

An incomplete binary tree gets an ASCII representation that overlaps
the one of the corresponding complete binary tree, which is not the most
compact representation, but may still be useful for illustration purposes,
especially when showing the evolution of a tree.

Sample output:
```none
                       1
           2                       3
     4           5           6           7
  8     9    10    11    12    13    14    15
16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
```

```none
                       1
           2                       3
                 5           6           7
             10                13    14    15
            20 21             26 27            
```

Unfortunately binary trees mostly belong to the past. They are still a
valuable training tool, though, and are still fun to play with.
