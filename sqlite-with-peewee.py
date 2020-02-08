from peewee import *

# Select database
db = SqliteDatabase('crazypeople.sqlite')

# Create Model class for Peewee, defines fields, objects in program and columns in database.
class ChainsawJuggler(Model):
    name = CharField()
    country = CharField()
    number_of_catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} from {self.country} has a record of {self.number_of_catches} catches while juggling chainsaws.'

db.connect()
db.create_tables([ChainsawJuggler])

def add_record_holder():
    record_name = str(input('Enter the name of the record holder: '))
    record_country = str(input('Enter the country that ' + record_name + ' is from: '))
    record_number = int(input('How many catches did ' + record_name + ' make? '))
    new_record_holder = ChainsawJuggler(name=record_name, country=record_country, number_of_catches=record_number)
    new_record_holder.save()
    print('Record holder added.')

def update_record_holder():
    name = input('Enter the record holder you\'d like to update')
    new_catches = input('Enter the new number of catches for ' + name)
    rows_updated = ChainsawJuggler.update(number_of_catches=new_catches).where(ChainsawJuggler.name == name).execute()
    print('\nUpdated ' + str(rows_updated) + ' rows')


def delete_record_holder():
    name = input('Enter the name of the record holder to delete')
    rows_deleted = ChainsawJuggler.delete().where(ChainsawJuggler.name == name).execute()
    print('Deleted ' + str(rows_deleted) + ' rows')


def search_record_holder():
    search = input('Enter the name of the record holder to search')
    juggler = ChainsawJuggler.get_or_none(ChainsawJuggler.name == search)
    print(juggler)

def show_all_record_holders():
    jugglers = ChainsawJuggler.select()
    for juggler in jugglers:
        print(juggler)


def main():
    while(True):
        option = input('Select an option...\n1. Add \n2. Update \n3. Search \n4. Delete \n5. Show all \n6. Quit\n')
        if (option == '1'):
            add_record_holder()
        elif (option == '2'):
            update_record_holder()
        elif (option == '3'):
            search_record_holder()
        elif (option == '4'):
            delete_record_holder()
        elif (option == '5'):
            show_all_record_holders()
        elif (option == '6'):
            exit()

if __name__ == '__main__':
    main()