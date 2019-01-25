import textwrap
from typing import Iterator

def normalize(lines: str) -> str:
	""" Remove trailing whitespace from each line, 
	    keeping all line breaks except the last."""

	return '\n'.join(line.rstrip() for line in lines.strip().splitlines())


class Dialogue():
    """ ``Dialogue`` allows testing of text-based interactions or REPLs.

        A ``Dialogue`` instance is created with a session argument: a
        multi-line string with prompts, user inputs and expected outputs.
        Each time the ``fake_input`` method is called, it emulates the
        Python 3 ``input`` built-in function by printing a prompt, then
        a user input, and returning that input. Therefore, ``fake_input``
        can be used to mock ``input``, providing pre-recorded "user"
        inputs to the REPL under test.
    """

    session: str
    input_line_gen: Iterator[str]
    prompt: str

    def __init__(self, session: str):
        # dedent session given as indented string (see tests)
        self.session = normalize(textwrap.dedent(session))
        self.input_line_gen = iter(self)
        self.prompt = ''

    def __iter__(self):
        for line in self.session.splitlines():
            if line.startswith(self.prompt.rstrip()):
                yield line[len(self.prompt):].rstrip()

    def fake_input(self, prompt: str) -> str:
        """Use this method to mock the ``input`` built-in."""
        self.prompt = prompt
        try:
            line = next(self.input_line_gen)
        except StopIteration:
            raise EOFError()
        print(prompt + line)
        return line
