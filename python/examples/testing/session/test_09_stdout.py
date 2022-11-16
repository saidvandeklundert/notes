from E09_testing_stdout import printer


def test_printer(capfd):
    """Test stdout"""
    printer()
    # capfd.readouterr() -> CaptureResult(out='yolocolo\n', err='')
    output = capfd.readouterr()[0].strip()

    assert output == "yolocolo"
    # assert output == "uncommentTOmakeTHISfail"
