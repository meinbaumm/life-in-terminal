import sys 
import enum

import googletrans
import terminal

translator = googletrans.Translator()

sentence_sign = '-s'

class TranslationType(enum.Enum):
    by_word = 'words'
    by_sentence = 'sentence'


def _translate_one(text, src, dest, type):
    result = translator.translate(text, src=src, dest=dest)
    if type == TranslationType.by_word:
        print(terminal.green(f'{result.origin} -> {result.text}'))
    elif type == TranslationType.by_sentence:
        print(terminal.green(f'{result.text}'))


def _to_sentence(list_words):
    words_sentence = list_words[1:]
    sentence =' '.join(words_sentence)
    return sentence


def get_translation(args):
    src = args[0]
    dest = args[1]
    words = args[2:]

    if words[0].lower() == sentence_sign:
        sentence = _to_sentence(words)
        _translate_one(sentence, src, dest, type=TranslationType.by_sentence)
    else:
        for translation in words:
            _translate_one(translation, src, dest, type=TranslationType.by_word)


if __name__ == "__main__":
    get_translation(sys.argv[1:])
