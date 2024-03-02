from typing import Dict, List


class Query:
    def __init__(self, query: str) -> None:
        self.type: str = query[0]
        if self.type == "check":
            self.ind: int = int(query[1])
        else:
            self.s: str = query[1]


class QueryProcessor:
    _multiplier: int = 263
    _prime: int = 1000000007

    def __init__(self, bucket_count: int) -> None:
        self.bucket_count: int = bucket_count

        self.elems: Dict[List[int]] = {}
        for i in range(self.bucket_count):
            self.elems[i] = []

    def _hash_func(self, s: str) -> int:
        ans: int = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found: bool) -> None:
        print("yes" if was_found else "no")

    def write_chain(self, chain: List) -> None:
        print(" ".join(chain))

    def read_query(self) -> Query:
        return Query(input().split())

    def process_query(self, query: Query) -> None:
        if query.type == "check":
            self.write_chain(cur for cur in reversed(self.elems[query.ind]))
        else:
            hashed: int = self._hash_func(query.s)
            try:
                ind: int = self.elems[hashed].index(query.s)
            except ValueError:
                ind = -1
            if query.type == "find":
                self.write_search_result(ind != -1)
            elif query.type == "add":
                if ind == -1:
                    self.elems[hashed].append(query.s)
            else:
                if ind != -1:
                    self.elems[hashed].pop(ind)

    def process_queries(self) -> None:
        n: int = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == "__main__":
    bucket_count: int = int(input())
    proc: QueryProcessor = QueryProcessor(bucket_count)
    proc.process_queries()
