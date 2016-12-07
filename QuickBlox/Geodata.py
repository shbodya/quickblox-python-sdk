#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Geodata:
    """
    Geodata object
    """

    def __init__(self, id=None, application_id=None, created_at=None,
                 latitude=None, longitude=None, updated_at=None,
                 status=None, user_id=None, created_at_timestamp=None):
        self.id = id
        self.application_id = application_id
        self.created_at = created_at
        self.latitude = latitude
        self.longitude = longitude
        self.status = status
        self.created_at_timestamp = created_at_timestamp
        self.updated_at = updated_at
        self.user_id = user_id

        if not latitude and not longitude:
            raise ValueError("Geodata must have latitude or longitude")

    @staticmethod
    def from_dict(dict_data):
        if not dict_data:
            return None
        geo_data = dict_data.get('geo_datum')

        return Geodata(
            id=geo_data.get('id'),
            application_id=geo_data.get('application_id'),
            created_at=geo_data.get('created_at'),
            latitude=geo_data.get('latitude'),
            longitude=geo_data.get('longitude'),
            status=geo_data.get('status'),
            created_at_timestamp=geo_data.get('created_at_timestamp'),
            updated_at=geo_data.get('updated_at'),
            user_id=geo_data.get('user_id'),
        )

    def as_dict(self):
        return {
            'id': self.id,
            'application_id': self.application_id,
            'created_at': self.created_at,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'status': self.status,
            'created_at_timestamp': self.created_at_timestamp,
            'updated_at': self.updated_at,
            'user_id': self.user_id,
        }
