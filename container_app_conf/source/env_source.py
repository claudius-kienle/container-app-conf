#  Copyright (c) 2019 Markus Ressel
#  .
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#  .
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#  .
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import os
import re
from typing import List

from container_app_conf import ConfigEntry
from container_app_conf.const import ENV_REGEX
from container_app_conf.source import DataSource


class EnvSource(DataSource):
    """
    Data source utilizing environment variables
    """

    def __init__(self, entries: List[ConfigEntry]):
        # TODO: env keys should be implicit and never contain invalid characters
        for entry in entries:
            env_key = self.env_key(entry)
            if not re.match(ENV_REGEX, env_key):
                raise ValueError("Config entry contains invalid characters, restrict yourself to: {}".format(ENV_REGEX))

    def has(self, entry: ConfigEntry) -> bool:
        return self.env_key(entry) in os.environ.keys()

    def get(self, entry: ConfigEntry) -> any:
        return os.environ.get(entry.env_key, None)

    @staticmethod
    def env_key(entry: ConfigEntry) -> str:
        return "_".join(entry.yaml_path).upper()
