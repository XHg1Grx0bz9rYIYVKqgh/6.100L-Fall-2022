# Problem Set 4C
# Name:
# Collaborators:

import json
import ps4b # Importing your work from Part B

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    
    file_name (字符串): 包含要加载单词列表的文件名

    Returns: 一个有效单词的列表。单词是由小写字母组成的字符串。

    根据单词列表的大小，此函数可能需要一段时间才能完成。
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    
    判断 word 是否为有效单词，忽略大小写和标点符号

    word_list (列表): 字典中的单词列表。
    word (字符串): 一个可能的单词。

    Returns: 如果 word 在 word_list 中返回 True，否则返回 False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    Returns: 一段加密文本形式的故事。
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    
    给定一个字符串密文和一个可能用于生成该密文的填充码 (pad) 列表，
    找出实际用于生成该密文的填充码。

    我们将这样定义用于生成密文的填充码：当使用该填充码解密密文时，
    生成的明文中包含最多的有效英语单词。
    如果出现平局（有效单词数相同），则返回导致最大有效英语单词数的最后一个填充码。

    ciphertext (EncryptedMessage): 密文对象
    pads (list of lists of ints): 可能用于加密密文的填充码 (pad) 列表

    Returns: (PlaintextMessage) 包含解密后的密文和最佳填充码的消息对象
    '''
    max_num = 0
    pad_max = []
    for pad in pads:
        list_1 = ciphertext.decrypt_message(pad).get_text().split()
        num = 0
        for word in list_1:
            if is_word(load_words('words.txt'), word):
                num += 1
        if num >= max_num:
            pad_max = pad
            max_num = num
    return ciphertext.decrypt_message(pad_max)
        

def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    在此处编写代码，使用可能的填充码列表来解码 Bob 的故事。
    提示：使用辅助函数 get_story_string 和 get_story_pads 以及你的 EncryptedMessage 类。

    Returns: (string) 解码后的故事
    '''
    str_1 = get_story_string()
    pad_1 = get_story_pads()
    return decrypt_message_try_pads(ps4b.EncryptedMessage(str_1), pad_1).get_text()



if __name__ == '__main__':
    # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)