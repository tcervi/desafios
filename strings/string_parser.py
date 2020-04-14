LINE_SIZE_DEFAULT = 40
TEXT_FILE_DEFAULT = 'sample.txt'


def justify_text(text, line_size=LINE_SIZE_DEFAULT):
    pass


def format_text(base_text, line_size=LINE_SIZE_DEFAULT):
    if base_text is None:
        return ''

    if len(base_text) <= line_size:
        return base_text

    base_words = base_text.rsplit()

    text_lines = []
    lines_sizes = []
    current_line = ''
    current_size = 0
    for word in base_words:
        current_size += (len(word) + 1)
        if current_size < line_size:
            current_line += ' ' + word
            continue
        else:
            lines_sizes.append(len(current_line))
            text_lines.append(current_line.strip() + "\n")
            current_line = word
            current_size = len(word)
    else:
        lines_sizes.append(len(current_line))
        text_lines.append(current_line.strip())

    print(text_lines)
    print(lines_sizes)
    return text_lines


def main():
    input_file = open(TEXT_FILE_DEFAULT, "r")
    output_file = open("output_"+TEXT_FILE_DEFAULT, "w")
    text_sample = input_file.read()

    new_text = format_text(text_sample)
    # TODO justify_text(new_text)

    output_file.writelines(new_text)

    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main()