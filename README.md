# The Dialogue class

The `Dialogue` class helps testing REPLs (interactive interpreters with a Read-Eval-Print-Loop).

Given a multi-line interactive session transcript, a `Dialogue` instance emulates user interactions by offering a `fake_input` method which can replace the `input` built-in function in Python 3.

## How to use

You can code your REPL function to accept an input function as an optional argument, or you can monkey patch Python's `input` built-in. Either way, you replace the standard `input` with the `fake_input` method bound to a `Dialogue` instance. Each time it is invoked, this method will print the next prompt and fake user input from the session transcript, then return the same user input string to the REPL for processing.

The `Dialogue.session` instance attribute holds a multi-line string with all the prompts, user inputs and the outputs expected from the REPL under test. This is used to `assert` the test case.

See the `dialogue_test.py` module for two simple REPLs that exercise the `Dialogue` class.
