# -*- coding: utf-8 -*-
'''Simple tests for realto-libsms'''
import unittest

from django.conf import settings

test_settings = {
        'default': {
            'BACKEND' : 'libsms.backends.sms.SmsTransport',
            'PARAMS' : {
                'login' : 'some_login',
                'password' : 'some_password',
                }
            },
        'dummy': {
            'BACKEND' : 'libsms.backends.dummy.SmsTransport',
            },
        'other': {
            'BACKEND' : 'libsms.backends.other.SmsTransport',
            'PARAMS' : {
                'login' : 'some_login',
                'password' : 'some_password',
                'var1' : 'var1',
                'var2' : 'var2',
                }
            }
        }

if not settings.configured:
    settings.configure(SMS_TRANSPORTS=test_settings)

class TestLibSms(unittest.TestCase):
    def test_001(self):
        from libsms import sms_transport
        from libsms import sms_transports
        self.assertIsNotNone(sms_transport)
        sms_transport.send(phone='123123', msg='qweqwe')
        sms_transports['dummy'].send(phone='123123', msg='qweqwe')

if __name__ == '__main__':
    unittest.main()
