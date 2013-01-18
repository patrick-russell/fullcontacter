Fullcontact Python module
====================
A Python module for the [Fullcontact API](http://www.fullcontact.com) version 2.0
It has functionality for name stats API and person APIs (except vcard).

Readme
------------
You can find full documentation at [Fullcontact.com](http://www.fullcontact.com).

Specifically:<br>
[Name API docs](http://www.fullcontact.com/docs/?category=person)<br>
[Person API docs](http://www.fullcontact.com/docs/?category=name)

You will need a fullcontact API key to use this module. The name API is free, the person is not.

I have the name API and person API in separate classes to keep free/paid separate.

Installation
------------
With pip (prefered)

    pip install fullcontacter

With easy_install

    easy_install fullcontacter


Usage Examples
--------------
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

TODO
---------
Test coverage.
Ditch urllib2 for Requests.
Implement a better API and include more of the lookup options, including account status.

Random
---------
First attempt at releasing something to the public. I'm pretty new to this, tips, ideas, criticism, all welcome.

Copyright
---------
Copyright (c) 2013 Patrick Russell

See [LICENSE](https://github.com/patrick-russell/fullcontact-api-python/blob/master/LICENSE.md) for details.