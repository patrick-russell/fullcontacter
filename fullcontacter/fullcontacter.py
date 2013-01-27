'''
Fullcontacter: A wrapper for the excellent and helpful Fullcontact.com APIs
Fullcontacter version 0.3

Provides the exposed API for the Fullcontacter module. This should be considered alpha.
Future versions of this API will be different and more featureful.

'''

from lookup import lookup_request
import logging

#initialize logging.
logging.basicConfig(filename='fullcontacter.log', level=logging.INFO, format='%(asctime)s %(message)s')


class fullcontacterError():
    pass


class personLookup(object):
    '''look up person by email/phone/twitter/facebook via fullcontact's paid person api'''

    def __init__(self, api_key):
        self.api_key = api_key

    def lookitup(self, lookup_value, lookup_type, format='.json'):
        '''
          Valid lookup types are email,twitter,phone,facebookUsername
          Phone numbers should be formatted +country code area code number
          (ie +13035555555)
        '''

        if lookup_type == 'email':
            person_data = lookup_request('person', format, self.api_key, email=lookup_value)
        elif lookup_type == 'twitter':
            person_data = lookup_request('person', format, self.api_key, twitter=lookup_value)
        elif lookup_type == 'phone':
            person_data = lookup_request('person', format, self.api_key, phone=lookup_value)
        elif lookup_type == 'facebookUsername':
            person_data = lookup_request('person', format, self.api_key, facebookUsername=lookup_value)
        else:
            logging.info('ERROR unknown lookup type: ' + lookup_type)
            raise fullcontacterError()
            print 'Unknown lookup type'

        logging.info('url created ' + person_data['url'])
        logging.info(str(lookup_type) + ': ' + str(lookup_value))

        return person_data['lookup']


class nameStats(object):
    '''look up a name, first and/or last name via fullcontact's free name api'''

    def __init__(self, api_key):
        self.api_key = api_key

    def lookitup(self, fname=None, lname=None, name=None, format='.json'):

        name_data = lookup_request('name/stats', format, self.api_key,
                    givenName=fname, familyName=lname, name=name)

        logging.info('url created ' + name_data['url'])

        return name_data['lookup']
