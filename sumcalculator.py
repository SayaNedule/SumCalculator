value_dict = {}
OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}

def identify_action():
    while True:
        global number_in
        number_in = input().strip() #just added strip
        global number
        number = number_in.split()
        if number_in == '/exit':
            print('Bye!')
            break
        elif number_in == '/help':
            print('The program calculates the sum of numbers')
        elif number_in.startswith('/'):
            print("Unknown command")
        elif number_in.endswith('+') or number_in.endswith('-'):
            print('Invalid expression')
        elif number_in.startswith('+'):
            print(number_in[1])
        elif number_in.count('*') > 3:
            print('Invalid expression')
        elif number_in.count('/') >= 2:
            print('Invalid expression')
        elif number_in.count('(') != number_in.count(')'):
            print('Invalid expression')
        elif len(number) == 0:
            continue

        elif '=' in number_in:
            new_variable = number_in.replace(' ','').split('=')
            if new_variable[0].isalpha() and new_variable[1].isnumeric():
                value_dict[new_variable[0]] = int(new_variable[1])
            elif new_variable[0].isalpha() and new_variable[1].isalpha():
                if new_variable[1] in value_dict.keys():
                    value_dict[new_variable[0]] = value_dict[new_variable[1]]
                else:
                    print('Invalid assignment')
            else:
                print('Invalid identifier')
        elif len(number) == 1:
            try:
                print(value_dict[number_in])
            except KeyError:
                print("Unknown variable")

        elif '+' in number_in or '-' in number_in:
            suma = ''
            for n in number:
                if n.isalpha():
                    suma += str(value_dict[n])
                    suma += ' '
                elif n.isnumeric():
                    suma += n
                    suma += ' '
                else:
                    suma += n
            print(int(eval(suma)))


        elif len(number) >= 2:
            if '+' not in number or '-' not in number:
                print(int(eval(number_in)))
            else:
                calculation()



def calculation():
    global a_list
    a_list = [i for i in number]
    global new_list
    new_list = []
    sign_sinc()
    global string
    string = ''
    for new in new_list:
        string += new
        string += ' '
    infix_to_postfix()
    postfix_evaluation()

def sign_sinc():
    for num in a_list:
        if num == '--':
            new_sign = num.replace('--', '+')
            new_list.append(new_sign)
        elif num == '---':
            new_sign = num.replace('---', '-')
            new_list.append(new_sign)
        elif num == '++':
            new_sign = num.replace('++', '+')
            new_list.append(new_sign)
        elif num == '+++':
            new_sign = num.replace('+++', '+')
            new_list.append(new_sign)
        elif num == '+':
            new_sign = num.replace('+', '+')
            new_list.append(new_sign)
        elif num == '-':
            new_sign = num.replace('-', '-')
            new_list.append(new_sign)
        else:
            new_sign = num
            new_list.append(new_sign)




def infix_to_postfix():
    stack = []
    global output
    output = ''

    for ch in string:
        if ch not in OPERATORS:
            output+= ch
        elif ch=='(':
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output

def postfix_evaluation():
    s = output
    s=s.split()
    n=len(s)
    stack =[]

    for i in range(n):
        if s[i].isdigit():
            stack.append(int(s[i]))
        elif s[i]=="+":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)+int(b))
        elif s[i]=="*":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)*int(b))
        elif s[i]=="/":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)/int(a))
        elif s[i]=="-":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)-int(a))
    return stack.pop()


identify_action()
