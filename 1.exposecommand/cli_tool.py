import argparse

def greet(args):
    if args.name:
        print(f"Hello, {args.name}!")
    else:
        print("Hello, World!")

def sum_numbers(args):
    result = sum(args.numbers)
    print(f"The sum of the numbers is: {result}")

# Main function to set up the argument parser
def main():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description='A simple CLI with two commands')
    
    # Create subparsers for the individual commands
    subparsers = parser.add_subparsers()

    # 'greet' command
    parser_greet = subparsers.add_parser('greet', help='Greet someone')
    parser_greet.add_argument('--name', help='Name of the person to greet')
    parser_greet.set_defaults(func=greet)

    # 'sum' command
    parser_sum = subparsers.add_parser('sum', help='Calculate the sum of numbers')
    parser_sum.add_argument('numbers', nargs='+', type=int, help='Numbers to sum')
    parser_sum.set_defaults(func=sum_numbers)

    # Parse the arguments and call the appropriate function
    args = parser.parse_args()

    # Call the function associated with the command
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

