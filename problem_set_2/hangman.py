# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# 辅助代码
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.
    returns: list, 一个有效单词列表。单词由小写字母字符串组成。

    Depending on the size of the word list, this function may
    take a while to finish.
    根据单词列表的大小，此函数可能需要一段时间才能完成。
    """
    print("Loading word list from file...")
    # inFile: file
    # inFile: 文件对象
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    # line: 字符串
    line = inFile.readline()
    # wordlist: list of strings
    # wordlist: 字符串列表
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    wordlist (list): 单词列表（字符串）

    returns: a word from wordlist at random
    returns: 从 wordlist 中随机返回一个单词
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# 辅助代码结束
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
# 加载单词列表，以便在程序中的任何位置访问
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    secret_word: string, 用户正在猜测的小写单词
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far
    letters_guessed: list (小写字母列表), 目前为止已猜过的字母

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    returns: boolean, 如果 secret_word 的所有字母都在 letters_guessed 中，则为 True，否则为 False
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # 在此处填写代码并删除 "pass"
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    secret_word: string, 用户正在猜测的小写单词
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far
    letters_guessed: list (小写字母列表), 目前为止已猜过的字母

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    returns: string, 由字母和星号 (*) 组成，表示 secret_word 中尚未猜出的字母
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # 在此处填写代码并删除 "pass"
    word = ""
    for i in secret_word:    
        if i in letters_guessed:
            word += i
        else:
            word += "*"
    return word
            
        
        


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far
    letters_guessed: list (小写字母列表), 目前为止已猜过的字母

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    returns: string, 由尚未猜出的字母组成。这些字母应按字母顺序返回
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # 在此处填写代码并删除 "pass"
    str = ""
    for i in range(len(string.ascii_lowercase)):
        if string.ascii_lowercase[i] not in letters_guessed:
            str += string.ascii_lowercase[i]
    return str

def choose_a_letter(secret_word, available_letters):
    choose_from = ""
    for i in secret_word:
        if i in available_letters:
            choose_from += i
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    secret_word: string, 要猜测的秘密单词。
    with_help: boolean, this enables help functionality if true.
    with_help: boolean, 如果为 true，则启用辅助功能。

    Starts up an interactive game of Hangman.
    启动一个交互式的 Hangman 游戏。

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.
    * 游戏开始时，让用户知道 secret_word 包含多少个字母，以及他们开始时有多少次猜测机会。

    * The user should start with 10 guesses.
    * 用户应以 10 次猜测机会开始。

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.
    * 在每一轮之前，你应该向用户显示他们还剩多少次猜测机会，以及用户尚未猜出的字母。

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)
    * 要求用户每一轮提供一个猜测。记得确保用户输入的是单个字母（或者是用于辅助功能的帮助字符 '!'）

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.
    * 如果用户输入了错误的辅音，则用户失去一次猜测机会，而如果用户输入了错误的元音 (a, e, i, o, u)，则用户失去两次猜测机会。

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * 用户应该在每次猜测后立即收到反馈，了解他们的猜测是否出现在计算机的单词中。

    * After each guess, you should display to the user the
      partially guessed word so far.
    * 每次猜测后，你应该向用户显示目前为止部分猜出的单词。

    -----------------------------------
    with_help functionality
    with_help 功能（辅助功能）
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.
    * 如果猜测是符号 !，你应该向用户揭示单词中缺失的一个字母，代价是消耗 3 次猜测机会。如果用户剩余猜测机会不足 3 次，打印一条警告消息。否则，将此字母添加到他们已猜出的单词中并继续正常游戏。

    Follows the other limitations detailed in the problem write-up.
    遵循问题说明中详述的其他限制。
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # 在此处填写代码并删除 "pass"
    letters_guessed = ""
    guesses = 10
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    while  not has_player_won(secret_word, letters_guessed) and guesses > 0:
    # 循环检查是否胜利
        print("---")    
        print(f"You have {guesses} guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        # print("Please guess a letter:")
        # guess_letter = input().lower()
        guess_letter = input("Please guess a letter: ").lower()
        if guess_letter.isalpha():
        # 如果用户猜的字符是字母：
            if guess_letter not in letters_guessed:
            # 如果用户猜的字母不在已猜的字母列表里
                if guess_letter in secret_word:
                # 如果猜中
                    letters_guessed += guess_letter
                    print("Good guess: " + get_word_progress(secret_word, letters_guessed))
                else:
                # 如果猜错
                    letters_guessed += guess_letter    
                    if guess_letter in ["a", "e", "i", "o", "u"]:
                        guesses -= 2
                    else:
                        guesses -= 1
                    print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
            else:
            # 如果用户菜的字母在已猜的字母列表里
                print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
        elif guess_letter == "!" and with_help:
        # 如果用户猜的字符是"!"
            if guesses >= 3:
                guesses -= 3
                reveal_letter = choose_a_letter(secret_word, get_available_letters(letters_guessed))
                letters_guessed += reveal_letter
                print("Letter revealed: " + reveal_letter)
                print(get_word_progress(secret_word, letters_guessed))
            else:
                print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
            
        else:
        # 如果用户猜的字符不是字母也不是感叹号
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
    print("---")    
    if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        unique_letters = ""
        for i in secret_word:
            if i not in unique_letters:
                unique_letters += i
        print(f"Your total score for this game is: {guesses + len(unique_letters) * 4 + len(secret_word) * 3 }")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test
# 当你完成了 hangman 函数后，向下滚动到文件底部并取消注释这些行以进行测试

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.
    # 要测试你的游戏，请取消注释以下三行。

    secret_word = choose_word(wordlist)
    # secret_word = "wildcard"
    with_help = True
    hangman(secret_word, with_help)


    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!
    # 在你完成 with_help 功能后，将 with_help 更改为 True 并尝试输入 "!" 作为猜测！

    ###############

    # SUBMISSION INSTRUCTIONS
    # 提交说明
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    # 提交作业时，上面的行是否被注释并不重要。但是，请在提交前再次运行 ps2_student_tester.py，以确保所有测试都通过。
    pass

