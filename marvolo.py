from typing import List


def atomize(name: str):
    return list("^" + name + "$")


def join_groups(grouped_name: List[str], group_pair: str):
    """Join the given groups where they occur in a name.

    For example, `grouped_name=["A", "B", "C"], group_pair="AB"` gives `["AB", "C"]`.
    """
    idx = 0
    result = []
    while idx < len(grouped_name):
        if idx + 1 == len(grouped_name):
            result.append(grouped_name[idx])
            break
        if "".join(grouped_name[idx : idx + 2]) == group_pair:
            result.append(group_pair)
            idx += 2
        else:
            result.append(grouped_name[idx])
            idx += 1
    return result


def iterate_groups(grouped_name):
    return iter(grouped_name)


def iterate_group_pairs(grouped_name):
    for group_pair in zip(grouped_name[:-1], grouped_name[1:]):
        yield "".join(group_pair)
