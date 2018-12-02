class PuzzlesUtils:
    """
    Utility class for coding challenges and puzzles
    """
    def read_file(self, file_path):
        """

        :param file_path: path of file to read
        :return:
        """
        file = open(file_path, "r")
        contents = [line for line in file.read()]
        return contents