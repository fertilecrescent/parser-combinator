
# POLISH: OP, EXPR+
# EXPR: '(', OP, EXPR*, ')' | NUMBER
# OP: '+ ' | '- ' | '* ' | '/ '
# NUMBER: OPTIONAL_NEGATIVE, DIGIT+
# OPT_NEGATIVE: [ '-' ]
# DIGIT: '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

def digit(x):
    clean = x
    x = x.lstrip()
    if x[0] in set('123456789'):
        return True, x[1:]
    return False, clean

def opt_negative(x):
    clean = x
    x = x.lstrip()
    if x[0] == '-':
        return True, x[1:]
    else:
        return True, x[0:]

def number(x):
    clean = x
    x = x.lstrip()
    x = opt_negative(x)[1]
    is_digit, x = digit(x)
    if not is_digit:
        return False, clean
    while is_digit:
        is_digit, x = digit(x)
    return True, x

def op(x):
    clean = x
    x = x.lstrip()
    if x[0] in set ('+-*/') and x[1] == ' ':
        return True, x[2:]
    else:
        return False, clean

def expr(x):
    clean = x
    x = x.lstrip()

    is_number, x = number(x)
    if is_number:
        return is_number, x
    else:
        x = clean.lstrip()

    if not x[0] == '(':
        print(x)
        print(x[0])
        print('bye 1')
        return False, clean
    
    x = x[1:]

    is_op, x = op(x)
    if not is_op:
        print(x)
        print('bye 2')
        return False, clean

    is_expr, x = expr(x)
    if not is_expr:
        print(x)
        print('bye 3')
        return False, clean

    while is_expr:
        is_expr, x = expr(x)
    
    if x[0] != ')':
        print(x)
        print('bye 4')
        return False, clean

    return True, x[1:]    




assert digit('1dfasdf') == (True, 'dfasdf')
assert digit('xdsafdsafs') == (False, 'xdsafdsafs')
assert opt_negative('-dsasdfa') == (True, 'dsasdfa')
assert opt_negative('dsasfd') == (True, 'dsasfd')
assert number('123dasfd') == (True, 'dasfd')
assert number('-123dasfd') == (True, 'dasfd')
assert number('dsasdfdsaf') == (False, 'dsasdfdsaf')
assert number('-dsasdfdsaf') == (False, '-dsasdfdsaf')
assert op('+fdsasdf') == (False, '+fdsasdf')
assert op('+ 12321') == (True, '12321')
assert expr('(+ 12 123 (+ 12 123))') == (True, '')
assert expr('(+ 12 123 (+ 12 123)) dasdfas') == (True, ' dasdfas')
assert expr('(+ 12 123 (+ 12 123))') == (False, '(+ 12 123 (+ 12 123)')

print('tests passed')