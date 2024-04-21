from typing import List, Tuple


class Database:
    def __init__(self, row_counts: List[int]) -> None:
        self.row_counts: List[int] = row_counts
        self.max_row_count: int = max(row_counts)
        n_tables: int = len(row_counts)
        self.ranks: List[int] = [0] * n_tables
        self.parents: List[int] = list(range(n_tables))

    def merge(self, src: int, dst: int) -> bool:
        src_parent: int = self.get_parent(src)
        dst_parent: int = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] = (
                self.row_counts[dst_parent] + self.row_counts[src_parent]
            )
            self.max_row_count = max(self.max_row_count, self.row_counts[src_parent])
        elif self.ranks[src_parent] == self.ranks[dst_parent]:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] = (
                self.row_counts[dst_parent] + self.row_counts[src_parent]
            )
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])
            self.ranks[dst_parent] += 1
        else:
            self.parents[src_parent] = dst_parent
            self.row_counts[dst_parent] = (
                self.row_counts[dst_parent] + self.row_counts[src_parent]
            )
            self.max_row_count = max(self.max_row_count, self.row_counts[dst_parent])

        return True

    def get_parent(self, table: int) -> int:
        # find parent and compress path
        if self.parents[table] == table:
            return table
        else:
            return self.get_parent(self.parents[table])


def test_cases() -> None:
    db1: Database = Database([1, 1, 1, 1, 1])
    queries1: List[Tuple[int, int]] = [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)]
    max_row_count1: List[int] = []
    for q in queries1:
        db1.merge(q[0] - 1, q[1] - 1)
        max_row_count1.append(db1.max_row_count)
    assert max_row_count1 == [2, 2, 3, 5, 5]

    db2: Database = Database([10, 0, 5, 0, 3, 3])
    queries2: List[Tuple[int, int]] = [(6, 6), (6, 5), (5, 4), (4, 3)]
    max_row_count2: List[int] = []
    for q in queries2:
        db2.merge(q[0] - 1, q[1] - 1)
        max_row_count2.append(db2.max_row_count)
    assert max_row_count2 == [10, 10, 10, 11]


def main() -> None:
    n_tables, n_queries = map(int, input().split())
    counts: List[int] = list(map(int, input().split()))
    assert len(counts) == n_tables
    db: Database = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
    # test_cases()
