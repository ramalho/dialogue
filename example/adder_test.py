from pytest import mark

from dialogue import Dialogue, normalize

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
def test_adder(capsys, session):
    dlg = Dialogue(session)
    adder(dlg.fake_input)
    captured = capsys.readouterr()
    assert dlg.session == normalize(captured.out)
