"""
In the protocol being used by the Elves, the start of a
 packet is indicated by a sequence of four characters that are all different.

your subroutine needs to identify the first position where the four
 most recently received characters were all different. Specifically, 
 it needs to report the number of characters from the beginning of the buffer 
 to the end of the first such four-character marker.

Here are a few more examples:
  mjqjpqmgbljsphdztnvjfqwrcgsmlb 7 ( jpqm )
  bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
  nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
  nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
  zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

"""
with open("input_6.txt", "rt") as f:
    assignment = f.read()
signals: list[str] = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
    assignment,
]


def find_end_of_signal(signal) -> None:
    scan_start: int = 0
    scan_end: int = 4
    end_of_signal = len(signal)
    while scan_end <= end_of_signal:
        to_scan = signal[scan_start:scan_end]
        # print(to_scan)
        if unique(to_scan):
            print(f"signal starting position is {scan_end}")
            return
        scan_start += 1
        scan_end += 1
    return


def unique(sequence: str) -> bool:
    seen: dict[str, bool] = {}
    for char in sequence:
        if seen.get(char):
            return False
        else:
            seen[char] = True
    return True


for signal in signals:
    find_end_of_signal(signal=signal)

"""

    your subroutine needs to identify the first position where the 14
        most recently received characters were all different.
        
    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

"""


def find_end_of_signal_part_2(signal):
    scan_start: int = 0
    scan_end: int = 14
    end_of_signal = len(signal)
    while scan_end <= end_of_signal:
        to_scan = signal[scan_start:scan_end]
        # print(to_scan)
        if unique(to_scan):
            print(f"signal starting position is {scan_end}")
            return
        scan_start += 1
        scan_end += 1
    return


for signal in signals:
    find_end_of_signal_part_2(signal=signal)
