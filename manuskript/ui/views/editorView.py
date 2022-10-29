#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class EditorView:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("ui/editor.glade")

        self.widget = builder.get_object("editor_view")

    def show(self):
        self.widget.show_all()