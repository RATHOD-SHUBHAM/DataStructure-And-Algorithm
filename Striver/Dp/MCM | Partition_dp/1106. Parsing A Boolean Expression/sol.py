class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operator = []
        operand = []

        for char in expression:
            
            if char == ')':
                values = []

                while operand[-1] != '(':
                    # pop out all the values for this bracket
                    values.append(operand.pop())
                
                # remove the '('
                operand.pop()

                # get the operator for this bracker/subsequence
                op = operator.pop()

                result = self.evaluate(values, op)

                operand.append(result)
            
            elif char == ",":
                continue
            
            elif char == '&' or char == '|' or char == '!':
                operator.append(char)
            
            else:
                operand.append(char)
        

        return True if operand[-1] == 't' else False

    def evaluate(self, values, op):
        if op == "!":
            if values[0] == 't':
                return 'f'
            else:
                return 't'
        
        elif op == '|':
            if 't' in values:
                return 't'
            else:
                return 'f'
        
        elif op == '&':
            if 'f' in values:
                return 'f'
            else:
                return 't'