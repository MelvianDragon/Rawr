# If I were only using pure Python, I'd use the Enum class
# instead of creating a bunch of empty class instances. However,
# RPython only allows a couple of the most basic built-in modules.

class Token:
    def __init__(self, index):
        self.index = index

class LBracket(Token):
    pass

class RBracket(Token):
    pass

class Colon(Token):
    pass

class Exclam(Token):
    pass

class QuestionToken(Token):
    pass

class PeriodToken(Token):
    pass

class EndParagraph(Token):
    pass

class Rawr(Token):
    def __init__(self, index, word):
        self.index = index
        self.word = word

single_tokens = {
    "[": LBracket,
    "]": RBracket,
    ":": Colon,
    "!": Exclam,
    "?": QuestionToken,
    ".": PeriodToken
}

def tokenize(code):
    code += "\n" # EOF condition
    index = 0
    tokens = []
    newlines = 0
    start = 0
    was_rawr = False
    while index < len(code):
        char = code[index]

        # Handle rawrs
        is_rawr = char not in single_tokens and char not in "\n\r\t "
        if is_rawr and not was_rawr:
            start = index
        elif not is_rawr and was_rawr:
            tokens.append(Rawr(start, code[start:index]))

        # Handle single-character tokens
        if char in single_tokens:
            tokens.append(single_tokens[char](index))
        elif char == '\n':
            newlines += 1
        elif char == '\r' or char == '\t':
            pass

        # Handle paragraph separations
        if char != '\n':
            if newlines >= 2:
                tokens.append(EndParagraph(index - newlines))
            newlines = 0
        index += 1
        was_rawr = is_rawr

    return tokens