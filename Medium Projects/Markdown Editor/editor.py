class MarkdownEditor:

    def __init__(self):
        self.final_text = []
        self.line_count = 0
        self.select_format()

    def select_format(self):
        self.format = input('Choose a formatter: ')
        if self.format == '!help':
            print("""Available formatters: plain bold italic header link inline-code new-line
        Special commands: !help !done""")
            self.select_format()
        elif self.format == '!done':
            self.exit()
        elif self.format in ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list']:
            self.check_format(self.format)
        else:
            print('Unknown formatting type or command')
            self.select_format()

    def check_format(self, style):
        if style == 'plain':
            self.plain()
        elif style == 'bold':
            self.bold()
        elif style == 'italic':
            self.italic()
        elif style == 'link':
            self.link()
        elif style == 'header':
            self.header()
        elif style == 'new-line':
            self.new_line()
        elif style == 'inline-code':
            self.inline_code()
        elif style in ['ordered-list', 'unordered-list']:
            self.list(style)

    def list(self, style):
        n = 0
        while n < 1:
            n = int(input('Number of rows: '))
            if n < 1:
                print('The number of rows should be greater than zero')
        temp = []
        for i in range(n):
            temp.append(input(f'Row #{i + 1}: '))
        if style == 'ordered-list':
            for i in range(n):
                temp[i] = f'{i + 1}. {temp[i]}\n'
        else:
            for i in range(n):
                temp[i] = f'* {temp[i]}\n'
        for i in range(n):
            self.final_text.append(temp[i])
        self.printing()

    def plain(self):
        text = input('Text: ')
        self.final_text.append(text)
        self.printing()

    def bold(self):
        text = input('Text: ')
        self.final_text.append(f'**{text}**')
        self.printing()

    def italic(self):
        text = input('Text: ')
        self.final_text.append(f'*{text}*')
        self.printing()

    def inline_code(self):
        text = input('Text: ')
        self.final_text.append(f'`{text}`')
        self.printing()

    def new_line(self):
        self.final_text.append('\n')
        self.printing()

    def header(self):
        level = int(input('Level: '))
        if 1 <= level <= 6:
            text = input('Text: ')
            self.final_text.append('#' * level)
            self.final_text.append(f' {text}')
            self.final_text.append('\n')
            self.printing()
        else:
            print('The level should be within the range of 1 to 6')
            self.header()

    def link(self):
        label = input('Label: ')
        url = input('URL: ')
        self.final_text.append(f'[{label}]({url})')
        self.printing()

    def printing(self):
        for text in self.final_text:
            print(text, end='')
        print()
        self.select_format()

    def exit(self):
        with open('output.md', 'w') as out:
            for text in self.final_text:
                out.write(text)


editor = MarkdownEditor()
