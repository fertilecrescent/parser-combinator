# ------ EBNF for Polish Notation ------

# POLISH: OP, EXPR+
# OP: '+' | '-' | '*' | '/'
# EXPR: '(', OP, EXPR*, ')' | NUMBER
# NUMBER: OPTIONAL_NEGATIVE, DIGIT+
# OPT_NEGATIVE: [ '-' ]
# DIGIT: '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'


# + ( 1 2)
# OP

zero = Terminal("0")
one = Terminal("1")
two = Terminal("2")
three = Terminal("3")

digit = Or(one, two, three, ...)

negative = Terminal("-")
opt_negative = ZeroOrOne(negative)

plus_digit = OneOrMore(digit)
number = Concatenate(opt_negative, plus_digit)

expression = Recursive(term=number, extend="(!)")

plus = Terminal("+")
mines = Terminal("-")
times = Terminal("*")
divide = Terminal("/")

operator = Or(plus, minus, times, divide)

polish = Concatenate(operator, expression)
