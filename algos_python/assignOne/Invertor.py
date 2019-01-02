class Invertor:

    def __init__(self, ipath, opath):
        self.filepath = ipath
        self.output_filepath = opath
        self.unsorted_list = self.__set_unsorted_list()
        self.sorted_list = None
        self.inversions = None

    def __set_unsorted_list(self):
        """
        Private because it doesnt make sense to use anywhere else
        :return: list
        """
        my_list = []
        with open(self.filepath, "r") as file:
            for line in file:
                my_list.append(line.strip())
        return my_list

    def set_sorted_list(self, my_list):
        self.sorted_list = my_list

    def set_inversions(self, inv):
        self.inversions = inv

    def write_sorted_list(self):
        with open(self.output_filepath, "w") as file:
            file.write(f"It took {self.inversions} inversions to sort this file")
            file.write("-------------------")
            file.write("\n")

            for number in list:
                file.write(f'{number}\n')
