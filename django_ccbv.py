"""
by Leonardo Borges Avelino (lborgav@gmail.com)
"""
import sublime
import sublime_plugin

import webbrowser


def go_to_ccbv(q):
    url = 'http://ccbv.co.uk/' + q
    webbrowser.open_new_tab(url)


class DjangoCcbvCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for selection in self.view.sel():
            q = self.view.substr(selection)
            go_to_ccbv(q)
