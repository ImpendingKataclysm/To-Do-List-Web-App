FILEPATH = "tasks.txt"


def get_list_from_file(filepath=FILEPATH):
    """
    Read a file at a specified file path and store each line as a list item
    :param filepath: the path of the file to read
    :return: the list of items read from the file
    """
    with open(filepath) as list_file:
        flist = list_file.readlines()
    return flist


def write_list_to_file(flist, filepath=FILEPATH):
    """
    Writes a specified list of items to a specified file path (1 item per line)
    :param flist: the list to write to the file
    :param filepath: the path of the file in which to write the list
    :return: None
    """
    with open(filepath, 'w') as list_file:
        list_file.writelines(flist)


def slice_numbered_string(string, delimiter='.'):
    """
    Slices a numbered string after the numbers and delimiter, leaving only the text
    :param string: the string to slice
    :param delimiter: the delimiter following the number
    :return: The text in the string
    """
    num = 0

    for char in string:
        if char.isdigit():
            num += 1
        if char == delimiter:
            num += 1

    # add 1 to num assuming there is a space following the delimiter
    return string[num + 1:]


if __name__ == "__main__":
    print(get_list_from_file())
