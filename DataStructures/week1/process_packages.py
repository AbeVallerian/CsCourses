from collections import namedtuple
from typing import List, NamedTuple

Request: NamedTuple = namedtuple("Request", ["arrived_at", "time_to_process"])
Response: NamedTuple = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.finish_time: List[int] = []

    def process(self, request: Request) -> Response:
        if self.finish_time and self.finish_time[-1] <= request.arrived_at:
            self.finish_time = []
        else:
            while self.finish_time and self.finish_time[0] <= request.arrived_at:
                self.finish_time.pop(0)
        # self.finish_time = list(
        #     filter(lambda t: t > request.arrived_at, self.finish_time)
        # )
        if len(self.finish_time) == 0:
            self.finish_time.append(request.arrived_at + request.time_to_process)
            return Response(False, request.arrived_at)
        if len(self.finish_time) < self.size:
            if self.finish_time[-1] > request.arrived_at:
                self.finish_time.append(self.finish_time[-1] + request.time_to_process)
                return Response(False, self.finish_time[-2])
            else:
                self.finish_time.append(request.arrived_at + request.time_to_process)
                return Response(False, request.arrived_at)
        else:
            return Response(True, request.arrived_at)


def process_requests(requests: List[Request], buffer: Buffer) -> List[Response]:
    responses: List[Response] = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def test_cases() -> None:
    print(process_requests([], Buffer(1)) == [])
    print(process_requests([Request(0, 0)], Buffer(1)) == [Response(False, 0)])
    print(
        process_requests(
            [
                Request(0, 1),
                Request(0, 1),
            ],
            Buffer(1),
        )
        == [
            Response(False, 0),
            Response(True, 0),
        ]
    )
    print(
        process_requests(
            [
                Request(0, 1),
                Request(1, 1),
            ],
            Buffer(1),
        )
        == [
            Response(False, 0),
            Response(False, 1),
        ]
    )
    print(
        process_requests(
            [
                Request(0, 1),
                Request(0, 1),
            ],
            Buffer(2),
        )
        == [
            Response(False, 0),
            Response(False, 1),
        ]
    )


def main() -> None:
    buffer_size, n_requests = map(int, input().split())
    requests: List[Request] = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer: Buffer = Buffer(buffer_size)
    responses: List[Response] = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)

    # test_cases()


if __name__ == "__main__":
    main()
