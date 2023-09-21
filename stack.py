class Stack:
    def __init__(self):
        self.top = -1
        self.stack = [0] * 22

    def push(self, value):
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        data=self.stack[self.top]
        self.top-=1
        return data


    def peek(self):
        return self.stack[self.top]

    def size(self):
        return self.top + 1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    def display(self):
        print('[ ', end='')
        for i in range(self.size()):
            print(self.stack[i] , end='')
        print(' ] ', end=' ')

def is_operator(char):
    return char in {'+', '-', '*', '/','^','(',')'}

def precedence(op):
    if op in {'+', '-'}:
        return 1
    elif op in {'*', '/'}:
        return 2
    elif op in {'^'}:
        return 3
    return 0


def infix_to_postfix(expression):
    result = []
    stack = Stack()

    for char in expression:

        if not is_operator(char):
            result += char
        elif is_operator(char) and char==')':
            while stack.peek()!='(':
                result+=stack.pop()
            stack.pop()

        elif is_operator(char):

            if precedence(char)>0:
                if precedence(char) <= precedence(stack.peek()):
                    while precedence(char) <= precedence(stack.peek()):
                        result+=stack.pop()
                    stack.push(char)

                elif precedence(char) > precedence(stack.peek()):
                    stack.push(char)
            else:
                stack.push(char)
        print('stack = ' , end='')
        stack.display()

        print('\tResult = ',result, end='\n')



    while not stack.is_empty():
        result.append(stack.pop())
        print('stack = ', end='')
        stack.display()

        print('\tResult = ', result, end='\n')

    return ''.join(result)

########################################################### MAIN ####

infix_expression = "A+B*C/(E-F)"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
