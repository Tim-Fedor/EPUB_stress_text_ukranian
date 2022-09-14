import sys

from ukrainian_word_stress import Stressifier, StressSymbol
import ebooklib
from ebooklib import epub


# OVERRIDE ebooklib
class BookWriterNew(epub.EpubWriter):
    def _write_items(self):
        for item in self.book.get_items():
            self.out.writestr('%s/%s' % (self.book.FOLDER_NAME, item.file_name), item.content)


def write_new_epub(name, old_book, options=None):
    epub_new = BookWriterNew(name, old_book, options)
    epub_new.process()
    try:
        epub_new.write()
    except IOError:
        pass
# END OVERRIDE


def add_symbol_to_words(text):
    s = text.decode('utf-8')
    stressify = Stressifier(stress_symbol=StressSymbol.CombiningAcuteAccent)
    return stressify(s).encode('utf-8')


if __name__ == '__main__':
    book = epub.read_epub(sys.argv[1])
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    for chapter in items:
        chapter.content = add_symbol_to_words(chapter.content)
    write_new_epub(sys.argv[2], book)
