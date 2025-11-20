import sys


def computeMeanCSV(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file: 
        lines = file.readlines()

    
    lines = lines[1:]

    num_columns = len(lines[0].strip().split(','))
    sums = [0.0] * num_columns
    counts = [0] * num_columns

    for line in lines:
        # Remove quotes and split
        values = line.strip().replace('"', '').split(',')
        for i, val in enumerate(values):
            try:
                num = float(val.replace(',', '.').replace('M', '').replace('%', ''))
                sums[i] += num
                counts[i] += 1
            except ValueError:
                pass

    for i in range(num_columns):
        if counts[i] > 0:
            mean = sums[i] / counts[i]
            print(f"Mean of column {i}: {mean}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    computeMeanCSV(filename)
