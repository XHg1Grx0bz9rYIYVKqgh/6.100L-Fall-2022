# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    return input_text.split()


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)

    Args (参数):
        input_iterable: 一个字符串或字符串列表，全部由小写字符组成
    Returns (返回值):
        一个映射关系为 字符串:整数 (string:int) 的字典，其中每个字符串
        是 input_iterable 中的一个字母或单词，而对应的整数
        是该字母或单词在 input_iterable 中出现的频率
    Note (注意): 
        你可以假设我们提供的文本文档中，唯一的空白字符只有换行符或单词之间的空格（也就是说不存在制表符/Tab键）
    """
    dict_1 = {}
    for ele in input_iterable:
        if ele not in dict_1:
            dict_1[ele] = 1
        else:
            dict_1[ele] += 1
    return dict_1
    


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    
    Args (参数):
        word: 字符串形式的单词
    Returns (返回值):
        一个映射关系为 字符串:整数 (string:int) 的字典，其中每个字符串
        是单词 (word) 中的一个字母，而对应的整数
        是该字母在单词中出现的频率
    """
    list_2 = list(word)
    dict_2 = {}
    for ele in list_2:
        if ele in dict_2:
            dict_2[ele] += 1
        else:
            dict_2[ele] = 1
    return dict_2
    


### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
        
        dict1 和 dict2 的键都是小写的，
    你不需要担心大小写敏感问题。

    Args (参数):
        freq_dict1: word1 的字母频率字典或 text1 的单词频率字典
        freq_dict2: word2 的字母频率字典或 text2 的单词频率字典
    Returns (返回值):
        float (浮点数), 一个 0 到 1 之间（包含 0 和 1）的数字，
        表示这些单词/文本彼此之间的相似程度。

        单词/文本频率的差异 = DIFF，由以下三种情况累加而成：
        * 如果一个元素同时出现在 dict1 和 dict2 中，取频率的差值（绝对值）
        * 如果一个元素只出现在 dict1 中，取 dict1 中的该频率
        * 如果一个元素只出现在 dict2 中，取 dict2 中的该频率
        
        总频率 = ALL，通过将 dict1 和 dict2 中的所有频率相加计算得出。
        
        返回 1-(DIFF/ALL) 的结果，并保留 2 位小数。
    """
    dict_3 = {}
    ALL = 0
    DIFF = 0
    for i in freq_dict1:
        if i not in freq_dict2:
            dict_3[i] = freq_dict1[i]
            ALL += freq_dict1[i]
        else:
            dict_3[i] = abs(freq_dict1[i] - freq_dict2[i])
            ALL += freq_dict1[i] + freq_dict2[i]
    for i in freq_dict2:
        if i not in dict_3:
            dict_3[i] = freq_dict2[i]
            ALL += freq_dict2[i]
    DIFF = sum(dict_3.values())
    return round(1 - DIFF/ALL, 2)


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.

    dict1 和 dict2 的键都是小写的，
    你不需要担心大小写敏感问题。

    Args (参数):
        freq_dict1: 其中一段文本的频率字典
        freq_dict2: 另一段文本的频率字典
    Returns (返回值):
        一个列表，包含输入字典中出现频率最高的单词（一个或多个）

    关于“出现频率最高的单词”：
        * 基于两个字典中合并后的单词频率。
          如果一个单词在两个字典中都出现，将其频率之和作为合并后的频率。
        * 不必同时存在于两个字典中，也就是说，它可以只存在于 dict1 中，
          只存在于 dict2 中，或者同时存在于 dict1 和 dict2 中。
    
    如果有多个单词并列第一（即拥有相同的最高频率），
    请返回一个包含所有这些单词的、按字母顺序排列的列表。
    """
    dict_4 = {}
    for i in freq_dict1:
        dict_4[i] = freq_dict1[i]
    for i in freq_dict2:
        if i not in dict_4:
            dict_4[i] = freq_dict2[i]
        else:
            dict_4[i] += freq_dict2[i]
    max_4 = max(dict_4.values())
    list_4 = []
    for i in dict_4:
        if dict_4[i] == max_4:
            list_4.append(i)
    return list_4


### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier

    Args (参数):
        file_path: 字符串形式的文件名
    Returns (返回值):
        一个将每个单词映射到其 TF 值的字典

    * TF 的计算公式为：
      TF(i) = (单词 *i* 在文档中出现的次数) / (文档中的单词总数)
    * 思考一下如何利用之前的 get_frequencies 函数来辅助计算
    """
    list_5 = text_to_list(load_file(file_path))
    dict_5 = get_frequencies(list_5)
    dict_5_2 = {}
    for i in list_5:
        dict_5_2[i] = dict_5[i] / len(list_5)
    return dict_5_2

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()
    
    Args (参数):
        file_paths: 文件名列表，其中每个文件名都是字符串
    Returns (返回值):
        一个将每个单词映射到其 IDF 值的字典

    * IDF 的计算公式为：
      IDF(i) = log_10(文档总数 / 包含单词 *i* 的文档数量)
    * 其中 log_10 表示以 10 为底的对数，可以使用 math.log10() 进行计算
    """
    dic_word = {}
    num_doc = len(file_paths)   
    for i in file_paths:
        list_5 = text_to_list(load_file(i))
        list_5_2 = []
        for j in list_5:
            if j not in list_5_2:
                list_5_2.append(j)
        for k in list_5_2:
            if k in dic_word:
                dic_word[k] += 1
            else:
                dic_word[k] = 1
    dict_5_2 = {}
    for l in dic_word:
        dict_5_2[l] = math.log10(num_doc/dic_word[l])
    list_5 = dict_5_2.items()
    return dict_5_2


def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        
        Args (参数):
        tf_file_path: 字符串形式的文件名（用于计算 TF）
        idf_file_paths: 文件名列表，其中每个文件名都是字符串（用于计算 IDF）
    Returns (返回值):
        一个排序后的元组列表（按 TF-IDF 分数递增排列），其中每个元组
        的格式为 (单词, TF-IDF)。如果单词的 TF-IDF 分数相同，
        则这些单词应按字母顺序递增排列。

    * TF-IDF(i) = TF(i) * IDF(i)
        """
    dict_5 = {}
    for i in get_tf(tf_file_path):
        dict_5[i] = get_tf(tf_file_path)[i] * get_idf(idf_file_paths)[i]
    list_5_3 = sorted(dict_5.items(),key = lambda x: x[1])  
    return tuple(list_5_3)

if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    # Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)      # should print ['hello', 'world', 'hello']
    print(friend)     # should print ['hello', 'friends']

    # Tests Problem 1: Get Frequencies
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    # Tests Problem 2: Get Letter Frequencies
    freq1 = get_letter_frequencies('hello')
    freq2 = get_letter_frequencies('that')
    print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    # Tests Problem 3: Similarity
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    word1_freq = get_letter_frequencies('toes')
    word2_freq = get_letter_frequencies('that')
    word3_freq = get_frequencies('nah')
    word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    print(word_similarity1)       # should print 1.0
    print(word_similarity2)       # should print 0.25
    print(word_similarity3)       # should print 0.0
    print(word_similarity4)       # should print 0.4

    # Tests Problem 4: Most Frequent Word(s)
    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    print(most_frequent)      # should print ["hello", "world"]

    # Tests Problem 5: Find TF-IDF
    tf_text_file = 'tests/student_tests/hello_world.txt'
    idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]