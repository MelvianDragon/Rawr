from tokenizer import *

class Statement:
    pass

class Function(Statement):
    def __init__(self, name, sentences):
        self.name = name
        self.sentences = sentences

class Question(Statement):
    def __init__(self, predicate, body):
        self.predicate = predicate
        self.body = body

class Sentence(Statement):
    pass

class Exclamation(Sentence):
    def __init__(self, words):
        self.words = words

class Period(Sentence):
    def __init__(self, words):
        self.words = words


class Word:
    pass

class RawrWord(Word):
    def __init__ (self, word, R1s, is_A, As, Ws, R2s, extras):
        self.word = word
        self.R1s = R1s
        self.is_A = is_A
        self.As = As
        self.Ws = Ws
        self.R2s = R2s
        self.extras = extras

class LambdaWord(Word):
    def __init__ (self, sentences):
        self.sentences = sentences

def parse_rawr(tokens, index):
    rawr_obj = tokens[index]
    rawr = rawr_obj.word
    index += 1
    i = 0
    R1s = 0
    As = 0
    Ws = 0
    R2s = 0
    extras = []
    is_A = True
    # Parse Rs
    while i < len(rawr) and rawr[i] not in "AaEe":
        if rawr[i] not in "Rr":
            raise ValueError("Expected R")
        R1s += 1
        i += 1
    # Parse As or Es
    if i < len(rawr) and rawr[i] in "Aa":
        is_A = True
        while i < len(rawr) and rawr[i] not in "Ww":
            if rawr[i] not in "Aa":
                raise ValueError("Expected A")
            i += 1
            As += 1
    elif i < len(rawr) and rawr[i] in "Ee":
        is_A = False
        while i < len(rawr) and rawr[i] not in "Ww":
            if rawr[i] not in "Ee":
                raise ValueError("Expected E")
            i += 1
            As += 1
    # Parse Ws
    while i < len(rawr) and rawr[i] not in "Rr":
        if rawr[i] not in "Ww":
            raise ValueError("Expected W")
        Ws += 1
        i += 1
    # Parse Rs
    while i < len(rawr) and rawr[i] in "Rr":
        R2s += 1
        i += 1

    if R1s == 0 or As == 0 or Ws == 0 or R2s == 0:
        raise ValueError("Incomplete rawr. Make sure there is at least one of each letter.")

    # Parse subrawrs
    while i < len(rawr) and rawr[i] in "AaEeWw":
        inner_As = 0
        inner_Ws = 0
        inner_Rs = 0
        inner_opposite = False
        # Parse As or Es IF they exist
        if i < len(rawr) and rawr[i] in "AaEe":
            if rawr[i] in "Aa":
                inner_opposite = not is_A
                while i < len(rawr) and rawr[i] not in "Ww":
                    if rawr[i] not in "Aa":
                        raise ValueError("Expected A")
                    i += 1
                    inner_As += 1
            elif rawr[i] in "Ee":
                inner_opposite = is_A
                while i < len(rawr) and rawr[i] not in "Ww":
                    if rawr[i] not in "Ee":
                        raise ValueError("Expected E")
                    i += 1
                    inner_As += 1
        # Parse Ws
        while i < len(rawr) and rawr[i] not in "Rr":
            if rawr[i] not in "Ww":
                raise ValueError("Expected W")
            inner_Ws += 1
            i += 1
        # Parse Rs
        while i < len(rawr) and rawr[i] in "Rr":
            inner_Rs += 1
            i += 1
        if inner_Ws == 0 or inner_Rs == 0:
            raise ValueError("Incomplete subrawr. Make sure there is at least one W and one R.")
        extras.append((inner_opposite, inner_As, inner_Ws, inner_Rs))
    return index, RawrWord(rawr.lower(), R1s, is_A, As, Ws, R2s, extras)

def parse_lambda(tokens, index):
    if not isinstance(tokens[index], LBracket):
        raise ValueError("Lambda must start with left bracket.")
    index += 1
    sentences = []
    while index < len(tokens) and not isinstance(tokens[index], RBracket):
        index, sentence = parse_sentence(tokens, index)
        sentences.append(sentence)
    if index >= len(tokens):
        raise ValueError("Missing right bracket.")
    index += 1
    return index, LambdaWord(sentences)

def parse_sentence(tokens, index):
    words = []
    if index >= len(tokens):
        raise ValueError("Expected a sentence.")
    while index < len(tokens):
        token = tokens[index]
        if isinstance(token, LBracket):
            index, _lambda = parse_lambda(tokens, index)
            words.append(_lambda)
        elif isinstance(token, PeriodToken):
            index += 1
            if len(words) == 0:
                raise ValueError("Sentences cannot be empty.")
            return index, Period(words)
        elif isinstance(token, Exclamation):
            index += 1
            if len(words) == 0:
                raise ValueError("Sentences cannot be empty.")
            return index, Exclamation(words)
        elif isinstance(token, QuestionToken):
            index += 1
            if len(words) == 0:
                raise ValueError("Sentences cannot be empty.")
            index, inner = parse_sentence(tokens, index)
            return index, Question(words, inner)
        elif isinstance(token, Rawr):
            index, rawr = parse_rawr(tokens, index)
            words.append(rawr)
        else:
            print(token)
            raise ValueError("Unexpected token.")
    raise ValueError("Missing sentence ending.")


def parse_paragraph(tokens, index):
    new_index, first_rawr = parse_rawr(tokens, index)
    function_name = None
    if isinstance(tokens[new_index], Colon):
        function_name = first_rawr.word
        new_index += 1
    else:
        new_index = index
    index = new_index
    sentences = []
    while index < len(tokens) and not isinstance(tokens[index], EndParagraph):
        index, sentence = parse_sentence(tokens, index)
        sentences.append(sentence)
    if index < len(tokens):
        index += 1
    if function_name is not None:
        return index, [Function(function_name, sentences)]
    return index, sentences

def parse(tokens):
    index = 0
    paragraphs = []
    while index < len(tokens):
        index, paragraph = parse_paragraph(tokens, index)
        paragraphs.append(paragraph)
    return paragraphs