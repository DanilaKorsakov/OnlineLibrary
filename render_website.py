import json

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server, shell
from more_itertools import chunked


def on_reload():

    with open("books.json", "r", encoding='utf-8') as my_file:
        books_json = my_file.read()


    books = json.loads(books_json)

    books_row = list(chunked(books,2))

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    rendered_page = template.render(
        books_row=books_row
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

def main():
    on_reload()

    # server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    # server.serve_forever()

    server = Server()
    server.watch('template.html', on_reload)
    server.serve(root='.')


if __name__ == '__main__':
    main()

