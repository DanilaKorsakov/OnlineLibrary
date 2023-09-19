# Сайт для чтения книг

Данный код предоставляет доступ к сайту, на котором размещены книги, которые можно скачать и прочитать. Информация по книгам взята с сайта [tululu.org](https://tululu.org/)


## Запуск сайта онлайн

Для запуская сайта с книгами можно перейти по ссылке : [https://danilakorsakov.github.io/OnlineLibrary/pages/index1.html](https://danilakorsakov.github.io/OnlineLibrary/pages/index1.html)

## Запуск сайта оффлайн

Для запуска сайта оффлайн необходимо:

  1. скачать копию проекта
  1. зайти в папку с проектом и открыть папку `pages`
  1. запустить файл `index1.html`

## Просмотр кода и его редактирование

Чтобы посмотреть код, а также редактировать его необоходимо:

  1. скачать копию проекта
  1. установить все необходимые зависимости. Это можно сделать используя команду:

        ```
        pip install -r requirements.txt
        ```
  1. запустить сервер (Позволяет сразу же просматривать изменения на странице):
      ```
       python render_website.py
      ```
  1. открыть файл `template.html`, в котором редактируется весь шаблон страниц
  
  1. перейти по ссылке [http://127.0.0.1:5500/](http://127.0.0.1:5500/)

Все данные по книгам находятся в файле `books.json`

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
