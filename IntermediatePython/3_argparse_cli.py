import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y',type=float,default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation',type=str,default='add',
                        help='What operation (add,sub,mul,div) ?')
    args = parser.parse_args()
    print(calc(args))
    
def calc(args):
    operation = args.operation
    x = args.x
    y = args.y
    if operation == 'add':
        return x+y
    elif operation =='sub':
        return x-y
    elif operation =='mul':
        return x*y
    elif operation =='div':
        return x/y

if __name__ == "main":
    main()

#operation = calc (7,3,'add')
#print(operation)
