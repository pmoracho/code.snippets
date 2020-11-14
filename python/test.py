#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gettext
_ = gettext.gettext


def install_lang(l):
	global _
	DIR = "locale"
	APP = "test"

	lang = gettext.translation(APP, DIR, languages=[l], fallback=True)
	lang.install()
	_ = lang.gettext


if __name__ == '__main__':
	install_lang("EN")
	print(_("Cadena traducida"))

	install_lang("ES")
	print(_("Cadena traducida"))
