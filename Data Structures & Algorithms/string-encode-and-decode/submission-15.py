class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""

        result = ""
        for s in strs:
            # ex: 5#hello
            result += f"{str(len(s))}#{s}"

        return result

    def decode(self, s: str) -> List[str]:
        if s == "": return []

        result = []
        i = 0
        while i < len(s) - 1:
            lengthIndex = i
            lengthAsStr = ""
            # seek forward, handle case where length's
            # num of digits is more than 1
            while True:
                if s[lengthIndex] != "#":
                    lengthAsStr += s[lengthIndex]
                    lengthIndex += 1
                else:
                    break

            substrLen = int(lengthAsStr)

            if substrLen == 0:
                result.append("")
            else:
                # when substring-ing, start at i,
                # skip the substring length value
                # and the delimiter "#"
                substr = s[i + len(lengthAsStr) + 1 : i + len(lengthAsStr) + substrLen + 1]
                result.append(substr)
            # go to next length value in string
            i += len(lengthAsStr) + substrLen + 1

        return result