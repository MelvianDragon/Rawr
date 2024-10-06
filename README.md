# Rawr

**Rawr** is a dynamically typed, stack-based, concatenative-style, interpreted esoteric programming language featuring first-class functions along with file and console I/O.

In Rawr, programs are structured into paragraphs, each paragraph consisting of normal sentences (ending with a period), exclamations (ending with `!`), and questions (ending with `?`). All words in the programming language consist entirely of variations of the word _rawr_.

It is written in RPython, allowing it to be JIT-compiled. However, it can also be executed in regular Python.

## QUICK WARNING

**It is absolutely possible that there will be bugs with certain functionality, as I haven't fully tested all of the features yet.** There's also a lot of room for improvement, such as with error messages. However, you can take a look at it and play around with it a little. If _anything_ about the documentation confuses you, please message me, e-mail me, or maybe even open an issue!

## Examples

### "Hello, world!" program

```
Rrraaaaaaaawwwrawwrrawwwwwwwwwrrawwwwwwwwwrraawwrraaaaawwwwwraaaawwwraawwwwwwwwwwrraawwrraawwwwwrrawwwwwwwwwrrawrraaaawwwwr rraaawwrrr.
```

### Factorial function
```
Rawrrwwrr: Rawrr rrrawwr rrawwwr rrawwrr?
Rawrr rrrawwr rawwrr rawrwrwr raawrr.
```

Adding this as the second paragraph will use the function above to compute 15 factorial and print the result.

```
Rrraawwwwwwr rawrrwwrr rraaawwwrr.
```

### Further examples

More examples can be found in the examples folder.

## Compiling with RPython

Generally the recommended way to use Rawr, but can be a little difficult to set up.

Install PyPy first.

Then download PyPy source to get RPython:

```
curl https://downloads.python.org/pypy/pypy2.7-v7.3.17-src.tar.bz2 -o pypy2.7.tar.bz2
tar jxf pypy2.7.tar.bz2
export RPY=$(pwd)/pypy2.7-v7.3.17-src/rpython/bin/rpython
export PATH=$PATH:$(pwd)/pypy2.7-v7.3.17-src/rpython/bin
../pypy2.7-v7.3.17-src/rpython/bin/rpython --output=rawr-exe rawr/__init__.py
```

## Specification

### Program structure

A program is made up of _paragraphs_. A paragraph is a collection of _sentences_, and paragraphs are separated by two newlines. Single lines are ignored, similar to the way Markdown and other markup languages work.

Paragraphs serve two purposes in Rawr:
- The stacks are reset between paragraphs, only keeping values produced by _exclamations_. This is generally useful for managing the stacks. 
- A function definition takes up the entire paragraph.

Within paragraphs there are _sentences_, of which there are three kinds:
- **Basic sentences** end with a period (`.`) and do not do anything special except run the code that it contains. They are, however, useful for clearly defining the scope of a question.
- **Exclamations** end with an exclamation point (`!`). Any values that an exclamation puts on the stacks will persist onto the next paragraph when it's executed.
- **Questions** end with a question mark (`?`). After a question's code has been executed, the top value of the main stack determines whether the next sentence is executed or if it is skipped to the next sentence (or completed if it's the last sentence of a paragraph). If the value is a non-zero integer, then the next sentence is executed; otherwise it is skipped.

Paragraphs can be prefixed with `<word>: `, causing the entire paragraph to be defined as a function that goes by the name `<word>`. This is how named functions are defined in Rawr.

Sentences are just sequences of words, which are described shortly.

Finally, it's also possible to create _lambdas_, or anonymous functions, which are then pushed onto the stack as values. To do this, enclose a series of sentences in square brackets. Lambdas are themselves inside sentences.

### Words

All words in the program consist entirely of variations of the word _rawr_. The rules behind what is considered a valid word are very strict. Using the word _rawr_ as a basis:
1. Letters may be repeated one or more times (`rraawwrr`, `raaaaawrrr`)
2. Additional _subrawrs_ may be added at the end, which, unlike the primary rawr, do not need a vowel (`raawwrwwr`, `raaawwraaaawr`)
3. All rawrs are case-insensitive. `RAAWWWR` is the same as `raawwwr`. Rawrs can mix capitals as well (`rAwR`).
4. Rawrs may use an `e`-vowel instead, like `rewr`, which accesses the opposite stack of its corresponding `a`-vowel counterpart. Any rawr can use either stacks by swapping the vowels (`reewrewr` instead of `raawrawr`).

No other form, or any other characters, are allowed.

The language features a number of built-in rawrs, all of which are listed below. All of them can be overridden, although do so with caution.

**Constants** are specified in the code by using a rawr that uses three initial Rs. The number of each kind of letter used determines the value that is put on the stack. Utilizing subrawrs results in the creation of a list of numbers.

The formula is as follows:

```
('a'-count - 1) * 10 + ('w'-count - 1) * 1 + (last-'r'-count - 1) * 100.
```

Here are some examples:

```
rrrawr        0
rrraawr       10
rrrawwr       1
rrrawrr       100
rrrawrawr     [0, 0]
rrraaawwwwwwr 25
```

## The runtime

Rawr programs operate on values pushed and popped from two stacks: the main stack and the secondary stack. All built-in rawrs operate on the main stack; to operate on the secondary stack, use `e`-vowels instead of `a`-vowels. For instance, `rawr` swaps two values on the main stack, but `rewr` swaps two values on the secondary stack. This rule also holds for user-defined functions; if all of a function name's vowels are swapped, the resulting function will use the opposite stacks of what was originally defined.



## Built-in rawrs

```
Stack functions
- swap             rawr      b a  
- dup              rawrr     a b b
- pop              rawwr     a    
- roll             raawr     b c a
- over             raawrwr   a b a

Arithmetic
- add              rrawr     a+b
- sub              rawwrr    a-b
- mul              raawrr    a*b
- div              raawwr    a/b
- mod              rrawrr    a%b
- pos              rawrwr    +a
- neg              rawrwwr   -a

Comparison
- >                rrawwr    a>b
- >=               rraawr    a>=b
- <                rawrrr    a<b
- <=               rawwwr    a<=b
- ==               rrawwwr   a==b
- and              raaawr    a&&b
- or               raawwrr   a||b
- not              rrawwrr   !a

List operations
- append           rraawrr    ( list item       -- list      )
- insert           rraawwr    ( list index item -- list      )
- get              rraawwrr   ( list index      -- list item )
- delete           rawwwrrr   ( list index      -- list item )
- cat              raaawrrr   ( list list       -- list      )

Functional
- stash 1->2       rawrrewr   ( moves top item from main stack to secondary stack )
- stash 2->1       rewrrawr   ( moves top item from secondary stack to main stack )
- recurse          rawrwrwr   ( calls itself )
- break            rawwrwrr   ( ends a paragraph early, equivalent to "return" in most languages )
- execute          raaawwrr   Executes a function on the stack.

IO
- print_string     rraaawwrrr   ( a --      )
- print_numbers    rraaawwwrr   ( a --      )
- read_line        rraaawwwrrr  (   -- list )

Types
- type             rraaawwrwwr  a 0|1|2
```

## Notes on the code style

If you're familiar with Python, you may notice that the code for Rawr appears to do a lot of things that are unnecessary, such as wrapping values into classes before being put on a list. Much of these seemingly unnecessary decisions are due to RPython's extremely strict rules on what are considered valid programs. Keep this in mind if you plan on contributing any code, and if you _do_ make a pull request, make sure you run it through RPython before going forward.

## License

MIT License.



