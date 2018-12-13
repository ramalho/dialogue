# REPLs and the Dialogue class

The programs in this repository show how to build and test a REPL (Read-Eval-Print-Loop, the core loop of an interactive interpreter).


## The Dialogue testing class

The most complicated code here is the `Dialogue` class, designed for testing REPLs. Given a multi-line interactive session transcript, a `Dialogue` instance emulates user interactions by offering a `fake_input` method which can replace the `input` built-in function in Python 3.

Each of the REPLs here takes an input function as an optional argument, defaulting to `input`. To test, invoke the REPL with a `fake_input` method bound to a `Dialogue` instance. This method will print a prompt and a fake user input, then return the same user input string to the REPL for processing.

The `Dialogue.session` instance attribute holds a multi-line string with all the prompts, user inputs and the outputs expected from the REPL under test. This is used to `assert` the test case.

See the `dialogue_test.py` module for two simple REPLs that exercise the `Dialogue` class.


## An adding machine REPL

A more interesting REPL example is `adder.py`, which can be used from the command line. It's a "adding machine" that does just that: it adds numbers — the most common use of traditional desktop adding machines with paper tape. The file `adder_test.py` is another example of using `Dialogue`.

Here is an `adder.py` session from start to finish:

```
$ ./adder.py 
Enter 0 to quit.
[1] 10
10.0
[2] 22.5
32.5
[3] 17.97
50.47
[4] zzz
Please type numbers.
[4] 33.05
83.52
[5] 0
$
```

> My father, Jairo Ramalho, liked to say that an adding machine with paper tape is much better than a handheld calculator or calculator app that only shows one number at a time. With the adding machine you can easily double check the numbers on the paper tape. Jairo would enjoy using `adder.py`.

![Adding machine](adding-machine-500x.jpg "Adding machine with paper tape.")
