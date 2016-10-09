# python_translate_to_multi_languages
This app is using the google translator api. You have to type your text and after you get the output in json format.

Please note that the output can have unicode characters. If you want to convert use unicodedata.

Read more about unicode characters here:
http://www.fileformat.info/info/unicode/char/a.htm




Here is a short example that I found on stackoverflow:

title = u"Klüft skräms inför på fédéral électoral große"
import unicodedata
unicodedata.normalize('NFKD', title).encode('ascii','ignore')
'Kluft skrams infor pa federal electoral groe'
