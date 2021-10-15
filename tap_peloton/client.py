"""REST client handling, including PelotonStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from memoization import cached

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import APIKeyAuthenticator

import pylotoncycle
from singer_sdk.streams.core import Stream
from singer_sdk.tap_base import Tap
from singer_sdk.typing import ArrayType


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class PelotonStream(Stream):
    """Peloton stream class."""
    def __init__(self, tap: Tap):
        super().__init__(tap)
        self.conn = pylotoncycle.PylotonCycle(self.config.get("username"), self.config.get("password"))
        self.recent_workouts_number = self.config.get("recent_workouts_number")

