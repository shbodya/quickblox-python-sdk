# -*- coding: utf-8 -*-

from .Client import Client
from .Sessions import Session
from .User import User
from .Dialog import Dialog
from .Message import Message
from .Geodata import Geodata
from .Blob import Blob
from .Version import __version__

__title__ = 'QuickBlox'
__author__ = 'bogdan.shaparenko@injoit.com'

__all__ = [
    'Client', 'Session', 'User', 'Dialog',
    'Message', 'Geodata', 'Blob', '__version__'
]
