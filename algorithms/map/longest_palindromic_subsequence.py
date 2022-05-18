def longest_palindromic_subsequence(s):

    k = len(s)
    o_list = [0] * k    # 申请长度为n的列表，并初始化
    n_list = [0] * k    # 同上
    longest_sub_str = ""
    longest_len = 0

    for j in range(0, k):
        for i in range(0, j + 1):
            if j - i <= 1:
                if s[i] == s[j]:
                    n_list[i] = 1                 # 当 j 时，第 i 个子串为回文子串
                    len_t = j - i + 1
                    if longest_len < len_t:        # 判断长度
                        longest_sub_str = s[i:j + 1]
                        longest_len = len_t
            else:
                if s[i] == s[j] and o_list[i+1]:   # 当j-i>1时，判断s[i]是否等于s[j]，并判断当j-1时，第i+1个子串是否为回文子串
                    n_list[i] = 1                  # 当 j 时，第 i 个子串为回文子串
                    len_t = j - i + 1
                    if longest_len < len_t:
                        longest_sub_str = s[i:j + 1]
                        longest_len = len_t
        o_list = n_list                            # 覆盖旧的列表
        n_list = [0] * k                          # 新的列表清空
    # ~ from icecream import ic
    # ~ ic(s, logestSubStr)
    return longest_len#, longest_sub_str
