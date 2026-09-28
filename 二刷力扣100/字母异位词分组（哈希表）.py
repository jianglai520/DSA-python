from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dit = defaultdict(list)  # 默认字典的值是list

    for i in strs:
        a = ''.join(sorted(i))
        dit[a].append(i)

    return list(dit.values())


# 测试
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))