from parser import *

class StackItem:
    pass

class ListItem(StackItem):
    def __init__(self, lst):
        self.lst = lst

class NumberItem(StackItem):
    def __init__(self, num):
        self.num = num

class LambdaItem(StackItem):
    def __init__(self, _lambda):
        self._lambda = _lambda


def flip_rawr(word):
    # Note that the parser automatically lowercases all rawrs.
    word = RawrWord(word.word, word.R1s, word.is_A, word.As, word.Ws, word.R2s, word.extras)
    word.word = word.word.replace('e', '\0').replace('a', 'e').replace('\0', 'a')
    word.is_A = not word.is_A
    return word

#
# BUILT-IN FUNCTIONS
#

# Stack management

def builtin_swap(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rawr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    stack.append((persist, a2))
    stack.append((persist, a1))

def builtin_dup(functions, para, stack, secondary_stack, persist):
    if len(stack) == 0:
        raise RuntimeError("The stack had nothing to duplicate.")
    stack.append(stack[-1])

def builtin_pop(functions, para, stack, secondary_stack, persist):
    if len(stack) == 0:
        raise RuntimeError("The stack had nothing to pop.")
    stack.pop()

def builtin_roll(functions, para, stack, secondary_stack, persist):
    if len(stack) < 3:
        raise RuntimeError("The raawr function requires at least 3 items on the stack.")
    _, a3 = stack.pop()
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    stack.append((persist, a2))
    stack.append((persist, a3))
    stack.append((persist, a1))

def builtin_over(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The raawrwr function requires at least 2 items on the stack.")
    stack.append(stack[-2])





# Arithmetic

def builtin_add(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rrawr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(a1.num + a2.num)))
    else:
        raise ValueError("incorrect arguments")

def builtin_sub(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rawwrr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(a1.num - a2.num)))
    else:
        raise ValueError("incorrect arguments")

def builtin_mul(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The raawrr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(a1.num * a2.num)))
    else:
        raise ValueError("incorrect arguments")

def builtin_div(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The raawwr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(a1.num / a2.num)))
    else:
        raise ValueError("incorrect arguments")

def builtin_mod(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rrawrr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(a1.num % a2.num)))
    else:
        raise ValueError("incorrect arguments")

def builtin_pos(functions, para, stack, secondary_stack, persist):
    if len(stack) < 1:
        raise RuntimeError("The rawrwr function requires at least 1 item on the stack.")
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem):
        stack.append((persist, NumberItem(+a1.num)))
    else:
        raise ValueError("incorrect arguments")

def builtin_neg(functions, para, stack, secondary_stack, persist):
    if len(stack) < 1:
        raise RuntimeError("The rawrwwr function requires at least 1 item on the stack.")
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem):
        stack.append((persist, NumberItem(-a1.num)))
    else:
        raise ValueError("incorrect arguments")


# Comparison

def builtin_gt(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rrawwr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(1 if a1.num > a2.num else 0)))
    else:
        raise ValueError("incorrect arguments")

def builtin_gte(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rraawr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(1 if a1.num >= a2.num else 0)))
    else:
        raise ValueError("incorrect arguments")

def builtin_lt(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rawrrr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(1 if a1.num < a2.num else 0)))
    else:
        raise ValueError("incorrect arguments")

def builtin_lte(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rawwwr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(1 if a1.num <= a2.num else 0)))
    else:
        raise ValueError("incorrect arguments")

def builtin_eql(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rrawwwr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(1 if a1.num == a2.num else 0)))
    else:
        raise ValueError("incorrect arguments")

def builtin_and(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The raaawr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(1 if a1.num != 0 and a2.num != 0 else 0)))
    else:
        raise ValueError("incorrect arguments")

def builtin_or(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The raawwrr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem) and isinstance(a2, NumberItem):
        stack.append((persist, NumberItem(1 if a1.num != 0 or a2.num != 0 else 0)))
    else:
        raise ValueError("incorrect arguments")

def builtin_not(functions, para, stack, secondary_stack, persist):
    if len(stack) < 1:
        raise RuntimeError("The rrawwrr function requires at least 1 item on the stack.")
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem):
        stack.append((persist, NumberItem(0 if a1.num != 0 else 1)))
    else:
        raise ValueError("incorrect arguments")


# List

def builtin_append(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rraawrr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, ListItem):
        a1.lst.append(a2)
        stack.append((persist, a1))
    else:
        raise ValueError("incorrect arguments")

def builtin_insert(functions, para, stack, secondary_stack, persist):
    if len(stack) < 3:
        raise RuntimeError("The rraawwr function requires at least 3 items on the stack.")
    _, a3 = stack.pop()
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if a2.num < 0:
        raise ValueError("Index must be non-negative.")
    if isinstance(a1, ListItem) and isinstance(a2, NumberItem):
        a1.lst.insert(max(0, a2.num), a3) # max(0, ...) is necessary to please RPython
        stack.append((persist, a1))
    else:
        raise ValueError("incorrect arguments")

def builtin_get(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rraawwrr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, ListItem) and isinstance(a2, NumberItem):
        stack.append((persist, a1))
        if not isinstance(a2.num, int):
            raise ValueError("Index must be a whole number.")
        if a2.num < 0:
            raise ValueError("Index must be non-negative.")
        if a2.num >= len(a1.lst):
            raise ValueError("Index out of bounds.")
        stack.append((persist, a1.lst[a2.num]))
    else:
        raise ValueError("incorrect arguments")

def builtin_delete(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The rawwwrrr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, ListItem) and isinstance(a2, NumberItem):
        stack.append((persist, a1))
        if not isinstance(a2.num, int):
            raise ValueError("Index must be a whole number.")
        if a2.num < 0:
            raise ValueError("Index must be non-negative.")
        if a2.num >= len(a1.lst):
            raise ValueError("Index out of bounds.")
        stack.append((persist, a1.lst.pop(a2.num)))
    else:
        raise ValueError("incorrect arguments")

def builtin_cat(functions, para, stack, secondary_stack, persist):
    if len(stack) < 2:
        raise RuntimeError("The raaawrrr function requires at least 2 items on the stack.")
    _, a2 = stack.pop()
    _, a1 = stack.pop()
    if isinstance(a1, ListItem) and isinstance(a2, ListItem):
        stack.append((persist, ListItem(a1.lst + a2.lst)))
    else:
        raise ValueError("incorrect arguments")



# Functional

def builtin_stash(functions, para, stack, secondary_stack, persist):
    if len(stack) < 1:
        raise RuntimeError("The rawrrewr function requires at least 1 item on the stack.")
    _, a1 = stack.pop()
    secondary_stack.append((persist, a1))

def builtin_recurse(functions, para, stack, secondary_stack, persist):
    execute_paragraph(functions, para, para, stack, secondary_stack)

def builtin_execute(functions, para, stack, secondary_stack, persist):
    if len(stack) < 1:
        raise RuntimeError("The raaawwrr function requires at least 1 item on the stack.")
    _, a1 = stack.pop()
    if isinstance(a1, LambdaItem):
        execute_paragraph(functions, para, a1._lambda, stack, secondary_stack)
    else:
        raise ValueError("incorrect arguments")


# I/O

def builtin_print_numbers(functions, para, stack, secondary_stack, persist):
    _, value = stack.pop()
    if isinstance(value, NumberItem):
        print(value.num)
    elif isinstance(value, ListItem):
        print(value.lst) # TODO: change this
    else:
        print("<Unknown type>")

def builtin_print_string(functions, para, stack, secondary_stack, persist):
    _, value = stack.pop()
    if isinstance(value, ListItem):
        print(''.join([chr(a.num) for a in value.lst if isinstance(a, NumberItem)]))
    else:
        raise ValueError("incorrect arguments")

#def builtin_read_line(functions, para, stack, secondary_stack, persist):
#    i = input(">> ")
#    stack.append((persist, ListItem([NumberItem(ord(n)) for n in i])))


# Types

def builtin_type(functions, para, stack, secondary_stack, persist):
    if len(stack) < 1:
        raise RuntimeError("The rraaawwrwwr function requires at least 1 item on the stack.")
    _, a1 = stack.pop()
    if isinstance(a1, NumberItem):
        stack.append((persist, a1))
        stack.append((persist, NumberItem(0)))
    elif isinstance(a1, ListItem):
        stack.append((persist, a1))
        stack.append((persist, NumberItem(1)))
    elif isinstance(a1, LambdaItem):
        stack.append((persist, a1))
        stack.append((persist, NumberItem(2)))
    else:
        raise RuntimeError("invalid type found in stack, this is a bug.")


builtin_functions = {
    # Stack management
    "rawr": builtin_swap,
    "rawrr": builtin_dup,
    "rawwr": builtin_pop,
    "raawr": builtin_roll,
    "raawrwr": builtin_over,

    # Arithmetic
    "rrawr": builtin_add,
    "rawwrr": builtin_sub,
    "raawrr": builtin_mul,
    "raawwr": builtin_div,
    "rrawrr": builtin_mod,
    "rawrwr": builtin_pos,
    "rawrwwr": builtin_neg,

    # Comparison
    "rrawwr": builtin_gt,
    "rraawr": builtin_gte,
    "rawrrr": builtin_lt,
    "rawwwr": builtin_lte,
    "rrawwwr": builtin_eql,
    "raaawr": builtin_and,
    "raawwrr": builtin_or,
    "rrawwrr": builtin_not,

    # List operations
    "rraawrr": builtin_append,
    "rraawwr": builtin_insert,
    "rraawwrr": builtin_get,
    "rawwwrrr": builtin_delete,
    "raaawrrr": builtin_cat,

    # Functional
    "rawrrewr": builtin_stash,
    "rawrwrwr": builtin_recurse,
    "raaawwrr": builtin_execute,

    # IO operations
    "rraaawwrrr": builtin_print_string,
    "rraaawwwrr": builtin_print_numbers,
    #"rraaawwwrrr": builtin_read_line,

    # Types
    "rraaawwrwwr": builtin_type,
}

def execute_rawr(functions, para, word, stack, secondary_stack, persist):
    rawr = word.word
    R1s = word.R1s
    is_A = word.is_A
    As = word.As
    Ws = word.Ws
    R2s = word.R2s
    extras = word.extras
    if rawr in functions:
        execute_paragraph(functions, functions[rawr], functions[rawr], stack, secondary_stack)
        return False, True
    elif rawr in builtin_functions:
        builtin_functions[rawr](functions, para, stack, secondary_stack, persist)
        return False, True
    elif rawr == "rawwrwrr": # break
        return True, True
    elif R1s == 3 and len(extras) > 0: # constant list 
        constant = []
        constant.append(NumberItem((As - 1) * 10 + (Ws - 1) + (R2s - 1) * 100))
        for (inner_is_A, inner_As, inner_Ws, inner_Rs) in extras:
            constant.append(NumberItem((inner_As - 1) * 10 + (inner_Ws - 1) + (inner_Rs - 1) * 100))
        stack.append((persist, ListItem(constant)))
    elif R1s == 3: # constant number
        stack.append((persist, NumberItem((As - 1) * 10 + (Ws - 1) + (R2s - 1) * 100)))
    else:
        return False, False
    return False, True

def execute_paragraph(functions, para, code, main_stack, secondary_stack):
    for statement in code:
        if isinstance(statement, Sentence):
            persist = isinstance(statement, Exclamation)
            for word in statement.words:
                if isinstance(word, RawrWord):
                    brk, success = execute_rawr(functions, para, word, main_stack, secondary_stack, persist)
                    if brk:
                        return True
                    if not success:
                        flipped_word = flip_rawr(word)
                        brk, success = execute_rawr(functions, para, flipped_word, secondary_stack, main_stack, persist)
                        if brk:
                            return True
                        if not success:
                            raise ValueError("No such rawr '" + word.word + "'.")
                elif isinstance(word, LambdaWord):
                    main_stack.append((False, LambdaItem(word.sentences)))
        elif isinstance(statement, Function):
            functions[statement.name] = statement.sentences
        elif isinstance(statement, Question):
            brk = execute_paragraph(functions, para, [Period(statement.predicate)], main_stack, secondary_stack)
            if brk:
                return True
            _, result = main_stack.pop()
            if isinstance(result, NumberItem) and result.num != 0:
                brk = execute_paragraph(functions, para, [statement.body], main_stack, secondary_stack)
                if brk:
                    return True
        else:
            print(statement)
            raise RuntimeError("That wasn't supposed to happen!")
    return False


def execute_ast(ast):
    functions = {}
    main_stack = []
    secondary_stack = []
    for paragraph in ast:
        execute_paragraph(functions, paragraph, paragraph, main_stack, secondary_stack)
        main_stack = [i for i in main_stack if i[0]]
        secondary_stack = [i for i in secondary_stack if i[0]]