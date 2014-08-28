# -*- coding: utf-8 -*-
from libsms.backends import BaseSmsTransport

class SmsTransport(BaseSmsTransport):
    def __init__(self, **kw):
        self.params = kw

    def send(self, phone, msg):
        print "transport {} called with {}".format(self.__class__, locals())
