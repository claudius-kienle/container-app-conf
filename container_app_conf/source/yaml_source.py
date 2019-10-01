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
import logging
import os

import yaml

from container_app_conf.source import FilesystemSource

LOGGER = logging.getLogger(__name__)


class YamlSource(FilesystemSource):
    """
    Data source utilizing YAML files
    """
    DEFAULT_FILE_EXTENSIONS = ['yaml', 'yml']

    def _load(self, file_path: str) -> dict:
        with open(file_path, 'r') as ymlfile:
            import yaml
            return yaml.load(ymlfile, Loader=yaml.FullLoader)

    def write_reference(self, reference: dict):
        """
        Writes a reference config file
        """
        text = yaml.dump(reference)

        folder = self.paths[0]
        file_name = "{}_reference.{}".format(self.file_names[0], self.file_extensions[0])
        file_path = os.path.join(self.paths[0], file_name)

        os.makedirs(folder, exist_ok=True)
        with open(file_path, "w") as file:
            file.write(text)
