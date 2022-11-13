class CSVFile:
    def __init__(self, name):
        self.name = name
        self.file = None

    def __open(self):
        try:
            self.file = open(self.name, 'r')
            return True
        except FileNotFoundError:
            print("Errore File not Found")
            return False

    def get_data(self):
        li = []
        if self.__open():
            for item in self.file:
                element = item.split(',')
                if element[0] != 'Date':
                    element[1] = element[1].replace('\n', '')
                    li.append(element)
            self.file.close()
        return li