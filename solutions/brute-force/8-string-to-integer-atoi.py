class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        is_negative = False
        order = 0
        number = 0
        number_read = False

        while i < n:     
            print(number, order, s[i])       
            if not number_read and s[i] == " ":
                i += 1
                continue

            elif not number_read and s[i] == "-":
                number_read = True
                is_negative = True
            
            elif not number_read and s[i] == "+":
                number_read = True
                        
            elif not s[i].isdigit():
                break
            
            
            else:
                number_read = True
                number *= 10
                number += int(s[i])
                order += 1
            
            if number > 0 and int(math.log(number,2)) >= 31:
                return 2**31 - 1 if not is_negative else (-2)**31
            
            i += 1

        return number * -1 if is_negative else number
