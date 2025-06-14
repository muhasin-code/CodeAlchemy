def main():
    n = 5 # int(input("Enter the number of datapoints: "))
    datapoints = [1, 5, 4, 2, 3, 6] # [int(input("Enter datapoint: ")) for _ in range(n)]

    print(f"Mean: {mean(n, datapoints)}")
    print(f"Median: {median(sorted(datapoints))}")
    print(f"Range: {range_(datapoints)}")


def mean(n, datapoints):
    return sum(datapoints) / n


def median(datapoints):
    mid = len(datapoints) // 2
    if len(datapoints) % 2 == 1:
        return datapoints[mid]
    else:
        return (datapoints[mid] + datapoints[mid - 1])/2
    

def range_(datapoints):
    return max(datapoints) - min(datapoints)


if __name__ == '__main__':
    main()