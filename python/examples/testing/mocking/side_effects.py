from unittest import mock


class Token:
    def __init__(self, next_token):
        self._next_token = next_token

    @property
    def next_token(self):
        return self._next_token


def test():
    with mock.patch(
        "__main__.Token.next_token", new_callable=mock.PropertyMock
    ) as mocked_attribute:
        mocked_attribute.side_effect = [4, 5, None]
        d = Token("foo")
        print(d.next_token)
        print(d.next_token)
        print(d.next_token)


if __name__ == "__main__":
    test()
