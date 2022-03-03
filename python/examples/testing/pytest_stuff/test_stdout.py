"""
https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html
"""


def printer():
    print("yolocolo")


def test_printer(capfd):
    """Test stdout"""
    printer()
    # capfd.readouterr() -> CaptureResult(out='yolocolo\n', err='')
    output = capfd.readouterr()[0].strip()

    assert output == "yoclocolo"
    # assert output == "uncommentTOmakeTHISfail"
