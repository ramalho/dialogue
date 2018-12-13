# REPLs and the Dialogue class

The programs in this repository show how to build and test a REPL (Read-Eval-Print-Loop, the core loop of an interactive interpreter).

## The Dialogue testing class

The most complicated code here is the `Dialogue` class, designed for testing REPLs. Given a multi-line interactive session transcript, a `Dialogue` instance emulates user interactions by offering a `fake_input` method which can mock the `input` built-in function in Python 3. Monkey-patching the `input` built-in before running a REPL will feed it with fake user inputs from a session transcript.

Each time the REPL calls `input`, the `fake_input` mock will print a prompt and a fake user input, then return the same user input string to the REPL for processing.

The `transcript` method returns a multi-line string with all the prompts, user inputs and the outputs expected from the REPL under test. See the `dialogue_test.py` module for two simple REPLs that exercise the `Dialogue` class.

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

> My father, Jairo Ramalho, liked to say that an adding machine with paper tape is much better than a handheld calculator or calculator app that only shows one number at a time. With the adding machine you can easily double check the numbers on the paper tape. My father would enjoy using `adder.py`.

![Adding machine](adding-machine-500x.jpg "Adding machine with paper tape.")
