




import pytest
import config as cf
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv

#list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'

lst_moovie = lt.newList(list_type)
mooviefile = cf.data_dir + 'theMoviesdb/AllMoviesDetailsCleaned 2.csv'


def setUp():
    print('Loading books')
    loadCSVFile(mooviefile, lst_moovie)
    print(lst_moovie['size'])


def tearDown():
       pass
#vote_average;vote_count

def loadCSVFile(file, lst):
    input_file = csv.DictReader(open(file, encoding = "utf-8"))
    for row in input_file:
        lt.addLast(lst, row)

def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element['vote_average'])

def less(element1, element2):
    if int(element1['vote_average']) < int(element2['vote_average']):
        return True
    return False

def test_sort():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.insertionSort(lst_moovie, less)

def test_loading_CSV_y_ordenamiento():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.insertionSort(lst_moovie,less)
    while not (lt.isEmpty(lst_moovie)):
        x = int(lt.removeLast(lst_moovie)['vote_average'])
        if not (lt.isEmpty(lst_moovie)):
            y = int(lt.lastElement(lst_moovie)['vote_average'])
        else:
            break
        assert x > y