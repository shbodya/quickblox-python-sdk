#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json
import random
import time
import hmac
from hashlib import sha1

try:
    import requests
except ImportError:
    raise "Please install requests"

try:
    from urllib.parse import urlparse, parse_qs
except ImportError:
    from urlparse import urlparse, parse_qs

from .Sessions import Session
from .User import User
from .Dialog import Dialog
from .Message import Message
from .Geodata import Geodata
from .Blob import Blob
from .Version import __version__

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'

URI_SESSION = 'session'
URI_LOGIN = 'login'
URI_USER = 'users'
URI_GEODATA = 'geodata'
URI_BLOBS = 'blobs'
URI_CUSTOM_DATA = 'data'
URI_DIALOG = 'chat/Dialog'
URI_MESSAGE = 'chat/Message'


class QBException(Exception):
    def __init__(self, message, http_code=None, code=None, error_id=None):
        super(QBException, self).__init__(message)
        self.http_code = http_code
        self.code = code
        self.error_id = error_id


class Client(object):
    """
    Simple API Client
    """
    def __init__(self, application_id, authorization_key,
                 auth_secret, api_url):
        """
        Init
        """
        self.application_id = application_id
        self.authorization_key = authorization_key
        self.auth_secret = auth_secret
        self.api_url = api_url

    def _get_url(self, uri):
        return 'https://' + self.api_url + '/' + uri + '.json'

    def _get_base_headers(self):
        content_type = 'application/json'
        return {
            'User-Agent': 'QuickBloxPy/' + __version__,
            'Content-Type': content_type,
            'QuickBlox-REST-API-Version': '0.1.1'
        }

    def _create_signature(self, secret_key, string):
        h = hmac.new(secret_key.encode('utf-8'), string.encode('utf-8'),
                     digestmod=sha1)
        return h.hexdigest()

    def __parse_blob_params(self, uri):
        query = parse_qs(uri.query)
        params = {
            'Content-Type': query.get('Content-Type')[0],
            'Expires': query.get('Expires')[0],
            'acl': query.get('acl')[0],
            'key': query.get('key')[0],
            'policy': query.get('policy')[0],
            'success_action_status': query.get('success_action_status')[0],
            'x-amz-algorithm': query.get('x-amz-algorithm')[0],
            'x-amz-credential': query.get('x-amz-credential')[0],
            'x-amz-date': query.get('x-amz-date')[0],
            'x-amz-signature': query.get('x-amz-signature')[0],
        }
        return params

    def _request(self, method, url, data=None, headers=None, params=None):
        """
        Request prototype
        """
        headers = self._get_base_headers()
        if headers:
            headers.update(headers)
        result = requests.request(
            method,
            url,
            headers=headers,
            data=(json.dumps(data) if data else None),
            params=params
        )

        if result.ok:
            try:
                return result.json()
            except ValueError:
                return result
        try:
            error = result.json()
            raise QBException(
                error.get('errors'),
            )
        except ValueError:
            raise QBException(
                result.text,
                http_code=result.status_code,
            )

    def __upload(self, url, data=None, files=None):
        """
        Upload request prototype
        """
        result = requests.request(
            POST,
            url,
            data=data,
            files=files
        )

        if result.ok:
            try:
                return result.json()
            except ValueError:
                return result
        try:
            error = result.json()
            raise QBException(
                error.get('errors'),
            )
        except ValueError:
            raise QBException(
                result.text,
                http_code=result.status_code,
            )

# Session
    def create_session(self):
        """
        Create Session
        """
        nonce = str(random.randint(100000, 1000000000))
        timestamp = int(round(time.time()))
        tmp_str = 'application_id={app_id}&auth_key={auth_key}' \
                  '&nonce={nonce}&timestamp={timestamp}' \
                  .format(app_id=self.application_id,
                          auth_key=self.authorization_key,
                          nonce=nonce,
                          timestamp=timestamp
                          )
        sign = self._create_signature(self.auth_secret, tmp_str)
        params = {'application_id': self.application_id,
                  'auth_key': self.authorization_key,
                  'nonce': nonce,
                  'timestamp': timestamp,
                  'signature': sign
                  }
        return Session.from_dict(
            self._request(
                POST,
                self._get_url(URI_SESSION),
                params=params
            )
        )

    def destroy_session(self, token):
        """
        Destroy Session
        """
        params = {
            "token": token
            }
        return self._request(
            DELETE,
            self._get_url(URI_SESSION),
            params=params
        )

    def create_user_session(self, login, password):
        """
        Create Session with User
        """
        nonce = str(random.randint(100000, 1000000000))
        timestamp = int(round(time.time()))
        tmp_str = 'application_id={app_id}&auth_key={auth_key}' \
                  '&nonce={nonce}&timestamp={timestamp}&user[login]={login}' \
                  '&user[password]={password}' \
                  .format(app_id=self.application_id,
                          auth_key=self.authorization_key,
                          nonce=nonce,
                          timestamp=timestamp,
                          login=login,
                          password=password
                          )
        sign = self._create_signature(self.auth_secret, tmp_str)
        params = {'application_id': self.application_id,
                  'auth_key': self.authorization_key,
                  'nonce': nonce,
                  'timestamp': timestamp,
                  'signature': sign,
                  'user[login]': login,
                  'user[password]': password
                  }
        return Session.from_dict(
            self._request(
                POST,
                self._get_url(URI_SESSION),
                params=params
            )
        )

# User
    def create_user(self, token, login, password):
        """
        Create User
        """
        params = {
            'user[login]': login,
            'user[password]': password,
            'token': token
            }
        return User.from_dict(
            self._request(
                POST,
                self._get_url(URI_USER),
                params=params
            )
        )

    def update_user(self, token, user_id, login=None, blob_id=None,
                    email=None, external_user_id=None, facebook_id=None,
                    twitter_id=None, full_name=None, phone=None, website=None,
                    tag_list=None, custom_data=None):
        """
        Update User
        """
        params = {}
        if login:
            params['user[login]'] = login
        if blob_id:
            params['user[blob_id]'] = blob_id
        if email:
            params['user[email]'] = email
        if external_user_id:
            params['user[external_user_id]'] = external_user_id
        if facebook_id:
            params['user[facebook_id]'] = facebook_id
        if twitter_id:
            params['user[twitter_id]'] = twitter_id
        if full_name:
            params['user[full_name]'] = full_name
        if phone:
            params['user[phone]'] = phone
        if website:
            params['user[website]'] = website
        if tag_list:
            params['user[tag_list]'] = tag_list
        if custom_data:
            params['user[custom_data]'] = custom_data
        params['token'] = token
        return User.from_dict(
            self._request(
                PUT,
                self._get_url(URI_USER + '/' + str(user_id)),
                params=params
            )
        )

    def get_all_users(self, token, page=None, per_page=None):
        """
        Create User
        """
        params = {}
        if page:
            params['page'] = page
        if per_page:
            params['per_page'] = per_page
        params['token'] = token
        return self._request(
            GET,
            self._get_url(URI_USER),
            params=params
        )

    def delete_user(self, token, user_id):
        """
        Delete User
        """
        params = {'token': token}
        return self._request(
            DELETE,
            self._get_url(URI_USER + '/' + str(user_id)),
            params=params
        )

# Geodata
    def create_geodata(self, token, latitude, longitude, status=None):
        """
        Create Geodata
        """
        params = {
            'geo_data[latitude]': latitude,
            'geo_data[longitude]': longitude,
            'token': token
            }
        if status:
            params['geo_data[status]'] = status
        return Geodata.from_dict(
            self._request(
                POST,
                self._get_url(URI_GEODATA),
                params=params
            )
        )

    def list_geodata(self, token):
        """
        Get Geodata List
        """
        params = {'token': token}
        return self._request(
            GET,
            self._get_url(URI_GEODATA + '/find'),
            params=params
        )

# Content

    def create_blob(self, token, name, content_type,
                    public=None, tag_list=None):
        """
        Create File
        """
        params = {
            'token': token,
            'blob[content_type]': content_type,
            'blob[name]': name
            }
        if public:
            params['blob[public]'] = public
        if tag_list:
            params['blob[tag_list]'] = tag_list
        return Blob.from_dict(
            self._request(
                POST,
                self._get_url(URI_BLOBS),
                params=params
            )
        )

    def list_content(self, token):
        """
        Get Files List
        """
        params = {'token': token}
        return self._request(
            GET,
            self._get_url(URI_BLOBS),
            params=params
        )

    def upload_content(self, blob, file):
        """
        Upload File
        """
        uri = urlparse(blob.blob_object_access.get('params'))
        params = self.__parse_blob_params(uri)
        upload_link = uri._replace(query=None).geturl()
        files = {'file': file}
        return self.__upload(upload_link,
                             data=params,
                             files=files)

    def mark_uploaded(self, token, blob, size):
            """
            Declaring file uploaded
            """
            params = {
                'token': token,
                'blob[size]': size
                }
            return self._request(
                POST,
                self._get_url(URI_BLOBS + '/' + str(blob.id) + '/complete'),
                params=params
            )

    def create_and_upload(self, token, name, file, content_type, size,
                          public=None, tag_list=None):
        """
        Create blod and upload uploade file
        """
        blob = self.create_blob(token, name, content_type)
        result = self.upload_content(blob, file)
        if result.ok:
            self.mark_uploaded(token, blob, size)
            return blob
        else:
            return QBException(
                result.text,
                http_code=result.status_code,
            )

    def delete_content(self, token, blob_id):
        """
        Delete File
        """
        params = {'token': token}
        return self._request(
            DELETE,
            self._get_url(URI_BLOBS + '/' + str(blob_id)),
            params=params
        )

# Dialog
    def create_dialog(self, token, type, occupants_ids, name, photo=None):
        """
        Create Dialog
        """
        params = {
            'type': type,
            'occupants_ids': occupants_ids,
            'name': name,
            'token': token
            }
        if photo:
            params['photo'] = photo
        return Dialog.from_dict(
            self._request(
                POST,
                self._get_url(URI_DIALOG),
                params=params
            )
        )

    def get_dialogs(self, token):
        """
        Retrieve dialogs
        """
        params = {'token': token}
        return self._request(
            GET,
            self._get_url(URI_DIALOG),
            params=params
        )

    def update_dialog(self, token, chat_dialog_id, push_all=None,
                      pull_all=None, occupants_ids=None,
                      name=None, photo=None):
        """
        Update Dialog
        """
        params = {'token': token}
        if push_all:
            params['push_all[occupants_ids][]'] = push_all
        if pull_all:
            params['pull_all[occupants_ids][]'] = pull_all
        if name:
            params['name'] = name
        if photo:
            params['photo'] = photo
        return Dialog.from_dict(
            self._request(
                PUT,
                self._get_url(URI_DIALOG + '/' + str(chat_dialog_id)),
                params=params
            )
        )

    def get_messages(self, token, chat_dialog_id, limit=None,
                     skip=None, count=None, mark_as_read=None):
        """
        Retrieve messages
        """
        params = {
            'token': token,
            'chat_dialog_id': chat_dialog_id
            }
        if limit:
            params['limit'] = limit
        if skip:
            params['skip'] = skip
        if count:
            params['count'] = count
        if mark_as_read:
            params['mark_as_read'] = mark_as_read
        return self._request(
            GET,
            self._get_url(URI_MESSAGE),
            params=params
        )

    def unread_messages(self, token, chat_dialog_ids):
        """
        Retrieve unread messages count
        """
        params = {
            'token': token,
            'chat_dialog_ids': chat_dialog_ids
            }
        return self._request(
            GET,
            self._get_url(URI_DIALOG + str(chat_dialog_ids)),
            params=params
        )

    def delete_dialog(self, token, chat_dialog_id, force=None):
        """
        Delete Dialog
        """
        params = {'token': token}
        if force:
            params['force'] = force
        return self._request(
            DELETE,
            self._get_url(URI_DIALOG + '/' + str(chat_dialog_id)),
            params=params
        )

# Message

    def create_message(self, token, chat_dialog_id=None, recipient_id=None,
                       message=None, send_to_chat=None, markable=None):
        """
        Create Message
        """
        if not chat_dialog_id and not recipient_id:
            raise ValueError("Message need chat_dialog_id or recipient_id")

        params = {'token': token}
        if chat_dialog_id:
            params['chat_dialog_id'] = chat_dialog_id
        if recipient_id:
            params['recipient_id'] = recipient_id
        if message:
            params['message'] = message
        if send_to_chat:
            params['send_to_chat'] = send_to_chat
        if markable:
            params['markable'] = markable
        return Message.from_dict(
            self._request(
                POST,
                self._get_url(URI_MESSAGE),
                params=params
            )
        )

    def update_message(self, token, chat_dialog_id, message_id, read=None,
                       message=None, delivered=None):
        """
        Update Message
        """
        params = {
            'token': token,
            'chat_dialog_id': chat_dialog_id
            }
        if read:
            params['read'] = read
        if message:
            params['message'] = message
        if delivered:
            params['delivered'] = delivered
        return self._request(
            PUT,
            self._get_url(URI_MESSAGE + str(message_id)),
            params=params
        )

    def delete_message(self, token, message_id):
        """
        Delete Message
        """
        params = {'token': token}
        return self._request(
            DELETE,
            self._get_url(URI_MESSAGE + '/' + str(message_id)),
            params=params
        )

# Custom Objects

    def create_custom_data(self, token, class_name, data=None):
        """
        Create new record
        """
        params = {'token': token}
        if data:
            params.update(data)
        return self._request(
            POST,
            self._get_url(URI_CUSTOM_DATA + '/' + str(class_name)),
            params=params
        )

    def update_custom_data(self, token, class_name, record_id,
                           parameters=None):
        """
        Retrieve records
        """
        params = {'token': token}
        if parameters:
            params.update(parameters)
        return self._request(
            PUT,
            self._get_url(URI_CUSTOM_DATA + '/' + str(class_name) +
                          '/' + str(record_id)),
            params=params
        )

    def get_custom_data(self, token, class_name):
        """
        Retrieve records
        """
        params = {'token': token}
        return self._request(
            GET,
            self._get_url(URI_CUSTOM_DATA + '/' + str(class_name)),
            params=params
        )

    def delete_custom_data(self, token, class_name, record_id):
        """
        Delete records
        """
        params = {'token': token}
        return self._request(
            DELETE,
            self._get_url(URI_CUSTOM_DATA + '/' + str(class_name) +
                          '/' + str(record_id)),
            params=params
        )
