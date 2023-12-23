import sys

def factorize(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line in file:
                n = int(line.strip())
                factor_pairs = factorize(n)
                for pair in factor_pairs:
                    print(f"{n}={pair[0]}*{pair[1]}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == '__main__':
    main()
