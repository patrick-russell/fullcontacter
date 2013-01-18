import fullcontacter

def main():
    #create a name object
    fc_name = fullcontacter.nameStats('YOUR API KEY HERE')

    #create a person object
    fc_person = fullcontacter.personLookup('YOUR API KEY HERE')

    #look up a name
    name = fc_name.lookitup(fname='Patrick', lname='Russell')

    #look up a person via twitter
    person_twitter = fc_person.lookitup('patrickrm101', 'twitter')

    #look up a person via email
    person_email = fc_person.lookitup('prussell@gmail.com')

    return name, person_twitter, person_email

if __name__ == "__main__":
    main()
