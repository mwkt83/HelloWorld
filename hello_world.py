import argparse

parser = argparse.ArgumentParser(description="Greet someone.")
parser.add_argument("name", nargs="?", default="World", help="name to greet")
args = parser.parse_args()

print(f"Hello, {args.name}!")
