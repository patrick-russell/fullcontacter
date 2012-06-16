import fullcontact

def main():
    #create a name object
    fc_name = fullcontact.nameStats('YOUR API KEY HERE')

    #create a person object
    fc_person = fullcontact.personLookup('YOUR API KEY HERE')
    
    #look up a name
    name = fc_name.lookitup(fname='Bart',lname='Lorang')
    
    #look up a person via twitter
    person_twitter = fc_person.lookitup('lorangb','twitter')
    
    #look up a person via email
    person_email = fc_person.lookitup('bart@fullcontact.com')
    
    return name, person_twitter,person_email
    
if __name__ == "__main__":
    main()