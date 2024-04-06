import argparse


def main():
    parser = argparse.ArgumentParser(
                        prog='paradox',
                        description='Mr. Paradox Travel Guide for Time Traveler',
                        # epilog='Text at the bottom of help',
                        )

    
    parser.add_argument('guide', help='Guide for Time Traveler')
    args = parser.parse_args()


   

main()

