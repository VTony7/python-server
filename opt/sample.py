import math
import sys

def main():
    print("hello world!")
    if (len(sys.argv) > 1):
        val = float(sys.argv[1])
        print(math.radians(val))

if __name__ == "__main__":
    main()
