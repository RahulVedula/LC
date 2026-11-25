class Solution:
    def entityParser(self, text: str) -> str:
        conversion = {"&quot;" : "\"", "&apos;" : "\'", "&amp;" : "&", "&gt;" : ">", "&lt;" : "<", "&frasl;" : "/"}
        curr_string = ""
        resulting_string = ""
        n, i = len(text), 0
        ampersand = False
        while i < n:
            if text[i] == "&":
                ampersand = True
                resulting_string += curr_string
                curr_string = "&"
            elif ampersand and (curr_string + text[i]) in conversion:
                resulting_string += conversion[curr_string + text[i]]
                curr_string = ""
            else:
                curr_string += text[i]

            i += 1
        resulting_string += curr_string
        return resulting_string