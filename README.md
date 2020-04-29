Welcome to Sutakku!

This is a simple concatenative stack based language I tried to create about six months ago in C, but ran into debugging issues. I decided to rewrite it in python so that I could actually get it working and make sure it would be worth rewriting a "real" interpreter in  C. It also helped me organize the structure of the program better. I guess you could call this the prototype.

Anyway, like I already kind of mentioned, this is a simple concatenative stack based interpreted language. It uses postfix notation like Forth. It is weakly typed with some implicit type conversion. I'm sure the typing is somewhat inconsistent, and needs to be tweaked. It's basically a toy lanuage I made for my own edification. I doubt anyone will find it useful, but I can dream.

Let's get into actually using the language. When the interpreter starts, you have the prompt and one empty stack, named 'main.' In Sutakku, you can have any number of stacks. (We'll get to that later)

First, you can quit at any time by entering `bye` all by itself. This and only this is the only thing that can't be redefined.

```
Welcome to Sutakku (Python)
Copyright 2020 SpaceBudokan
This program comes with ABSOLUTELY NO WARRANTY; This is free software, and you are welcome to redistribute it under certain conditions.

I'm so glad you're here!
Type "bye" to Exit
main>bye
Goodbye! I'll miss you...
```

Second, comments go in parentheses. They will simply be ignored.

```
main>(Anything in parentheses like this is a comment and will be ignored)
main>
```

The different objects on the stack(s) are called 'atoms.' To push some atoms onto the stack, type them at the prompt separated by spaces. you can enter strings onto the stack. They must be 'quoted' using squared brackets ('[' and ']'.) You can nest these to create quotes within quotes. Anything not quoted is evaluated. If the atom has not been defined to something else, integers evaluate to INT type, floating point numbers evaluate to FLT, and strings call builtin functions or defined macros.

```
main>1 2 3.0 [this is a string] [this is a quote [nested in another] quote]
```

To see the entire stack, use `pstack`

```
main>pstack
main:
0:STR	this is a quote [nested in another] quote
1:STR	this is a string
2:FLT	3.0
3:INT	2
4:INT	1
```

To just see the top element of the stack, use `top`

```
main>top
this is a quote [nested in another] quote
```

`pop` removes the top element of the stack
```
main>pstack
main:
0:STR	rabbit
1:STR	monkey
2:STR	horse
main>pop
main>pstack
main:
0:STR	monkey
1:STR	horse
```

Of course the basic math operators are here. `+ - * /` all work as expected

```
main>1 2 + top
3
main>3 2 - top
1
main>2 2 * top
4
main>6 2 / top
3
```

In Sutakku, integer 0 is false, and anything else is true. Greater than (>) and less than (<) must both be of a numerical (integer or float) type, OR both be of string type. Equality (=) checks both the type and content of an atom.

```
main>2 1 > top
1
main>1 2 > top
0
main>2 1 < top
0
main>2 1 > top
1
main>[1] [1] = top
1
main> 1 1 = top
1
main>1 [1] = top
0
```

The 'dup' function simply duplicates the top item on the stack.

```
main>1 pstack
main:
0:INT	1
main>dup pstack
main:
0:INT	1
1:INT	1
main>
```

`if then` statements are simple. you start with an `if` the atoms to evaluate if true, then finish is with `then`. If the top atom of the stack is true (i.e. notinteger 0) then the atoms are evaluated. If the top atom is false, everything between the `if` and `then` atoms is skipped. They can be nested.

```
main>1 if [this will be evaluated] 0 if [this will not be evaluated] then then
main>pstack
main:
0:STR	this will be evaluated
```

The `eval` function evaluates an atom as if you had typed it at the prompt.

```
main>[1 1 +] pstack
main:
0:STR	1 1 +
main>eval pstack
main:
0:INT	2
```

`cat` concatenatesthe top two atoms, whatever they may be, and places them on the stack as a string. (In this example, the concatenated string can be converted to an INT by evaluating it)

```
main> 1 2 pstack
main:
0:INT	2
1:INT	1
main>cat pstack
main:
0:STR	12
main>eval pstack
main:
0:INT	12
```

`atomize` is a special function that takes the top atom, parses it as if it were typed at the prompt, but does not evaluate the resulting atoms. Instead they are placed on the stack as strings.

```
main>[1 2 3 [a string] cat] pstack
main:
0:STR	1 2 3 [a string] cat
main>atomize pstack
main:
0:STR	cat
1:STR	[a string]
2:STR	3
3:STR	2
4:STR	1
```

`pull` and `bury` are two stack manipulation functions. `pull` take the specified atom and places it on the top of the stack. `bury` takes the top of the stack and makes it the atom specified. the index of the stack atoms are determined after `pull` or `bury` have consumed the top atom of the stack.
You'll notice there is no `swap` function. We will return to this later.

```
main>[apple] [orange] [banana] [kiwano horned melon] [jackfruit] pstack
main:
0:STR	jackfruit
1:STR	kiwano horned melon
2:STR	banana
3:STR	orange
4:STR	apple
main>3 pull pstack
main:
0:STR	orange
1:STR	jackfruit
2:STR	kiwano horned melon
3:STR	banana
4:STR	apple
main>2 bury pstack
main:
0:STR	jackfruit
1:STR	kiwano horned melon
2:STR	orange
3:STR	banana
4:STR	apple
```

To create another stack, use `newstack`. This will create a new empty stack using the top atom as the name of the stack. To switch to that stack, use `stack`. These functions will automatically treat numerical input as a string.

```
main>[beer] newstack
main>[beer] stack
beer>[pilsener] [IPA] [steam] [hefeweizen]
beer>
```

`to` consumes the top atom as the target stack and pops the (new) top item of the urrent stack and pushes it to the target stack. Similarly, `from` pops the top item from the target stack and pushes it onto the current stack.

```
beer>[main] stack
main>pstack
main:
0:STR	steam
1:STR	hefeweizen
main>[beer] from pstack
main:
0:STR	IPA
1:STR	steam
2:STR	hefeweizen
```

Last, but definitely not least, is `define`. This function defines a macro. You can define any atom to be ANY other atom. Sutakku does not have functions other than the built in function, merely macros. The top of the stack is the atom to be redfined, and the next atom is the definition. When the defined atom is encountered, the definnition will be evaluated as if it was typed at the prompt. There is no checking for recursive definitions, be careful. It is easy to define an atom to be itself and make python displeased with you.

```
main>[[This just prints this sentence.] top pop] [sentence] define
main>sentence
This just prints this sentence.
main>(now let's define a swap macro)
main>[1 pull] [swap] define
main>[red] [blue] pstack
main:
0:STR	blue
1:STR	red
main>swap pstack
main:
0:STR	red
1:STR	blue
main>(Now let's do the dumb shit and redefine a nuber to be a string)
main>[[farts]] [1] define
main>1 pstack
main:
0:STR	farts
```

This concludes your introduction to Sutakku. If you spot any errors, please let me know. If there is something that should be a function that isn't, please let me know. I don't plan on adding file handling until the C version. Other than that, I'm open to suggestions.
