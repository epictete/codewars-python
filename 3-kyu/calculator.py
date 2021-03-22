class Calculator(object):

    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    @staticmethod
    def precedence(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0

    @staticmethod
    def evaluate(exp):

        ops = []
        vals = []
        i = 0

        while i < len(exp):
            if exp[i] == ' ':
                i += 1
                continue
            if exp[i].isdigit():
                val = ''
                while i < len(exp) and (exp[i].isdigit() or exp[i] == '.'):
                    val += exp[i]
                    i += 1
                vals.append(float(val))
                i -= 1
            if exp[i] in Calculator.operators:
                while len(ops) > 0 and ops[-1] != '(' and Calculator.precedence(ops[-1]) >= Calculator.precedence(exp[i]):
                    val2 = vals.pop()
                    val1 = vals.pop()
                    op = ops.pop()
                    vals.append(Calculator.operators[op](val1, val2))
                ops.append(exp[i])
            if exp[i] == '(':
                ops.append(exp[i])
            if exp[i] == ')':
                while len(ops) > 0 and ops[-1] != '(':
                    val2 = vals.pop()
                    val1 = vals.pop()
                    op = ops.pop()
                    vals.append(Calculator.operators[op](val1, val2))
                ops.pop()
            i += 1

        while ops:
            val2 = vals.pop()
            val1 = vals.pop()
            op = ops.pop()
            vals.append(Calculator.operators[op](val1, val2))

        return vals[-1]


print(Calculator().evaluate("1.1 + 2.2 + 3.3") == 6.6)
print(Calculator().evaluate("2 - 3 - 4") == -5)
print(Calculator().evaluate("12 / 2 + 3 * 4 - 6") == 12)
print(Calculator().evaluate("2 / 2 + 3 * 4 - 6") == 7)
print(Calculator().evaluate("3 * 4 + 3 * 7 - 6") == 27)
print(Calculator().evaluate('1 + 1') == 2)
print(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )") == 2)
print(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )") == 5)
print(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )") == 16)
print(Calculator().evaluate("3 * ( 4 + 7 ) - 6") == 27)
