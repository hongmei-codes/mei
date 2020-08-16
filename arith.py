def tokenize(expr):
    """To tokenize user expression by moving past whitespaces and return tokens as a list"""

    tokens = expr.split()
    return tokens


def parentheses_balance_check(tokens):
    """To check if parentheses are balanced. If unbalanced, print error message"""
    current_token = 0
    l_count = 0  # left parentheses count
    r_count = 0  # right parentheses count

    # check if parentheses are balanced
    for t in tokens:
        current_token += 1

        if t == '(':
            l_count += 1

        if t == ')':
            r_count -= 1
            if l_count + r_count < 0:  # excess ')'
                if r_count == -1:  # when the first token is ')'
                    error_token = current_token - 1
                    # print error message
                    left_expr = ' '.join(tokens[:error_token])
                    right_expr = ' '.join(tokens[error_token:])
                    print(f'Unexpected right parenthesis between {left_expr} and {right_expr}')
                    return
                else:  # r_count != 1, the first token is not ')'
                    error_token = current_token - 1
                    # print error message
                    left_expr = ' '.join(tokens[:error_token])
                    right_expr = ' '.join(tokens[error_token:])
                    print(f'Unexpected right parenthesis between {left_expr} and {right_expr}')
                    return

            if l_count + r_count > 0:  # excess '('
                unclosed = l_count + r_count
                if current_token != len(tokens):
                    continue  # to loop through rest of elements in list
                # print error message
                expr = ' '.join(tokens)
                if unclosed == 1:
                    print(f'There is {unclosed} unclosed left parenthesis in {expr}')
                    return
                else:
                    print(f'There are {unclosed} unclosed left parentheses in {expr}')
                    return

    if l_count + r_count == 0:  # parenthesis are balanced
        return True  # True meaning yes, parenthesis are balanced


def opd_opr_check(tokens):
    """To check if operands and operators are valid. If not, print error message"""

    # check if operands and operators are valid
    op = ['+', '-', '/', '//', '*']
    current_token = 0
    num_count = 0
    op_count = 0
    for t in tokens:
        current_token += 1  # current_token starts counting from 1, not 0
        if t != '(' and t != ')':  # to bypass parentheses and check operands and operators
            if t.isalpha() is True:  # operand is variable, not number
                error_token = current_token - 1
                # print error message
                left_expr = ' '.join(tokens[:error_token])
                right_expr = ' '.join(tokens[error_token + 1:])
                v = tokens[error_token]
                print(f'Invalid expression, expecting operand between {left_expr} and {right_expr}',
                      f'but {v} is a variable', sep=' ')
                return True  # True meaning yes there is an error
            elif t.isalpha() is False:  # p is either a number or an operator, not a variable
                if t in op:  # p is an operator
                    op_count -= 1
                    if num_count + op_count < 0:  # excess operator, missing operand
                        error_token = current_token - 1
                        # print error message
                        if tokens[current_token - 2] == '(':  # if previous token is '('
                            error_token = current_token - 2
                        left_expr = ' '.join(tokens[:error_token])
                        right_expr = ' '.join(tokens[error_token:])
                        print(f'Invalid expression, expecting operand between {left_expr} and {right_expr}')
                        return True
                else:  # p is not in the op list, so is a number
                    num_count += 1
                    if num_count + op_count > 1:  # excess number, missing operator
                        error_token = current_token - 1
                        # print error message
                        if tokens[current_token - 2] == '(':  # if previous token is '('
                            error_token = current_token - 2
                        left_expr = ' '.join(tokens[:error_token])
                        right_expr = ' '.join(tokens[error_token:])
                        print(f'Invalid expression, expecting operator between {left_expr} and {right_expr}')
                        return True

        if t == '(':
            if tokens[current_token] == ')':  # current_token starts at ONE, not 0,
                # So, tokens[current_token] refers to the next t in tokens
                error_token = current_token
                left_expr = ' '.join(tokens[:error_token])
                right_expr = ' '.join(tokens[error_token:])
                print(f'Invalid expression, expecting operand between {left_expr} and {right_expr}')
                return True


def calc(expr):
    """To determine validity of an expression. If valid, expression will be evaluated"""

    while True:
        # tokenize expression
        tokens = tokenize(expr)

        # check if parentheses are balanced
        balanced = parentheses_balance_check(tokens)
        if balanced is None:
            continue

        # check validity of operands and operators
        has_error = opd_opr_check(tokens)
        if has_error is True:
            continue

        # expression is valid. evaluate expression
        ans = eval(expr)
        return ans