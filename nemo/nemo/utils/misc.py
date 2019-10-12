from collections import UserDict


def pad_to(x: int, k=8) -> int:
    """Pad int value up to divisor of k.

    Examples:
        >>> pad_to(31, 8)
        32

    """

    return x + (x % k > 0) * (k - x % k)


class Config(UserDict):
    MAIN_SECTIONS = ('optimization', 'input', 'target', 'inference')

    def __init__(self, data, **kwargs):
        super().__init__(data, **kwargs)

        for section in self.MAIN_SECTIONS:
            if section not in self.data:
                self.data[section] = dict()
