def rev_str(s):
    if len(s) == 0 or len(s) == 1:
        return s
    return s(s[:1]) + s[0]