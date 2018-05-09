------------------------------------------
SCRABBLE-SCORE
------------------------------------------

I use a prefix tree to store the pair of letters-to-value in the value file.

Pros:
Using prefix tree to store the pair of letters-to-value could reduce the time complexity for searching. If we use hashtable to store the letters-to-value, when searching if any letters combination exist in a word, the time complexity would be higher, since if we use hashtable, we have to find all combinations of letters start from the first index. Also, if we have many different combinations of letters-to-value, using prefix tree can save space -- we don't need to store some prefix of letters repeatly.

e.g: by using hashtable to get the value of "hacker", we have to find if "hacker", "hacke", "hack"......."acker", "acke", "ack".....in the hash table. the searching time complexity would be O((length)^2) for just one word.

Cons:
In some situation hashtable has better performance than prefix tree. When letters which is same as the word is stored in the hashtable, searching is just O(1).


Time Complexity:
Suppose we have m pairs of letters-to-value and n words in thre directionary waiting to be calculated. storing the pairs to prefix tree has O(m * average length of letters) time complexity, searching one word would take O (length of word), thus searching all words in dictionary would take O(n * average length of words). The overall time complexity depends on m, n and the length of letters and words.


------------------------------------------
Class TrieNode
------------------------------------------
TrieNode has 3 members: 
1) val: represents for the value of letters, if such combination is not letters yet, val is 0.
2) is_word: represents if the combination of letters is letters with value in the value file
3) children: this is an array of pointer to the children of current TrieNode, here we have length 52 since we also want this program works fine for uppercase letters. The index of the array represents for the letter, start from index 0 -- 'a'. 

------------------------------------------
compute_values
------------------------------------------
We read from value file and dictionary file to firstly store the letters-to-value and then start searching. the final results is printed and stored in "val_result.txt"

------------------------------------------
get_value
------------------------------------------
This is the part we search the word in the prefix tree. Traverse the word to see if any letter is the children of root, and continue searchin the next letter, everytime we found the value of letters we update the value and save the index, which can make sure we can go back to the index and keep searching the remaining part if we go any further in the trie and found no letters.

------------------------------------------
put_letters
------------------------------------------
Traverse the letters and store the value and letters in the Trie.

