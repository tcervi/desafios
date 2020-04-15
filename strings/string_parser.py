import argparse


LINE_SIZE_DEFAULT = 40
TEXT_FILE_DEFAULT = 'sample.txt'


def left_justify(line, width):
    """Given a line of text and a target width, return that line left-justified
    to the target width, padded with blank spaces.

    :param line: the text line to be left-justified
    :param width: the target line width
    :return: a string representing the line left-justified
    """
    if line is None or not isinstance(line, str):
        raise ValueError("Wrong line value was passed to be left-justified")

    if width is None:
        raise ValueError("No line width was passed to lef-justify")

    return ' '.join(line.rsplit()).ljust(width)


def justify_line(line, width):
    """Given a line of text and a target width, return that line justified to the target width

    :param line: the text line to be justified
    :param width: the target line width
    :return: a string representing the line justified
    """

    if line is None or not isinstance(line, str):
        raise ValueError("Wrong line value was passed to be left-justified")

    if width is None:
        raise ValueError("No line width was passed to lef-justify")

    missing_size = width - len(line)
    line_spaces = line.count(' ')
    new_line = line

    if missing_size == 0:
        return line

    # Based on the missing number of chars to complete the line width and the number of blank spaces in line
    # it is possible to know how many times it will be needed to add a new space
    complete_iterations, remaining_spaces = divmod(missing_size, line_spaces)
    remaining_half, remaining_r = divmod(remaining_spaces, 2)
    target_char = ' '
    # From missing_size/line_spaces division it is possible to know
    # how many times all the spaces will have to increase by one
    for i in range(complete_iterations):
        new_line = new_line.replace(target_char, target_char + ' ')
        target_char = target_char + ' '
    else:
        # If there was no remaining from missing_size/line_spaces division, the line is justified
        if remaining_spaces == 0:
            return new_line

    # If there was a remaining value from missing_size/line_spaces division, this value will be divided by two
    # so we can include a new extra space to the first and the last "outlier" spaces between strings on this line
    # and for each iteration will come closer to the center of the string
    # (a simplified way to ensure balance on extra spaces)
    for i in range(remaining_half):
        new_line = new_line.replace(target_char, target_char + ' ', 1)
        reversed_line = new_line[::-1]
        reversed_line = reversed_line.replace(target_char, target_char + ' ', 1)
        new_line = reversed_line[::-1]
    else:
        # If, yet, we still have a remaining from remaining_spaces/2 division
        # this extra space will be added to the last 'outlier' space between strings on the line
        if remaining_r is not 0:
            new_target_char = target_char + ' ' * remaining_half
            reversed_line = new_line[::-1]
            reversed_line = reversed_line.replace(new_target_char, new_target_char + ' ', 1)
            new_line = reversed_line[::-1]

    return new_line


def justify_text(lines_list, line_size=LINE_SIZE_DEFAULT):
    """Given a target line width and a list of stings, each one of width smaller or equal
    to the target, return a list of strings with text justified and width exact the same as
    the target one.

    :param lines_list: the list of stings to be justified
    :param line_size: the target line width
    :return: the given list of strings justified to line width
    """

    new_lines_list = []
    for line in lines_list:
        # Left-justifying single word lines
        if len(line.rsplit()) == 1:
            new_lines_list.append(left_justify(line, line_size))
        else:
            new_lines_list.append(justify_line(line, line_size))

    return new_lines_list


def format_text(base_text, line_size=LINE_SIZE_DEFAULT):
    """Given a text and a maximum line width, return a list of strings
    representing the original text divided in lines having the given line width

    :param base_text: the original text
    :param line_size: the maximum line width
    :return: a list of strings of the given line width
    """

    if base_text is None:
        return ''

    if len(base_text) <= line_size:
        return base_text

    base_words = base_text.rsplit()

    text_lines = []
    current_line = ''
    current_size = 0
    for word in base_words:
        current_size += (len(word) + 1)
        if current_size < line_size:
            current_line += ' ' + word
            continue
        else:
            text_lines.append(current_line.strip() + "\n")
            current_line = word
            current_size = len(word)
    else:
        text_lines.append(current_line.strip())

    return text_lines


def main():
    parser = argparse.ArgumentParser(description='Simple Text Parser implementation in Python.'
                                                 ' Formatted text will have a pre-defined line length')
    parser.add_argument('--input_file', default=TEXT_FILE_DEFAULT, help='File location containing text to be formatted')
    parser.add_argument('--output_file', default="output_"+TEXT_FILE_DEFAULT, help='File location to save result')
    parser.add_argument('--line_len', default=40, type=int, help='Pre-defined line length value')
    args = parser.parse_args()

    input_file = open(args.input_file, "r")
    output_file = open(args.output_file, "w")
    text_sample = input_file.read()

    new_text = format_text(text_sample, args.line_len)
    new_text = justify_text(new_text)

    output_file.writelines(new_text)

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()