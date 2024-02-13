from collections import namedtuple
from sys import stdin
from typing import List

Segment = namedtuple("Segment", "start end")


def to_segment(segments: List[List[int]]) -> List[Segment]:
    return map(lambda x: Segment(x[0], x[1]), segments)


def optimal_points(segments: List[Segment]) -> List[int]:
    s_segments: List[str] = []
    for s in segments:
        s_segments.append(",".join([str(s.start), str(s.end)]))

    o_segments: List[List[int]] = []
    for s in set(s_segments):
        o_segments.append([int(s.split(",")[0]), int(s.split(",")[1])])
    o_segments = sorted(o_segments, key=lambda x: (x[0], x[1]))

    single_points: List[int] = []
    points: List[int] = []
    s_end: int = -1
    for s in o_segments:
        if len(points) == 0:
            points.append(s[1])
        elif s[1] < points[-1]:
            points.pop()
            points.append(s[1])
        elif s[0] <= points[-1] <= s[1]:
            pass
        elif points[-1] < s[0]:
            points.append(s[1])

        if s[0] == s[1]:
            single_points.append(s[0])

    if s_end != -1:
        points.append(s_end)

    return sorted(list(set(points + single_points)))


def test_cases() -> None:
    print(optimal_points(to_segment([[1, 3], [2, 5], [3, 6]])) == [3])
    print(optimal_points(to_segment([[4, 7], [1, 3], [2, 5], [5, 6]])) == [3, 6])
    print(optimal_points(to_segment([[0, 1], [2, 4], [5, 5]])) == [1, 4, 5])
    print(optimal_points(to_segment([[1, 5], [2, 2]])) == [2])
    print(
        optimal_points(to_segment([[40, 42], [38, 40], [41, 41], [39, 41], [41, 42]]))
        == [40, 41]
    )


if __name__ == "__main__":
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

    # test_cases()
