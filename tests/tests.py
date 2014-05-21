#!/usr/bin/env python

import imurl
from nose.tools import eq_


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
