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
                except ValueError:
                    result += 0
    file.close()
    return result if not empty else None
