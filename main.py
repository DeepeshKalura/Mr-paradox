import os
import argparse
from dotenv import load_dotenv
from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from app.llm_model import model_response
from app.qrcode import generate_qr_code

# Set the environment variable
load_dotenv()



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
    print(generate_qr_code())
else:
    wolfram = WolframAlphaAPIWrapper()
    weather = wolfram.run(f"weather {args.destination} time {args.time}")
    if (args.budget != None):
        money_value = wolfram.run(f"describe money {args.budget}")
    else:
        money_value = "INR"
    print(model_response(location=args.destination, dates=args.time, money_value=args.budget, money=money_value, weather=weather))
