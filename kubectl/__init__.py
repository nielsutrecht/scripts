import base64
import json
import subprocess

import sys

class KubeCtl:
    def _read_command(self, command):
        result = subprocess.run(command.split(), stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8')

    def _print_command(self, command):
        subprocess.Popen([command], shell=True).wait()

    def list_pods(self):
        text = self._read_command("kubectl get pods -o name")
        return list(map(lambda it: it.split('/')[1], text.splitlines()))

    def list_secrets(self):
        text = self._read_command("kubectl get secrets -o name")
        return list(map(lambda it: it.split('/')[1], text.splitlines()))


    def read_secret(self, secret):
        text = self._read_command("kubectl get secret " + secret + " -o json")
        data = json.loads(text)['data']
        return list(map(lambda kv: (kv[0], base64.b64decode(kv[1]).decode('utf-8')), data.items()))


    def read_secret_key(self, secret, key):
        tuples = list(filter(lambda it: it[0] == key, self.read_secret(secret)))
        if len(tuples) == 0:
            print("Key" + key + " not found in secret" + secret)
        elif len(tuples) > 1:
            print("Secret " + secret + " has multiple keys for " + key)
        else:
            return tuples[0][1]


    def split_secrets(self):
        items = map(lambda it: it.split(), test.splitlines())
        filtered = filter(lambda it: len(it) == 4 and it[0] != "NAME", items)
        secrets = list(map(lambda it: it[0], filtered))

        return secrets