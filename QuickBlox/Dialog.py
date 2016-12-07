#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Dialog:
    """
    Dialog object
    """

    def __init__(self, id=None, created_at=None, updated_at=None,
                 last_message=None, last_message_date_sent=None, name=None,
                 last_message_user_id=None, photo=None, occupants_ids=None,
                 type=None, xmpp_room_jid=None, unread_messages_count=None):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_message = last_message
        self.last_message_date_sent = last_message_date_sent
        self.last_message_user_id = last_message_user_id
        self.name = name
        self.photo = photo
        self.occupants_ids = occupants_ids
        self.type = type
        self.xmpp_room_jid = xmpp_room_jid
        self.unread_messages_count = unread_messages_count

        if not id:
            raise ValueError("Dialog must have ID")

    @staticmethod
    def from_dict(dict_data):
        if not dict_data:
            return None

        return Dialog(
            id=dict_data.get('_id'),
            created_at=dict_data.get('created_at'),
            updated_at=dict_data.get('updated_at'),
            last_message=dict_data.get('last_message'),
            last_message_date_sent=dict_data.get('last_message_date_sent'),
            last_message_user_id=dict_data.get('last_message_user_id'),
            name=dict_data.get('name'),
            photo=dict_data.get('photo'),
            occupants_ids=dict_data.get('occupants_ids'),
            type=dict_data.get('type'),
            xmpp_room_jid=dict_data.get('xmpp_room_jid'),
            unread_messages_count=dict_data.get('unread_messages_count'),
        )

    def as_dict(self):
        data = {}
        if self.last_message:
            data['last_message'] = self.last_message
        if self.last_message_date_sent:
            data['last_message_date_sent'] = self.last_message_date_sent
        if self.last_message_user_id:
            data['last_message_user_id'] = self.last_message_user_id
        if self.name:
            data['name'] = self.name
        if self.photo:
            data['photo'] = self.photo
        data['xmpp_room_jid'] = self.xmpp_room_jid
        data['unread_messages_count'] = self.unread_messages_count
        data['type'] = self.type
        data['occupants_ids'] = self.occupants_ids
        data['created_at'] = self.created_at
        data['updated_at'] = self.updated_at
        data['_id'] = self.id
        return data
