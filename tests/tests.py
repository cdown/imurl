#!/usr/bin/env python

import imurl
import json
import os
from nose.tools import eq_


def relative(path):
    return os.path.join(os.path.dirname(__file__), path)


def test_album_id_from_url_without_url():
    out = imurl.album_id_from_url("Rbab9")
    eq_("Rbab9", out)


def test_album_id_from_url_basic():
    out = imurl.album_id_from_url("http://imgur.com/a/Rbab9")
    eq_("Rbab9", out)


def test_album_id_from_url_with_layout():
    out = imurl.album_id_from_url("http://imgur.com/a/Rbab9/layout/horizontal")
    eq_("Rbab9", out)


def test_album_id_from_url_with_anchor():
    out = imurl.album_id_from_url("http://imgur.com/a/Rbab9#0")
    eq_("Rbab9", out)


def test_album_id_from_url_with_layout_and_anchor():
    out = imurl.album_id_from_url("http://imgur.com/a/Rbab9/layout/horizontal#0")
    eq_("Rbab9", out)

def test_filter_image_urls():
    with open(relative("data/album_response.json")) as api_file:
        api_response = json.load(api_file)

    eq_([
        'http://i.imgur.com/24nLu.jpg',
        'http://i.imgur.com/Ziz25.jpg',
        'http://i.imgur.com/9tzW6.jpg',
        'http://i.imgur.com/dFg5u.jpg',
        'http://i.imgur.com/oknLx.jpg',
        'http://i.imgur.com/OL6tC.jpg',
        'http://i.imgur.com/cJ9cm.jpg',
        'http://i.imgur.com/7BtPN.jpg',
        'http://i.imgur.com/42ib8.jpg',
        'http://i.imgur.com/BbwIx.jpg',
        'http://i.imgur.com/x7b91.jpg',
    ], list(imurl.filter_image_urls(api_response))
    )
