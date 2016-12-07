#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Session:
    """
    Session object
    """

    def __init__(self, id=None, application_id=None, created_at=None,
                 nonce=None, token=None, device_id=None,
                 ts=None, updated_at=None, user_id=None):
        self.id = id
        self.application_id = application_id
        self.created_at = created_at
        self.nonce = nonce
        self.token = token
        self.device_id = device_id
        self.ts = ts
        self.updated_at = updated_at
        self.user_id = user_id

        if not id and not token:
            raise ValueError("Session must have ID or token")

    @staticmethod
    def from_dict(dict_data):
        if not dict_data:
            return None
        session = dict_data.get('session')

        return Session(
            id=session.get('id'),
            application_id=session.get('application_id'),
            created_at=session.get('created_at'),
            nonce=session.get('nonce'),
            token=session.get('token'),
            device_id=session.get('device_id'),
            ts=session.get('ts'),
            updated_at=session.get('updated_at'),
            user_id=session.get('user_id'),
        )

    def as_dict(self):
        return {
            'id': self.id,
            'application_id': self.application_id,
            'created_at': self.created_at,
            'nonce': self.nonce,
            'token': self.token,
            'device_id': self.device_id,
            'ts': self.ts,
            'updated_at': self.updated_at,
            'user_id': self.user_id,
        }
