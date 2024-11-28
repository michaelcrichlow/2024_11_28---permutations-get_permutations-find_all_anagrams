def get_permutations(s: str):
    # base case
    if len(s) == 1:
        return [s]

    # recursive case
    permutations = []
    head = s[0]
    tail = s[1:]
    tail_permutaions = get_permutations(tail)

    # two for loops
    for val in tail_permutaions:
        for i in range(len(val) + 1):
            new_perm = val[:i] + head + val[i:]
            permutations.append(new_perm)

    # return permutations
    permutations.sort()
    return permutations


def find_all_anagrams(s1: str, s2: str) -> list[int]:
    list_of_permutations = get_permutations(s2)
    local_array = []

    for i in range(0, len(s1) - len(s2)):
        if s1[i:i + len(s2)] in list_of_permutations:
            local_array.append(i)

    return local_array


def main() -> None:
    print(find_all_anagrams('cbaebabacd', 'abc'))


if __name__ == '__main__':
    main()
