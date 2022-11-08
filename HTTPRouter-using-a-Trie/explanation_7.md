# Explanation & time and space complexity analysis

## RouteTrieNode:
### init method
Time complexity is constant O(1)
Space complexity is constant O(1)

### insert method
Time complexity of insert is the same as it's for set method for python dict.
So in average case it's O(1), and O(n) in amortized worst case. 

Space complexity is constant O(1).


## RootTrie:

### init method
Time complexity is constant O(1)
Space complexity is constant O(1)

### insert method
Time complexity in worst case is O(m * n), where m is number of parts in path and
n is number of nodes in trie. We iterate through all parts in path and use "in"
operation in the loop to check if given part is in children of given node.
The insert method also contains calling insert in RouteTrieNode, which is responsible
for adding element to the dict. We can approximate time complexity of this to O(1),
because O(n) happens only for amortized worst case. 

Space complexity is O(1), I keep only info about current node, so space complexity
is constant.

### find method
Time complexity in worst case is O(m * n), where m is number of parts in path and
n is number of nodes in trie. We iterate through all parts in path and use "in"
operation in the loop to check if given part is not in children of given node.

Space complexity is O(1), I keep only info about current node, so space complexity
is constant.



## Router:

### init method
Time complexity is constant O(1)
Space complexity is constant O(1)

### add_handler method
Here split_paths and insert from RootTrie is used. So it could be also summarized to 
O(m * n), where m is number of parts in path and n is number of nodes in trie

### lookup method
Here split_paths and find from RootTrie is used. So it could be summarized to
O(m * n), where m is number of parts in path and n is number of nodes in trie

### split_paths method
Time complexity is O(n), all elements must be checked to split string.

Space complexity is O(n) in worst case, for almost each element new list item will be 
created.
