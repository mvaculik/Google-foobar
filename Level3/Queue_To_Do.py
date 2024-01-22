def xor_sequence(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

def solution(start, length):
    
    checksum = 0
    max_id = 2000000000
    border = start + length * length

    if start < 0 or length < 0 or border > max_id:
        return None
    
    for i in range(length):
 
        segment_start = start + i * length
        segment_end = segment_start + length - i - 1

        checksum ^= xor_sequence(segment_start - 1) ^ xor_sequence(segment_end)

    return checksum