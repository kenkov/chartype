#! /usr/bin/env python
# coding:utf-8

from __future__ import division
from chartype import *
from nose.tools import raises


def hiragana2katakana_test():
    ch = Chartype()
    for i, j in [("あ", "ア"), ("い", "イ"), ("う", "ウ")]:
        assert ch.hiragana2katakana(i) == j


def katakana2hiragana_test():
    ch = Chartype()
    for i, j in [("ア", "あ"), ("イ", "い"), ("ウ", "う")]:
        assert ch.katakana2hiragana(i) == j


def half2full_test():
    ch = Chartype()
    for i, j in [("ｱ", "ア"), ("ｲ", "イ"), ("ｳ", "ウ")]:
        assert ch.half2full(i) == j

def full2half_test():
    ch = Chartype()
    for i, j in [("ア", "ｱ"), ("イ", "ｲ"), ("ウ", "ｳ")]:
        assert ch.full2half(i) == j


@raises(CharTypeException)
def half2full_CharTypeException_test():
    ch = Chartype()
    for obj in ["今", "1", "ア", "a", "A"]:
        ch.half2full(obj)

@raises(CharException)
def half2full_CharException_test():
    ch = Chartype()
    for obj in ["ほげふが", object]:
        ch.half2full(obj)


if __name__ == '__main__':
    pass

