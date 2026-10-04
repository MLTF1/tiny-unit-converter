"""Convert a small set of everyday units from the command line."""
import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("conversion", choices=("c-to-f", "km-to-mi"))
    parser.add_argument("value", type=float)
    args = parser.parse_args()

    if args.conversion == "c-to-f":
        result = args.value * 9 / 5 + 32
        unit = "°F"
    else:
        result = args.value * 0.621371
        unit = "mi"
    print(f"{result:.2f} {unit}")


if __name__ == "__main__":
    main()
