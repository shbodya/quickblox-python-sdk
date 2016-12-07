#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Message:
    """
    Message object
    """

    def __init__(self, id=None, created_at=None, updated_at=None,
                 age=None, attachments=None, read_ids=None,
                 delivered_ids=None, chat_dialog_id=None, date_sent=None,
                 message=None, recipient_id=None, sender_id=None):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.age = age
        self.attachments = attachments
        self.read_ids = read_ids
        self.delivered_ids = delivered_ids
        self.chat_dialog_id = chat_dialog_id
        self.date_sent = date_sent
        self.message = message
        self.recipient_id = recipient_id
        self.sender_id = sender_id

        if not id:
            raise ValueError("Message must have ID")

    @staticmethod
    def from_dict(dict_data):
        if not dict_data:
            return None

        return Message(
            id=dict_data.get('_id'),
            created_at=dict_data.get('created_at'),
            updated_at=dict_data.get('updated_at'),
            age=dict_data.get('age'),
            attachments=dict_data.get('attachments'),
            read_ids=dict_data.get('read_ids'),
            delivered_ids=dict_data.get('delivered_ids'),
            chat_dialog_id=dict_data.get('chat_dialog_id'),
            date_sent=dict_data.get('date_sent'),
            message=dict_data.get('message'),
            recipient_id=dict_data.get('recipient_id'),
            sender_id=dict_data.get('sender_id'),
        )

    def as_dict(self):
        data = {}
        data['_id'] = self.id
        data['created_at'] = self.created_at
        data['updated_at'] = self.updated_at
        data['age'] = self.age
        if self.attachments:
            data['attachments'] = self.attachments
        if self.read_ids:
            data['read_ids'] = self.read_ids
        if self.delivered_ids:
            data['delivered_ids'] = self.delivered_ids
        data['chat_dialog_id'] = self.chat_dialog_id
        data['date_sent'] = self.date_sent
        data['message'] = self.message
        data['recipient_id'] = self.recipient_id
        data['sender_id'] = self.sender_id
        return data
