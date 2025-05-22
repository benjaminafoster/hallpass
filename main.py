import sys
from login import register_user

def main():
    try:
        register_user()
    except KeyboardInterrupt:
        print("\nEnding program...")
        sys.exit()

main()