#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Blob:
    """
    Blob object
    """

    def __init__(self, id=None, blob_status=None, content_type=None,
                 created_at=None, last_read_access_ts=None, lifetime=None,
                 name=None, public=None, ref_count=None, set_completed_at=None,
                 size=None, uid=None, updated_at=None, blob_object_access=None
                 ):
        self.id = id
        self.blob_status = blob_status
        self.content_type = content_type
        self.created_at = created_at
        self.last_read_access_ts = last_read_access_ts
        self.lifetime = lifetime
        self.name = name
        self.public = public
        self.ref_count = ref_count
        self.set_completed_at = set_completed_at
        self.size = size
        self.uid = uid
        self.updated_at = updated_at
        self.blob_object_access = blob_object_access

        if not id:
            raise ValueError("Blob must have ID or token")

    @staticmethod
    def from_dict(dict_data):
        if not dict_data:
            return None
        blob = dict_data.get('blob')

        return Blob(
            id=blob.get('id'),
            blob_status=blob.get('blob_status'),
            content_type=blob.get('content_type'),
            created_at=blob.get('created_at'),
            last_read_access_ts=blob.get('last_read_access_ts'),
            lifetime=blob.get('lifetime'),
            name=blob.get('name'),
            public=blob.get('public'),
            ref_count=blob.get('ref_count'),
            set_completed_at=blob.get('set_completed_at'),
            size=blob.get('size'),
            uid=blob.get('uid'),
            updated_at=blob.get('updated_at'),
            blob_object_access=blob.get('blob_object_access'),
        )

    def as_dict(self):
        data = {}
        if self.blob_status:
            data['blob_status'] = self.blob_status
        if self.last_read_access_ts:
            data['last_read_access_ts'] = self.last_read_access_ts
        if self.set_completed_at:
            data['set_completed_at'] = self.set_completed_at
        if self.size:
            data['size'] = self.size
        if self.blob_object_access:
            data['blob_object_access'] = self.blob_object_access
        data['uid'] = self.uid
        data['ref_count'] = self.ref_count
        data['public'] = self.public
        data['name'] = self.name
        data['lifetime'] = self.lifetime
        data['content_type'] = self.content_type
        data['created_at'] = self.created_at
        data['updated_at'] = self.updated_at
        data['id'] = self.id
        return data
