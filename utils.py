import yaml
import json

def load_yaml():
    with open('logbook.yaml') as logbook:
        data_yaml = yaml.load(logbook, Loader=yaml.FullLoader)
        return data_yaml

def load_json(file):
    with open(file) as readers:
        data_json = json.load(readers)
        return data_json

def search_in_library(data_input, id_book):
   filtered_books = list(filter(lambda x: x['book_id'] == id_book, data_input))
   sorted_book = sorted(filtered_books, key=lambda x: x['taken_at'])
   last = sorted_book[len(sorted_book) - 1]
   if last:
      return last
   else:
      return 0

def get_book(id_book):
    data_logbook = load_yaml()
    data_readers = load_json("readers.json")
    data_books = load_json("books.json")
    search_logbook = search_in_library(data_logbook, id_book)
    search_reader_book = list(filter(lambda x: x["id"]==search_logbook["reader_id"], data_readers))
    search_book = list(filter(lambda x: x["id"]==search_logbook["book_id"], data_books))
    if search_logbook["returned_at"] != None:
        in_library = True
    else:
        in_library = False

    result = {
        "book_id" : search_book[0]["id"],
        "book_name" : search_book[0]["title"],
        "last_reader_id" : search_reader_book[0]["id"],
        "last_reader_full_name" : search_reader_book[0]["first_name"] + " " + search_reader_book[0]["last_name"],
        "in_library" : in_library
    }
    return result