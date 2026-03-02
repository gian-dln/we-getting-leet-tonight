def plusOne(digits: list[int]) -> list[int]:
    for i in range (len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        if digits[i-1] == 9:
            continue
        elif digits[i-1]!= 0:
            digits[i-1] += 1
            return digits
        else:
         digits = [1] + digits
    return digits

