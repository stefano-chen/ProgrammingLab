def sum_csv(file_name):
    result = 0.0
    empty = True
    file = open(file_name, "r")
    if file is not None:
        for line in file:
            empty = False
            element = line.split(',')
            if element[0] != "Date":
                try:
                    result += float(element[1])
                except:
                    result += 0
    file.close()
    return result if not empty else None


def main():
    print(sum_csv("test.csv"))


if __name__ == "__main__":
    main()
