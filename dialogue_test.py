from pytest import mark

from dialogue import Dialogue


def uppercaser():
    """ This REPL outputs the user input uppercased."""
    while True:
        try:
            text = input('> ')
        except EOFError:  # no more inputs
            break
        if text == 'q':  # quit
            break
        print(text.upper())


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
def test_uppercaser(monkeypatch, capsys, session):
    dlg = Dialogue(session)
    with monkeypatch.context() as m:
        m.setitem(__builtins__, "input", dlg.fake_input)
        uppercaser()
    captured = capsys.readouterr()
    assert dlg.transcript() == captured.out


def reverser():
    """ This REPL outputs the user input reversed.

        The prompt includes an incrementing index.
    """
    index = 1
    while True:
        try:
            text = input(f'{index}: ')
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
    with monkeypatch.context() as m:
        m.setitem(__builtins__, "input", dlg.fake_input)
        reverser()
    captured = capsys.readouterr()
    assert dlg.transcript() == captured.out
