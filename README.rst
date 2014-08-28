==============
realto-libsms
==============
Realto-libsms is a thin wrapper library for sending SMS via multiple transports.

Installation
============
::

    pip install git+git://github.com/mrcardholder/realto-libsms.git

Or use
::

    git clone https://github.com/mrcardholder/realto-libsms.git
    cd realto-libsms
    python setup.py sdist
    pip install dist/realto-libsms-0.1.tar.gz


Usage
===========
::

    from libsms import sms_transport
    from libsms import sms_transports

    sms_transport.send(phone='123123', msg='qweqwe')
    sms_transports['dummy'].send(phone='123123', msg='qweqwe')
