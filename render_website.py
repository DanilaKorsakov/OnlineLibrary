import json


from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server, shell
from more_itertools import chunked
from pathlib import Path


def on_reload(folder):

    with open("books.json", "r", encoding='utf-8') as my_file:
        books_json = my_file.read()

    book_txt_url= "https://tululu.org/txt.php"

    books = json.loads(books_json)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('template.html')

    books_page =  list(chunked(books,10))

    for number, page in enumerate(books_page, 1):

        books_row = list(chunked(page,2))

        rendered_page = template.render(
            books_row=books_row,
        )

        with open(f'{folder}/index{number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)

def main():

    folder = 'pages/'

    Path(folder).mkdir(parents=True, exist_ok=True)

    on_reload(folder)


    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')




if __name__ == '__main__':
    main()

