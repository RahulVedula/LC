class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        number_stack = []

        for token in tokens:
            if token not in "+-/*":
                number_stack.append(token)
                continue
            
            number_2 = int(number_stack.pop())
            number_1 = int(number_stack.pop())

            if token == "+":
                immediate = number_1 + number_2
            elif token == "-":
                immediate = number_1 - number_2
            elif token == "/":
                magnitude = -1
                immediate = abs(number_1)//abs(number_2)
                if (number_1 >= 0 and number_2 >= 0) or (number_1 < 0 and number_2 < 0): magnitude = 1
                immediate *= magnitude
            elif token == "*":
                immediate = number_1 * number_2
            
            number_stack.append(immediate)
        
        return int(number_stack[0])
            

        