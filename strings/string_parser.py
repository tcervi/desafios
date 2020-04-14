import argparse


LINE_SIZE_DEFAULT = 40
TEXT_FILE_DEFAULT = 'sample.txt'


def left_justify(line, width):
    """

    :param line:
    :param width:
    :return:
    """


def justify_lines(lines_list, line_size=LINE_SIZE_DEFAULT):
    """Given a target line width and a list of stings, each one of width smaller or equal
    to the target, return a list of strings with text justified and width exact the same as
    the target one.

    :param lines_list: the list of stings to be justified
    :param line_size: the target line width
    :return:
    """
    pass


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
    # TODO justify_text(new_text)

    output_file.writelines(new_text)

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()