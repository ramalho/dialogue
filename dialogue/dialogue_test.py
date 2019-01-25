from pytest import mark

from dialogue import Dialogue, normalize


@mark.parametrize("lines, want", [
    ("a", "a"),
    ("b ", "b"),
    ("c\n", "c"),
    ("d \n", "d"),
    ("e\t \n", "e"),
    ("f \ng \n", "f\ng"),
])
def test_normalize(lines, want):
    assert want == normalize(lines)


def uppercaser(input_fn=input):
    """ This REPL outputs the user input uppercased."""
    while True:
        try:
            text = input_fn('> ')
        except EOFError:  # no more inputs
            break
        if text == 'q':  # quit
            break
        print(text.upper())


def test_uppercaser(capsys):
    dlg = Dialogue('> Xyz\nXYZ\n')
    uppercaser(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == normalize(captured.out)


@mark.parametrize("session", [
    """
    > q
    """,
    """
    > abc
    ABC
    """,
    """
    > first
    FIRST
    > second
    SECOND
    > third
    THIRD
    """,
])
def test_uppercaser_multiple(capsys, session):
    dlg = Dialogue(session)
    uppercaser(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == normalize(captured.out)


def reverser(input_fn=input):
    """ This REPL outputs the user input reversed.

        The prompt includes an incrementing index.
    """
    index = 1
    while True:
        try:
            text = input_fn(f'{index}: ')
        except EOFError:  # no more inputs
            break
        if text == 'exit':  # exit REPL
            break
        print(''.join(reversed(text)))
        index += 1


@mark.parametrize("session", [
    """
    1: exit
    """,
    """
    1: abc
    cba
    2:
    
    """,
    """
    1: 123
    321
    2: anna
    anna
    3: NaN
    NaN
    """,
])
def test_reverser(monkeypatch, capsys, session):
    dlg = Dialogue(session)
    reverser(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == normalize(captured.out)
