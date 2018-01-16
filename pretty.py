# -*- encoding: utf-8 -*-
import os
import subprocess

from pelican import signals


def tidy_html(pelican):
    """Tidy the HTML of Pelican output files.

    Spawns a series of subprocesses to tidy-up output HTML using the
    node.js library pretty.

    """
    js_dirpath = os.path.dirname(os.path.realpath(__file__))
    for dirpath, _, filenames in os.walk(pelican.settings['OUTPUT_PATH']):
        for name in filenames:
            if os.path.splitext(name)[1] in ('.html', ):
                filepath = os.path.join(dirpath, name)
                js_filepath = os.path.join(js_dirpath, "pretty_html.js")
                cmd_content = [
                    "node",
                    "{0}".format(js_filepath),
                    "--html={0}".format(filepath),
                ]
                p = subprocess.Popen(cmd_content)
                p.wait()


def register():
    signals.finalized.connect(tidy_html)
