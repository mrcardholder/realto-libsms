# -*- coding: utf-8 -*-

class BaseSmsTransport(object):
    '''SmsTransport interface'''

    def send(self, phone, msg):
        '''Invokes message sending logic'''
        raise NotImplementedError
