"""给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]
"""

from typing import List
from collections import defaultdict

# strs = ["eat"]
#
# a = []
#
# a.append(list(strs))
# print(a)

def groupAnagrams( strs: List[str]) -> List[List[str]]:
    dit = defaultdict(list)  # 字典，当访问不存在的键时，自动创建一个空列表作为该键的值

    for i in strs:
        a = "".join(sorted(i))
        dit[a].append(i)
    # for key, value in dit.items():
    #     print(key, value)
    return list(dit.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

