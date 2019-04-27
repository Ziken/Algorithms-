# Longest Common Sequence
### Complexity
    O(n*m)
### Functions
#### find_longest_subsequence
Function follows the directions and when sign is marked as found, append to current sequence.

#### find_all_longest_seqs
For sequences "ADBECF" and "DEFABC", the result is `['DEF', 'DEC', 'DBC', 'ABC']`

It starts from the end of the list `self.directions`, then looking for nearest signs that is marked as found. Next step is to append this character to `current_subsequence` and repeat until no signs are found which means that we have longest possible sequence. Append it and repeat. It is working based on graph (more or less). 