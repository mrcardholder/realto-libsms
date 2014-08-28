# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

class ConfigManager(dict):
    '''Wraps module configuration in a dict-like manner'''
    def __init__(self):
        super(ConfigManager, self).__init__()
        self.configured = False
        try:
            config = getattr(settings, 'SMS_TRANSPORTS')
            super(ConfigManager, self).update(config)
            self.configured = True
        except ImproperlyConfigured:
            pass

    def __getitem__(self, key):
        '''FIXME: memoize constructed objects for efficiency?'''
        if self.configured:
            rv = self.__transport_ctor(key)
        else:
            rv = None
        return rv

    def __transport_ctor(self, name):
        config_section = self.get(name, None)
        if not config_section:
            raise ImproperlyConfigured("libsms: alias '%s' not found" % (name))
        classpath = config_section.get('BACKEND', None) 
        if not classpath:
            raise ImproperlyConfigured("libsms: BACKEND is missing for alias '%s'" % (name))
        try:
            import_path, classname =  classpath.rsplit('.', 1)
            transport_module = import_module(import_path)
            transport_impl = getattr(transport_module, classname)
        except (ValueError, ImportError, AttributeError) as e: # need more ... to unpack
            raise ImproperlyConfigured("libsms: BACKEND is incorrect for alias '%s': %s" % (name, e))
        transport_params = config_section.get('PARAMS', {}) 
        return transport_impl(**transport_params)


sms_transports = ConfigManager()

sms_transport = sms_transports['default']

__all__ = ['sms_transport', 'sms_transports']
