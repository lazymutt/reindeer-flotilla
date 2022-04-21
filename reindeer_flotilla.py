#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import pathlib
import secrets
import sys
try:
    from zxcvbn import zxcvbn
except ImportError:
    print("zxcvbn module missing. Password quality testing disabled.\n")
    zxcvbn = None


def getword():
    """
    Returns a random word from /usr/share/dict/words.
    """

    words_path = '/usr/share/dict/words'

    random_word = secrets.choice(open(words_path, encoding='utf-8').readlines())
    random_word = random_word.rstrip('\r\n')
    return random_word.lower()


def getfrenchword():
    """
    Returns a random word from local french word list.
    """
    words_path = 'francais.txt'

    random_word = secrets.choice(open(words_path, encoding='utf-8').readlines())
    random_word = random_word.rstrip('\r\n')
    return random_word.lower()


def getspanishword():
    """
    Returns a random word from local spanish word list.
    """
    words_path = 'espanol.txt'

    random_word = secrets.choice(open(words_path, encoding='utf-8').readlines())
    random_word = random_word.rstrip('\r\n')
    return random_word.lower()


def decipher_pattern(args):
    """
    Parses pattern provided by user, calls appropriate function, returns final password.
    """
    processed_string = ""
    symbol_list = ['!', '$', '%', '&', '*', '+', '-', ':', ';']

    raw_pattern = list(args.pattern)

    for count, item in enumerate(raw_pattern):
        if item == "W":
            processed_string += str.capitalize(getword())
        elif item == "w":
            processed_string += getword()
        elif item == "R":
            ran_cap_raw = list(getword())
            cap_pos = secrets.randbelow(len(ran_cap_raw) - 1)
            ran_cap_raw[cap_pos] = ran_cap_raw[cap_pos].upper()
            processed_string += ''.join(ran_cap_raw)
        elif item == "#":
            processed_string += str(secrets.randbelow(9))
        elif item == "E":
            processed_string += str.capitalize(getspanishword())
        elif item == "e":
            processed_string += getspanishword()
        elif item == "F":
            processed_string += str.capitalize(getfrenchword())
        elif item == "f":
            processed_string += getfrenchword()
        elif item == "^":
            processed_string += symbol_list[secrets.randbelow(len(symbol_list) - 1)]
        else:
            print(f"{item} is an invalid pattern character")
            sys.exit()

        if args.separator and count < len(args.pattern) - 1:
            processed_string += args.separator

    return processed_string


def main():
    pattern_description = '''\
        Generates passwords.
    
        Output pattern flags:
        Letter\tMeaning
        W\tCapitalized English word
        w\tLowercase English word
        R\tEnglish word, with random letter capitalized
        #\tSingle digit, multiple instances for more digits
        ^\tSingle symbol, multiple instances for more symbols
        E\tCapitalized Spanish word
        s\tLowercase Spanish word
        F\tCapitalized French word
        f\tLowercase French word
    '''
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=pattern_description)
    parser.add_argument('-p', '--pattern', type=str, default='wWw', help='Provide pattern selectors, see description above')
    parser.add_argument('-s', '--separator', type=str, default='', help='Pattern selector separator character')

    args = parser.parse_args()

    if 'f' in args.pattern.lower():
        if not pathlib.Path('./francais.txt').exists():
            print('French dictionary missing.')
            sys.exit()
    if 'e' in args.pattern.lower():
        if not pathlib.Path('./espanol.txt').exists():
            print('Spanish dictionary missing.')
            sys.exit()
    if 'w' in args.pattern.lower():
        if not pathlib.Path('/usr/share/dict/words').exists():
            print('English dictionary missing.')
            sys.exit()

    if not zxcvbn:
        print("┌ pattern output")
        print("└───────────────────────────────")
    else:
        print(" ┌ quality (4 stars is best)")
        print(" │")
        print(" │   ┌ pattern output")
        print("─┴── └───────────────────────────────")

    for _ in range(20):
        pattern_final = decipher_pattern(args)

        if not zxcvbn:
            print(f'{pattern_final}')
        else:
            results = zxcvbn(pattern_final)
            result_stars = "*" * results['score']

            print(f'{result_stars:4} {pattern_final}')


if __name__ == '__main__':
    main()
