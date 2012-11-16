#API for Fullcontact version 2
#module version 0.5

from urllib2 import urlopen, Request, HTTPError
from urllib import urlencode
from json import load
import logging

#configuration
API_VERSION = 'v2'
END_POINT = 'https://api.fullcontact.com/{0}/'.format(API_VERSION)

CLIENT_VERSION = '0.2'
USER_AGENT = 'Python 2.7.3/Fullcontact Python module version{0}'.format(CLIENT_VERSION)

#initialize logging.
logging.basicConfig(filename='fullcontact.log', level=logging.INFO, format='%(asctime)s %(message)s')


class fullContactError():
    pass


class nameStats(object):
    '''look up first and last name via fullcontact's free name api'''

    def __init__(self, api_key):
        self.api_key = api_key

    def lookup_request(self, method, lkup={}):
        '''method to build the url, make the request, and dump the json to a dict'''

        #ensure proper encoding for look up values
        params = {}
        for k, v in lkup.iteritems():
            params[k] = unicode(v).encode('utf-8')

        params['apiKey'] = self.api_key
        data = urlencode(params)

        #make the url,create the request and set user agent
        lookup_url = "{0}{1}?{2}".format(END_POINT, method, data)
        lookup_req = Request(url=lookup_url, headers={'User-agent': USER_AGENT})

        logging.info('url created ' + lookup_req.get_full_url())
        logging.info(str(lkup))

        try:
            lookup = urlopen(lookup_req)
        except HTTPError, e:
            logging.error(e.code)
            raise fullContactError()
        else:
            name_data = load(lookup)
            logging.info('status code = ' + str(name_data['status']) + ' ' + str(lkup))
            return name_data

    def lookitup(self, method='name/stats.json', fname='', lname=''):
        return self.lookup_request(method, lkup={'givenName': fname, 'familyName': lname})


class personLookup(object):
    '''look up person by email/phone/twitter via fullcontact's paid person api'''

    def __init__(self, api_key):
        self.api_key = api_key

    def lookup_request(self, method, lkup):
        '''method to build up the url, make the request, and, if using JSON dump
          the JSON to a dict valid lookup types are email,twitter,phone,facebookUsername'''

        #ensure proper encoding for look up values
        params = {}
        for k, v in lkup.iteritems():
            params[k] = unicode(v).encode('utf-8')

        params['apiKey'] = self.api_key
        data = urlencode(params)

        #make the url,create the request and set user agent
        lookup_url = '{0}{1}?{2}'.format(END_POINT, method, data)
        lookup_req = Request(url=lookup_url, headers={'User-agent': USER_AGENT})

        logging.info('url created ' + lookup_req.get_full_url())
        logging.info(str(lkup))

        try:
            lookup = urlopen(lookup_req)
        except HTTPError, e:
            logging.error(e.code)
            raise fullContactError()
        else:
            if method == 'person.json':
                person_data = load(lookup)
                logging.info('status code = ' + str(person_data['status']) + ' ' + str(lkup))
            elif method == 'person.html':
                person_data = lookup.read().decode('utf-8')  # TODO need logging
            else:
                person_data = lookup
            # logging.info('status code = '+str(person_data['status'])+' '+str(lkup)) #TODO
            return person_data

    def lookitup(self, lkup_value, lkup_type='email', method='person.json'):
        return self.lookup_request(method, lkup={lkup_type: lkup_value})
