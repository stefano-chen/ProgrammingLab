import os


def sum_csv(file_name):
    result = 0.0
    file = open(file_name, "r")
    if file is not None:
        if os.stat(file_name).st_size > 0:
            for line in file:
                element = line.split(',')
                if element[0] != "Date":
                    try:
                        result += float(element[1])
                    except:
                        result += 0
        else:
            file.close()
            return None
    file.close()
    return result
