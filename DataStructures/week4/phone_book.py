from typing import Dict, List

HASH_SIZE: int = 1000


class Query:
    def __init__(self, query: List[str]):
        self.type: str = query[0]
        self.number: int = int(query[1])
        if self.type == "add":
            self.name: str = query[2]


def read_queries() -> List[Query]:
    n: int = int(input())
    return [Query(input().split()) for _ in range(n)]


def write_responses(result: List[str]) -> None:
    print("\n".join(result))


def process_queries(queries: List[Query]) -> List[str]:
    result: List[str] = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts: Dict[Query] = {}
    for cur_query in queries:
        hash_contact: int = abs(hash(str(cur_query.number))) % HASH_SIZE
        if cur_query.type == "add":
            # if we already have contact with such number,
            # we should rewrite contact's name
            if hash_contact not in contacts:
                contacts[hash_contact] = [cur_query]
            elif len(contacts[hash_contact]) == 0:
                contacts[hash_contact] = [cur_query]
            else:
                is_found: bool = False
                for j in range(len(contacts[hash_contact])):
                    if contacts[hash_contact][j].number == cur_query.number:
                        contacts[hash_contact].pop(j)
                        contacts[hash_contact].append(cur_query)
                        is_found = True
                        break
                if not is_found:
                    contacts[hash_contact].append(cur_query)
        elif cur_query.type == "del":
            if hash_contact not in contacts:
                pass
            elif len(contacts[hash_contact]) == 0:
                pass
            else:
                for j in range(len(contacts[hash_contact])):
                    if contacts[hash_contact][j].number == cur_query.number:
                        contacts[hash_contact].pop(j)
                        break
        else:
            response: str = "not found"
            if hash_contact not in contacts:
                pass
            elif len(contacts[hash_contact]) == 0:
                pass
            else:
                for contact in contacts[hash_contact]:
                    if contact.number == cur_query.number:
                        response = contact.name
                        break
            result.append(response)
    return result


def test_cases() -> None:
    queries: List[str] = [
        "add 911 police",
        "add 76213 Mom",
        "add 17239 Bob",
        "find 76213",
        "find 910",
        "find 911",
    ]
    print(process_queries(list(map(lambda x: Query(x.split()), queries))))


if __name__ == "__main__":
    write_responses(process_queries(read_queries()))

    # test_cases()
