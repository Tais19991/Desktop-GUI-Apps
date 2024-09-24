# ------------------------------------------------------------------------------
# File: text_extract.py
# Class: TextExtract
# Description: This class handles the extraction of text from images using pytesseract.
#
# Copyright (c) 2024 Tatiana Kasatkina
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

import pytesseract

# -----------------------------------------------------------------------------------------------------
PATH_TO_PYTESSERACT = r'C:\Program Files\Tesseract-OCR\tesseract'
# -----------------------------------------------------------------------------------------------------


class TextExtract:
    """Turn image to text using pytesseract"""

    def __init__(self):
        self.language = ''
        pytesseract.pytesseract.tesseract_cmd = PATH_TO_PYTESSERACT
        self.text = ''

    def image_to_text(self, image_path: str, language: str) -> str:
        """Turn img into text using pytesseract"""
        self.text = pytesseract.image_to_string(image_path, language, timeout=10)
        return self.text
