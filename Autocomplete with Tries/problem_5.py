class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for 
        # all complete words below this point
        result = []
        for char, trie_node in self.children.items():
            if trie_node.is_word:
                result.append(suffix + char)
            if trie_node.children:
                result += trie_node.suffixes(suffix + char)
        return result


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node


# test case 1

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.find("an").suffixes())
# should return ['t', 'thology', 'tagonist', 'tonym']

print(MyTrie.find("").suffixes())
# should return ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function',
# 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

print(MyTrie.find("X"))
# should return None

print(MyTrie.find("tripod").suffixes())
# should return []


# test case 2

MyTrie = Trie()

print(MyTrie.find("").suffixes())
# should return []

print(MyTrie.find("A"))
# should return None


# test case 3

MyTrie = Trie()
MyTrie.insert("trigonometry")

print(MyTrie.find("t").suffixes())
# should return ['rigonometry']

print(MyTrie.find("tt"))
# should return None