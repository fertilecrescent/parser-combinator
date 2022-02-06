
# POLISH: OP, EXPR+
# OP: '+' | '-' | '*' | '/'
# EXPR: '(', OP, EXPR*, ')' | NUMBER
# NUMBER: OPTIONAL_NEGATIVE, DIGIT+
# OPT_NEGATIVE: [ '-' ]
# DIGIT: '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

# write a function for each rule
# a Rule 



class PolishParser():

    def __init__(self, program):
        self.program = program # is a list of tokens
        self.position = 0
        self.current_token = self.update_current_token()
    
    def update_current_token(self):
        self.current_token = self.program[self.position]

    def parse_op(self):
        print('parse_op')
        if self.current_token not in {'+', '-', '*', '/'}:
            raise SyntaxError('expected an operator')
        else:
            self.position += 1
            while not self.end_of_program():
                self.parse_expression()
    
    def parse_expression(self):
        print('parse_expression')
        if self.current_token != '(':
            raise SyntaxError('expected an operator')
        

current_token = program[0]


def parse_op():






if program[0] in ops_lst:
    program = program