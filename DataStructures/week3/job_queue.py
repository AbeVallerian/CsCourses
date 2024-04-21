import heapq
from collections import namedtuple
from typing import List, NamedTuple, Tuple

AssignedJob: NamedTuple = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker:
    def __init__(self, start_time: int, idx: int):
        self.start_time = start_time
        self.idx = idx

    def __lt__(self, other):
        if self.start_time == other.start_time:
            return self.idx < other.idx
        return self.start_time < other.start_time


def assign_jobs(n_workers: int, jobs: List[int]) -> List[AssignedJob]:
    result: List[AssignedJob] = []
    next_free_time: List[Tuple[int, int]] = []
    for i in range(n_workers):
        heapq.heappush(next_free_time, Worker(start_time=0, idx=i))

    for job in jobs:
        next_worker: Worker = heapq.heappop(next_free_time)
        result.append(AssignedJob(next_worker.idx, next_worker.start_time))
        heapq.heappush(
            next_free_time,
            Worker(start_time=next_worker.start_time + job, idx=next_worker.idx),
        )

    return result


def test_cases() -> None:
    print(
        assign_jobs(2, [1, 2, 3, 4, 5])
        == [
            AssignedJob(0, 0),
            AssignedJob(1, 0),
            AssignedJob(0, 1),
            AssignedJob(1, 2),
            AssignedJob(0, 4),
        ]
    )
    print(
        assign_jobs(4, [1, 1, 1, 1, 1])
        == [
            AssignedJob(0, 0),
            AssignedJob(1, 0),
            AssignedJob(2, 0),
            AssignedJob(3, 0),
            AssignedJob(0, 1),
        ]
    )


def main() -> None:
    n_workers, n_jobs = map(int, input().split())
    jobs: List[int] = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)

    # test_cases()


if __name__ == "__main__":
    main()
