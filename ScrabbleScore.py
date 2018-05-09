class TrieNode(object):
    def __init__(self, val):
        self.val = val
        self.is_word = False
        self.children = [None] * 52

class Scrabble(object):
    def compute_values(self, value_path, dictionary_path):
        """
        :param value_path: String
        :param dictionary_path: String
        :return:
        """
        with open(value_path) as value_file:
            value_string = value_file.readlines()
        value_list = map(lambda string: string.strip().split(' '), value_string)

        with open(dictionary_path) as dictionary_file:
            dictionary = dictionary_file.readlines()
        dictionary_list = map(lambda string: string.strip(), dictionary)

        # construct the prefix tree
        root = TrieNode(0)
        for letters, val in value_list:
            self.put_letters(letters, root, int(val))

        # self.print_trie(root, -1, 0)

        # find value for word in dictionary
        val_list = list()
        result_file = open("val_result.txt", "w")
        for word in dictionary_list:
            val = self.get_value(word, root)
            val_list.append(val)
            result_file.write(word + ':' + str(val) + '\n')

        print zip(dictionary_list, val_list)

        return val_list

    def get_value(self, word, root):
        """
        :param word: String
        :param root: TrieNode
        :return: Integer
        """
        ascii_a = ord('a')
        ascii_upper_a = ord('A')
        n = len(word)
        if n == 0:
            return 0
        i, sum_val = 0, 0
        pre_idx = 0
        while i < n:
            node = root
            val = 0
            while i < n:
                pos = ord(word[i]) - ascii_upper_a + 26 if word[i].isupper() else ord(word[i]) - ascii_a
                if not node.children[pos]:
                    break
                node = node.children[pos]
                if node.is_word:
                    pre_idx = i
                    val = node.val
                i += 1
            i = pre_idx
            sum_val += val
            i += 1
            pre_idx += 1
        return sum_val

    def put_letters(self, letters, root, val):
        """
        :param letters: String
        :param root: TrieNode
        :param val: Integer
        :return: void
        """
        ascii_a = ord('a')
        ascii_upper_a = ord('A')
        node = root
        for char in letters:
            pos = ord(char) - ascii_upper_a + 26 if char.isupper() else ord(char) - ascii_a
            if not node.children[pos]:
                node.children[pos] = TrieNode(0)
            node = node.children[pos]
        node.val = val
        node.is_word = True

    def print_trie(self, node, pos, level):
        """
        :param node: TrieNode
        :param pos: Integer
        :param level: Integer
        :return: void
        """
        if not node:
            return
        if pos != -1:
            print(chr(ord('a') + pos), level) if pos < 26 else (chr(ord('A') + pos - 26), level), node.is_word, node.val
        for i in range(52):
            self.print_trie(node.children[i], i, level + 1)


scrabble = Scrabble()
value_path_1 = "value_file_1.txt"
dictionary_path_1 = "dictionary"
scrabble.compute_values(value_path_1, dictionary_path_1)

value_path_2 = "value_file_2.txt"
scrabble.compute_values(value_path_2, dictionary_path_1)
