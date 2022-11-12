class CSVFile:
    def __init__(self, filename):
        self.name = filename
        self.file = None

    def __open(self):
        try:
            self.file = open(self.name, 'r')
            return True
        except FileNotFoundError:
            return False

    def get_data(self):
        li = []
        if self.__open():
            for item in self.file:
                element = item.split(',')
                element[1] = element[1].replace('\n', '')
                if element[0] != 'Data':
                    li.append(element)
            self.file.close()
        return li


csv = CSVFile("test.csv")
print(csv.get_data())