import Services.BookStatistics as bs
import constants as cs
import Views.MainMenuView as mmv

def main():
    # books = fm.read_books(cs.book_file_name)
    bs.calculate_each_genre(cs.book_file_name)
    print("Printinu is pagrindinio")
    mmv.print_main_menu()

main()


# import importuojamas as imp

# kopija = imp.importuojamas_kintamasis

# imp.importuota_funkcija(kopija)

# objektas = imp.importuojama_klase()
# print(__name__)
# from importuojamas import importuota_funkcija as ifun
# from importuojamas import importuojama_klase as iklas

# ifun(15)
# import Classes.Book as bk # Importuojamas visas failas 

# bk.Book()

# from Classes.Book import Book # Importuojamas elementas

# Book()

# from Classes import Book,Reader # Importuojami keli failai