import argparse
from .generator import generate

def main():
    parser = argparse.ArgumentParser(description="Glint Static Site Generator")
    subparsers = parser.add_subparsers(dest="command")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate the static site")
    generate_parser.set_defaults(func=generate)

    args = parser.parse_args()
    if args.command:
        args.func()

if __name__ == "__main__":
    main()