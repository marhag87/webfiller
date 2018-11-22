"""
Main module for webfiller
"""
import subprocess
import re
from webfiller.config import (
    Config,
    ConfigError,
)


class Webfiller(object):
    """Main class"""
    def __init__(self):
        self.__config = Config

    @staticmethod
    def run_tool(tool, *args):
        """
        Run the specified tool
        :param tool: Tool to run
        :param args: Arguments to the tool
        :return: Output from run
        """
        run_list = [tool]
        for arg in args:
            run_list.append(arg)
        return subprocess.getoutput(" ".join(run_list))

    def xdotool(self, *args):
        """Run xdotool"""
        return self.run_tool(
            'xdotool',
            *args,
        )

    def run_pass(self, *args):
        """Run pass"""
        return self.run_tool(
            'pass',
            *args,
        )

    @property
    def url(self):
        """Get the url of the currently active window"""
        title = str(self.xdotool('getactivewindow', 'getwindowname'))
        split_title = title.split(' - ')
        if split_title[-1] == 'Google Chrome':
            return split_title[0]

    @staticmethod
    def password_cleanup(password):
        """Output password in format xdotool can handle"""
        password = password.splitlines()[0]
        split = password.split("'")
        joined = """'"'"'""".join(split)
        password = "'{}'".format(joined)
        return re.sub("''$", '', re.sub("^''", '', password))

    def print_login(self):
        """Fetch and input login information to the active window"""
        try:
            config = self.__config(self.url)
        except ConfigError:
            return

        if config.username is not None:
            self.xdotool(
                'type',
                '--clearmodifiers',
                '"{}"'.format(config.username),
            )
            self.xdotool(
                'key',
                '--clearmodifiers',
                'Tab',
            )

        if config.password is not None:
            # Clean up keydown, or Super will hang
            self.xdotool(
                'keyup',
                'Super'
            )

            password = self.run_pass(
                config.password,
            )
            self.xdotool(
                'type',
                '--clearmodifiers',
                self.password_cleanup(password),
            )
