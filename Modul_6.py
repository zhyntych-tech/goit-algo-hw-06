from collections import UserDict
from curses.ascii import isdigit


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not str(value).strip() :
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if value and len(str(value))!=10 or not str(value).isdigit():
            raise ValueError("Phone are not correct")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone):
        phone_obj = Phone(phone) # для перевірки коректності введеного номеру
        for i in self.phones:
            if i.value == phone:
                return i
        return None

    def add_phone(self, phone):
        if self.find_phone(phone) is None:
            self.phones.append(Phone(phone))
        return self

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if found_phone:
            self.phones.remove(found_phone)
        return self

	def edit_phone(self, old_phone, new_phone):
        new_phone_obj = Phone(new_phone)
        old_phone_obj = self.find_phone(old_phone)
        if old_phone_obj is not None:
            old_phone_obj.value = new_phone_obj.value
        else:
            raise ValueError("Phone not found")
        return self

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
		pass
