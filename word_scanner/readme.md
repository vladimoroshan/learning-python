Breaking Up a Sentence

Once we have our lexicon of words, we need a way to break up sentences so that we can figure
out what they are. In our case, we’ve defi ned a sentence as “words separated by spaces,” so we
really just need to do this:

 stuff = raw_input('> ')
 words = stuff.split()
 
 
That’s really all we’ll worry about for now, but this will work really well for quite a while.

Lexicon Tuples

Once we know how to break up a sentence into words, we just have to go through the list of
words and fi gure out what “type” they are. To do that, we’re going to use a handy little Python
structure called a “tuple.” A tuple is nothing more than a list that you can’t modify. It’s created by
putting data inside two () with a comma, like a list:

 first_word = ('direction', 'north')
 second_word = ('verb', 'go')
 sentence = [first_word, second_word]
 
This creates a pair (TYPE, WORD) that lets you look at the word and do things with it.
This is just an example, but that’s basically the end result. You want to take raw input from the
user, carve it into words with split, then analyze those words to identify their type, and fi nally
make a sentence out of them.

Scanning Input

Now you are ready to write your scanner. This scanner will take a string of raw input from a user
and return a sentence that’s composed of a list of tuples with the (TOKEN, WORD) pairings. If a
word isn’t part of the lexicon, then it should still return the WORD but set the TOKEN to an error
token. These error tokens will tell users they messed up.
