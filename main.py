import argparse

def fake_function(destination: str, time: str, buget: str ) -> str:
    """
    This function will return the destination for time travel
    """
    return f"Destination: {destination}, Time: {time}, Buget: {buget}"


def under_construction(value: float) -> str: 
    return f"This is payment feature is under construction! sob sob sob thanks for {value} money"


parser = argparse.ArgumentParser(prog="paradox", usage="%(prog)s request [options]", add_help=True, epilog="Made by Deepesh Kalura")

command = parser.add_subparsers(metavar="", title='request')


guide_sub_parser = command.add_parser('guide', help='Guide Nobiee Time Traveler')

guide_sub_parser.add_argument('destination', type=str, help='Destination for time travel')
guide_sub_parser.add_argument('time', type=str, help='Time for time travel')
guide_sub_parser.add_argument( '-b', '--budget', type=str, help='Buget for travelling', metavar='')

# guide.add_argument('--help', '-h', action='help', help='Guide Nobiee Time Traveler')



pay_sub_parser = command.add_parser('pay', help='Pay for the Time Travel guidance')

pay_sub_parser.add_argument('payment', help='INR Ammount Payment', type=float)


args = parser.parse_args()

if not any(vars(args).values()):
    parser.print_help()

elif 'payment' in args:
    print(under_construction(args.payment))
else:
    print(fake_function(args.destination, args.time, args.budget))


