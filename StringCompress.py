def string_compress(s: str) -> str:
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))
    compressed_str = ''.join(compressed)

    if len(compressed_str) < len(s):
        return compressed_str
    else:
        return s
    
input_str1 = "aabcccccaaa"
print(string_compress(input_str1))
input_str2 = "tttttkkaytt"
print(string_compress(input_str2))
input_str3 = "abcdefg"
print(string_compress(input_str3))
