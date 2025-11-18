def numRepeatMult(num, repeat):
    nums = []
    s = ""
    for _ in range(repeat):
        s += str(num)
        nums.append(int(s))
    expr = " × ".join(str(n) for n in nums)

    result = 1
    for n in nums:
        result *= n
    return f"{expr} = {result}"


print(numRepeatMult(1, 6))
