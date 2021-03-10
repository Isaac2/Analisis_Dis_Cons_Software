class person:
    def __init__(self, name, email, age, country):
        self.name = name
        self.email = email
        self.age = age
        self.country = country

    def print_data(self):
        print("Name: " + self.name +
            ", email: " + self.email +
            ", age: " + str(self.age) +
            ", country: " + self.country)
    
class directory:
    def __init__(self):
        self.contacts = []

    def add_contact(self, new_person):
        self.contacts.append( new_person )

    def delete_contact(self, index_delete ):
        self.contacts.pop( index_delete )

    def view_contact(self, index):
        self.contacts[index].print_data()

    def look_by_email(self, email):
        found = False
        for contact in self.contacts:
            if contact.email == email:
                print("Conctacto encontrado")
                contact.print_data()
                found = True

        if found == False:
            print("Contact not found")

    def look_by_age(self, age):
        found = False
        for contact in self.contacts:
            if contact.age == age:
                print("Conctact found")
                contact.print_data()
                found = True

        if found == False:
            print("Contact not found")
    
    def print_all(self):
        for contact in self.contacts:
            contact.print_data()

personA = person("Isa AAAAAA", "i@a.com", "15 years", "Uganda")
personB = person("Jack Sparrow", "j@s.com", "51", "Spanish")
personC = person("King Godzilla", "k@g.com", "700", "Japan")
personA.print_data()
personB.print_data()

directoryA = directory()
directoryA.look_by_email( "i@a.com" )
directoryA.add_contact( personA )
directoryA.add_contact( personB )
directoryA.add_contact( personC )
directoryA.add_contact( personA )
directoryA.add_contact( personA )

directoryA.look_by_age( "51" )
directoryA.look_by_age( 51 )
directoryA.look_by_email( "i@a.com" )

directoryA.view_contact( 1 )
directoryA.delete_contact( 1 )
directoryA.view_contact( 1 )
directoryA.print_all()