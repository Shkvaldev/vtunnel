from loguru import logger

from . import Node


class WordList:
    def __init__(self, path, logger=logger):
        self.logger = logger
        self.root = Node()
        self.path = path

        self.load()

    def insert(self, word):
        """Inserts new word into graph"""
        node = self.root

        # Inserting reversed word
        for letter in reversed(word):
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]

        node.is_leaf = True

    def load(self, path=None):
        """Loads words into graph from file"""
        if not path:
            path = self.path

        count = 0
        try:
            with open(path, "r") as f:
                for word in f.readlines():
                    self.insert(word.strip().lower())
                    count += 1
            self.logger.success(f"Wordlist of `{count}` words is ready!")
        except Exception as e:
            err_msg = f"Failed to load wordlist from file `{self.path}`: {e}"
            self.logger.error(err_msg)
            raise ValueError(err_msg)

    def find(self, postfix, limit=5):
        """Finds all words with provided postfix"""
        if not postfix:
            return []

        node = self.root
        for letter in reversed(postfix):
            if letter not in node.children:
                return []
            node = node.children[letter]

        result = []
        stack = [(node, postfix[::-1])]

        while stack and len(result) < limit:
            current_node, current_word = stack.pop()

            if current_node.is_leaf:
                result.append(current_word[::-1])

            for letter, child_node in current_node.children.items():
                stack.append((child_node, current_word + letter))

        return result

    def find_by_depth(self, depth):
        if depth <= 0:
            return []

        result = []
        stack = [(self.root, [], 0)]

        while stack:
            node, chars, curr_depth = stack.pop()

            if curr_depth == depth:
                word = "".join(reversed(chars))
                result.append(word)
                continue

            if curr_depth < depth:
                for letter, child_node in node.children.items():
                    stack.append((child_node, chars + [letter], curr_depth + 1))

        return result


if __name__ == "__main__":
    WordList("words.txt")
