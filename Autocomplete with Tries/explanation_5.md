# Time and space complexity analysis


## TrieNode:
### insert method
Time complexity of insert is the same as it's for set method for python dict.
So in average case it's O(1), and O(n) in amortized worst case. 

Space complexity is constant O(1).

### suffixes method
Time complexity is O(n), where n is number of children and children of sub_nodes
of given node.

Space complexity in worst case is O(n), where n is number of children and children of sub_nodes
of given node. In the worst case all items we check turns out to be a suffix.

## Trie:
### insert method
Time complexity in worst case is O(m * n), where m is number of chars in word and
n is number of nodes in trie. We iterate through all chars in word and use "in"
operation in the loop to check if given char is in children of given node.
The insert method also contains calling insert in TrieNode, which is responsible
for add element to the dict. We can approximate time complexity of this to O(1),
because O(n) happens only for amortized worst case. 

Space complexity is O(1), I keep only info about current node, so space complexity
is constant.

### find method
Time complexity in worst case is O(m * n), where m is number of chars in word and
n is number of nodes in trie. We iterate through all chars in word and use "in"
operation in the loop to check if given char is not in children of given node.

Space complexity is O(1), I keep only info about current node, so space complexity
is constant.
