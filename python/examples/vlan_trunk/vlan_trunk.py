from typing import List
from itertools import groupby


def vlan_range_string(vland_ids: List[int]) -> str:
    range_strings = list()

    for _, num_gen in groupby(enumerate(vland_ids), key=lambda x: x[0] - x[1]):
        num_list = [item[1] for item in num_gen]
        first, last = num_list[0], num_list[-1]
        range_strings.append(str(first) if first == last else f"{first}-{last}")

    return ",".join(range_strings)


if __name__ == "__main__":
    print(vlan_range_string([1, 2, 3, 201]))
    print(vlan_range_string([1, 2, 3, 4, 10, 11, 12, 200, 201]))
