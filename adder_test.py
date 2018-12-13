from pytest import mark

from dialogue import Dialogue

from adder import adder


@mark.parametrize("session", [
    """
    Enter 0 to quit.
    [1] 0
    """,
    """
    Enter 0 to quit.
    [1] 1
    1.0
    """,
    """
    Enter 0 to quit.
    [1] 11
    11.0
    [2] 22
    33.0
    [3] 33.9
    66.9
    """,
    """
    Enter 0 to quit.
    [1] z
    Please type numbers.
    [1] 3
    3.0
    [2] 4
    7.0
    """,
])
def test_adder(monkeypatch, capsys, session):
    dlg = Dialogue(session)
    with monkeypatch.context() as m:
        m.setitem(__builtins__, "input", dlg.fake_input)
        adder()
    captured = capsys.readouterr()
    assert dlg.transcript() == captured.out
