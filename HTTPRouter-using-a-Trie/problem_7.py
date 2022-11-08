class Router:
    def __init__(self, handler, not_found_handler):
        self.root = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        path_parts = self.split_path(path)
        self.root.insert(path_parts, handler)

    def lookup(self, path):
        if path == "/":
            return self.root.handler
        path_parts = self.split_path(path)
        handler = self.root.find(path_parts)
        return handler or self.not_found_handler

    def split_path(self, path):
        return path.rstrip("/").split("/")


class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, path_parts, handler):
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, path_parts):
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node.handler


class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

    def insert(self, path_part):
        self.children[path_part] = RouteTrieNode()


# test case 1

# create the router and add a route
router = Router("root handler", "not found handler")
# add a route
router.add_handler("/home/about", "about handler")

print(router.lookup("/"))
# should print 'root handler'

print(router.lookup("/home"))
# should print 'not found handler'

print(router.lookup("/home/about"))
# should print 'about handler'

print(router.lookup("/home/about/"))
# should print 'about handler'

print(router.lookup("/home/about/me"))
# should print 'not found handler'


# test case 2

# create the router and add a route
router = Router("root", "")
# add a route
router.add_handler("/home/home/about", "about handler")

print(router.lookup("/"))
# should print 'root'

print(router.lookup("/home"))
# should print ''

print(router.lookup("/home/about"))
# should print ''

print(router.lookup("/home/home/"))
# should print ''

print(router.lookup("/home/home/about"))
# should print 'about handler'


# test case 3

# create the router and add a route
router = Router("", "not found")
# add a route
router.add_handler("/about", "about handler")

print(router.lookup("/"))
# should print ''

print(router.lookup("/a"))
# should print 'not found'

print(router.lookup("/home/about"))
# should print 'not found'

print(router.lookup("/about/"))
# should print 'about handler'


# test case 4

# create the router and add a route
router = Router("root", "not found")
# add a route
router.add_handler("/", "about handler")

print(router.lookup("/"))
# should print 'root'

print(router.lookup("/a"))
# should print 'not found'

print(router.lookup("/home/about"))
# should print 'not found'

print(router.lookup("/about/"))
# should print 'not found'