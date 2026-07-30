from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    map = defaultdict(list)

    for s in strs:
        count = [0] * 26 #a-z

        for c in s:  #count sort
            count[ord(c) - ord('a')] += 1

        map[tuple(count)].append(s)


    return list(map.values())

