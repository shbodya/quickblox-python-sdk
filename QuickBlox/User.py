#!/usr/bin/env python
# -*- coding: utf-8 -*-


class User:
    """
    User object
    """

    def __init__(self, id=None, full_name=None, email=None, login=None,
                 phone=None, website=None, created_at=None, updated_at=None,
                 last_request_at=None, external_user_id=None, facebook_id=None,
                 twitter_id=None, twitter_digits_id=None, blob_id=None,
                 custom_data=None, user_tags=None):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.login = login
        self.phone = phone
        self.website = website
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_request_at = last_request_at
        self.external_user_id = external_user_id
        self.facebook_id = facebook_id
        self.twitter_id = twitter_id
        self.twitter_digits_id = twitter_digits_id
        self.blob_id = blob_id
        self.custom_data = custom_data
        self.user_tags = user_tags

        if not login and not email:
            raise ValueError("User must have login or email")

    @staticmethod
    def from_dict(dict_data):
        if not dict_data:
            return None
        user = dict_data.get('user')

        return User(
            id=user.get('id'),
            full_name=user.get('full_name'),
            email=user.get('email'),
            login=user.get('login'),
            phone=user.get('phone'),
            website=user.get('website'),
            created_at=user.get('created_at'),
            updated_at=user.get('updated_at'),
            last_request_at=user.get('last_request_at'),
            external_user_id=user.get('external_user_id'),
            facebook_id=user.get('facebook_id'),
            twitter_id=user.get('twitter_id'),
            twitter_digits_id=user.get('twitter_digits_id'),
            blob_id=user.get('blob_id'),
            custom_data=user.get('custom_data'),
            user_tags=user.get('user_tags'),
        )

    def as_dict(self):
        data = {}
        if self.full_name:
            data['full_name'] = self.full_name
        if self.email:
            data['email'] = self.email
        if self.login:
            data['login'] = self.login
        if self.phone:
            data['phone'] = self.phone
        if self.website:
            data['website'] = self.website
        if self.last_request_at:
            data['last_request_at'] = self.last_request_at
        if self.external_user_id:
            data['external_user_id'] = self.external_user_id
        if self.facebook_id:
            data['facebook_id'] = self.facebook_id
        if self.twitter_id:
            data['twitter_id'] = self.twitter_id
        if self.twitter_digits_id:
            data['twitter_digits_id'] = self.twitter_digits_id
        if self.blob_id:
            data['blob_id'] = self.blob_id
        if self.custom_data:
            data['custom_data'] = self.custom_data
        if self.user_tags:
            data['user_tags'] = self.user_tags
        data['created_at'] = self.created_at
        data['updated_at'] = self.updated_at
        data['id'] = self.id
        return data
