import base64
import json
import subprocess

import sys


class Git:
    def _read_command(self, command):
        result = subprocess.run(command.split(), stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')

    def _print_command(self, command):
        subprocess.Popen([command], shell=True).wait()

    def get_current_branch(self):
        text = self._read_command("git rev-parse --abbrev-ref HEAD")
        return text.strip()
