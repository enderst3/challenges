#!/usr/bin/env python3
from collections import OrderedDict
import datetime
import os
import sys

from peewee import *

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    ''' create the database and table if they dont exist'''
    db.connect()
    db.create_tables([Entry], safe=True)

def clear():
    os.system('cls' if os.name =='nt' else 'clear')

def menu_loop():
    ''' show menu '''
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit. ")
        for key, value in menu.items():
            '''this will print the key from the menu, and the docstring from function/value'''
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        '''this will run the function selected'''
        if choice in menu:
            clear()
            menu[choice]()

def add_entry():
    '''Add and entry.'''
    print('Enter your entry.  Press ctrl+d when finished.')
    # capture everything typed and get rid of the whitespace on the ends
    data = sys.stdin.read().strip() 

    if data:
        if input('Save entry? [Yn] ').lower() != 'n':
            Entry.create(content=data)
            print('Saved successfully!')


def view_entries(search_query=None):
    '''View previous entries.'''
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        '''this will do the search'''
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %D, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\n\n'+'='*len(timestamp))
        print('n) next entry')
        print('d) delete entry')
        print('q) return to main menu')

        next_action = input('Action: [Ndq] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
            print('Entry deleted!')

def search_entries():
    '''Search entries.'''
    view_entries(input('Search query: '))


def delete_entry(entry):
    '''Delete an entry.'''
    if input('Are you sure? [yN] ').lower() == 'y':
        entry.delete_instance()



menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
    ('d', delete_entry)
])

'''this will keep it from running all the time if imported'''
if __name__ == '__main__':
    initialize()
    menu_loop()