## EPUB_stress_text_ukranian UKR/ENG
Цей проект створенний для того, щоб автоматично проставити наголоси у будь-якій книжці українською формату EPUB.

This project was created to automatically place word stress in any Ukrainian book in EPUB format.

## Як користуватися? / How to use?
    python stress_book.py [назва файлу] [назва нового файлу]
Наприклад / Example:

    python stress_book.py garri.epub new_garri.epub

Після цього нову книгу можна навіть конвертувати в інший формат. Наприклад - в [MOBI](https://convertio.co/ru/epub-mobi)

After that, the new book can even be converted to another format. For example - in [MOBI](https://convertio.co/ru/epub-mobi)

## Як написан? / How is it written?
Насправді - сам проект дуже короткий і простий.
За основу взято два модулі:
1. [ebooklib](https://github.com/aerkalov/ebooklib) - модуль для роботи з форматом EPUB
2. [ukrainian-word-stress](https://github.com/lang-uk/ukrainian-word-stress) - модуль для проставлення наголосів у тексті з словника

Конкретно цей проект лише об'єдную роботу двух модулів, тому дуже рекомендую ознайомитися з репозиторіями без яких не було б цього проекту

In fact, the project itself is very short and simple.
It is based on two modules:
1. [ebooklib](https://github.com/aerkalov/ebooklib) - a module for working with the EPUB format
2. [ukrainian-word-stress](https://github.com/lang-uk/ukrainian-word-stress) - a module for placing accents in the text from the dictionary

In particular, this project only combines the work of two modules, so I highly recommend that you familiarize yourself with the repositories without which this project would not exist

## Чи можна допрацювати? / Can you contribute?
**Треба**. Проект сирий, тому приймаються будь-які баг-репорти та пулл-реквести.

**Of course**. The project is raw, so any bag-reports and pull-requests are accepted.

## TODO
+ потестити на більшій кількості книг - треба знайти потенційні проблеми
+ полегшити використання програми (web app?)
+ додати підтримку MOBI (скоріше за все через двусторонню конвертацію)
