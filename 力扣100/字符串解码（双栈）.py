def decodeString(s: str) -> str:
    str_stack = []
    num_stack = []
    cur_str = ""
    num = 0

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            str_stack.append(cur_str)
            num_stack.append(num)

            num = 0
            cur_str = ""
        elif ch == ']':
            repeat_times = num_stack.pop()
            prev_str = str_stack.pop()
            cur_str = prev_str + repeat_times * cur_str
        else:
            cur_str += ch
    return cur_str

