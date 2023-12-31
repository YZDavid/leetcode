class Solution:
    def encode(self, strs: list[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output

    def decode(self, string: str) -> list[str]:
        output = []
        i = 1
        parsed = ""
        while i < len(string):
            char = string[i]
            prev_char = string[i-1]
            if char == "#" and prev_char.isnumeric():
                for j in range(i+1, i+1 + int(prev_char)):
                    parsed += string[j]
                output.append(parsed)
                parsed = ""
            i += 1
        return output

soln = Solution()
    
input1 = ["leet", "code", "is", "fun"]
input2 = ["l33t", "c0d3", "1s", "4w3s0m3"]
input3 = ["#1337", "#69420", "#ayylmao"]
input4 = [""]
input5 = []

encode1 = soln.encode(input1)
print(encode1)
encode2 = soln.encode(input2)
print(encode2)
encode3 = soln.encode(input3)
print(encode3)
encode4 = soln.encode(input4)
print(encode4)
encode5 = soln.encode(input5)
print(encode5)

decode1 = soln.decode(encode1)
print(decode1)
decode2 = soln.decode(encode2)
print(decode2)
decode3 = soln.decode(encode3)
print(decode3)
decode4 = soln.decode(encode4)
print(decode4)
decode5 = soln.decode(encode5)
print(decode5)