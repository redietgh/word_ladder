#!/bin/python3
import copy
from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny',
    'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey',
    'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    with open(dictionary_file, 'r') as afile:
        words_list = [line.strip() for line in afile]
    if end_word not in words_list:
        return None
    if start_word == end_word:
        return [start_word]
    ladder = deque([[start_word]])
    while ladder:
        route = ladder.popleft()
        last_word = route[-1]
        for word in words_list[:]:
            if word not in route and _adjacent(last_word, word):
                if word == end_word:
                    return route + [end_word]
                else:
                    ladder.append(copy.deepcopy(route) + [word])
                    words_list.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 1:
        return True
    if ladder is None or len(ladder) < 1:
        return False
    if len(ladder) < 2:
        return False
    for i in range(0, len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    diff_charcounter = 0
    for i in range(len(word1)):
        diff_charcounter += 1
        if diff_charcounter > 1:
            return False
    return diff_charcounter == 1
