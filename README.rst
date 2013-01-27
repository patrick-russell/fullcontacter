Fullcontact Python module
=========================

A Python module for the `Fullcontact API`_ version 2.0 It has
functionality for name stats API and person APIs(except vcard format).

Readme
------

You can find full documentation at `Fullcontact.com`_.

Specifically: `Name API docs`_ `Person API docs`_

You will need a fullcontact API key to use this module. The name API is
free, the person is not.

I have the name API and person API in separate classes to keep free/paid
separate.

Installation
------------

With pip (prefered)

::

    pip install fullcontacter

With easy\_install

::

    easy_install fullcontacter

Usage Examples
--------------

::

    import fullcontacter

    def main():
        # create a name object
        fc_name = fullcontacter.nameStats('YOUR API KEY HERE')

        # create a person object
        fc_person = fullcontacter.personLookup('YOUR API KEY HERE')

        # look up a name
        name = fc_name.lookitup(fname='Patrick', lname='Russell')

        # look up a person via twitter
        person_twitter = fc_person.lookitup('patrickrm101', 'twitter')

        # look up a person via email
        person_email = fc_person.lookitup('prussell@gmail.com')

        return name, person_twitter, person_email

    if __name__ == "__main__":
        main()

TODO
----

support vcard
Test coverage.
Implement a better API and include more of the lookup options, including account status.

Random
------

First attempt at releasing something to the public. I’m pretty new to this, tips, ideas, criticism, all welcome.

Copyright
---------

Copyright (c) 2013 Patrick Russell

See `LICENSE`_ for details.

.. _Fullcontact API: http://www.fullcontact.com
.. _Fullcontact.com: http://www.fullcontact.com
.. _Name API docs: http://www.fullcontact.com/docs/?category=person
.. _Person API docs: http://www.fullcontact.com/docs/?category=name
.. _LICENSE: https://github.com/patrick-russell/fullcontacter/blob/master/LICENSE.md