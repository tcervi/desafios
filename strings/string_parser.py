
text_sample = \
    r'In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over' \
    r' the surface of the deep, and the Spirit of God was hovering over the waters.And God said, ' \
    r'"Let there be light," and there was light. God saw that the light was good, and he separated the light from the' \
    r' darkness. God called the light "day," and the darkness he called "night." And there was evening, and there' \
    r' was morning - the first day.'


def format_text(base_text, line_size=40):
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
            text_lines.append(current_line.strip())
            current_line = word
            current_size = len(word)
    else:
        lines_sizes.append(len(current_line))
        text_lines.append(current_line.strip())

    print(text_lines)
    print(lines_sizes)
    return text_lines


def main():
    format_text(text_sample)


if __name__ == '__main__':
    main()