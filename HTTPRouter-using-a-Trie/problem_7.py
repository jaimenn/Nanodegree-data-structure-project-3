"""
Solution of;
Project: Problems vs Algorithms
Problem 7: Request Routing in a Web Server with a Trie
"""

# A RouteTrie will store our routes and their associated handlers


class RouteTrie:

    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root
        # path or home page node
        self.root = RouteTrieNode()

    def insert(self, path):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of
        # this path
        path_list = split_path(path)

        current_node = self.root

        for page in path_list:
            if page not in current_node.children:
                current_node.insert(page)

            current_node = current_node.children[page]

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        path_list = split_path(path)
        current_node = self.root

        for page in path_list:
            if page not in current_node.children:
                return None

            current_node = current_node.children[page]

        return current_node.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one
# additional element, a handler.
class RouteTrieNode:

    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, page):
        # Insert the node as before
        self.children[page] = RouteTrieNode()


# The Router class will wrap the Trie and handle
class Router:

    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as
        # well!
        self.root = RouteTrieNode()
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler_data):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        current_node = self.root

        for page in path_list:

            if page not in current_node.children:
                current_node.insert(page)

            current_node = current_node.children[page]

        current_node.handler = handler_data

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "/":
            return "root_handler"

        path_list = self.split_path(path)

        current_node = self.root

        for page in path_list:

            try:
                if current_node.children[page]:
                    current_node = current_node.children[page]
            except:
                return "404 not found!"
        if not current_node.handler:
            return "404 not found!"

        return current_node.handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        if path[0] == "/":
            path = path[1:]

        if path[-1] == "/":
            path = path[:-1]

        path_list = path.split("/")

        return path_list


# Here are some test cases and expected outputs you can use to test your
# implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'

# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))

print(router.lookup("/home/about"))  # should print 'about handler'

# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))

# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
