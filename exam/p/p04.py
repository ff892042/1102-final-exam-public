def p04(input=2):
    output_list=None
    # ↓程式區域↓

    class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(idx, temp):
            if idx == len(digits):
                ret.append(temp)
            else:
                digit = digits[idx]
                for c in num_map[digit]:
                    temp += c
                    dfs(idx + 1, temp)
                    # 移除计算过的数
                    temp = temp[:-1]

        temp = ""
        ret = []
        dfs(0, temp)
        return ret
    # ↑程式區域↑
    return output_list
