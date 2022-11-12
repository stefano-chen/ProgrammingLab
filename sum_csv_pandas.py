import pandas as pd
from ErrorClass import ErrorClass


def sum_csv_pandas(filename):
    result = 0.0
    try:
        file = pd.read_csv(filename)
        for item in file["Valore"].tolist():
            try:
                result += float(item)
            except:
                result += 0
    except FileNotFoundError:
        raise ErrorClass("File not Found")
    except pd.errors.EmptyDataError:
        raise ErrorClass("Empty File")
    return result


def main():
    print("sum : {}".format(sum_csv_pandas("test.csv")))


if __name__ == "__main__":
    main()
