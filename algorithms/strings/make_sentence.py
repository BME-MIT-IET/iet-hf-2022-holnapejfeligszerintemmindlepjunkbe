"""
For a given string and dictionary, how many sentences can you make from the
string, such that all the words are contained in the dictionary.

eg: for given string -> "appletablet"
"apple", "tablet"
"applet", "able", "t"
"apple", "table", "t"
"app", "let", "able", "t"

"applet", {app, let, apple, t, applet} => 3
"thing", {"thing"} -> 1
"""

"""
TODO:   This algorithm has several problem and need to be fixed.
        Problems: 
            -   It uses a global variable in a recursive function. (beacause of the bad algorthm)
            -   When it tries to count the number of the sentences in the string
                it just increases a variable, but this isn't correct here. 
            -   It only returns true value, instead of the counted value.
            -   It returns dummy value because of the algorithm implementation is bad.
            -   The algorithm is too slow, but it can be much faster.
"""

count = 0


def make_sentence(str_piece, dictionaries):
    global count
    if len(str_piece) == 0:
        return True
    for i in range(0, len(str_piece)):
        prefix, suffix = str_piece[0:i], str_piece[i:]
        if prefix in dictionaries:
            if suffix in dictionaries or make_sentence(suffix, dictionaries):
                count += 1
    return True
