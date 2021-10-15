"""Peloton tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_peloton.streams import (
    PelotonStream,
    WorkoutMetricsStream,
    WorkoutsStream,
)

STREAM_TYPES = [
    WorkoutsStream,
    WorkoutMetricsStream,
]


class TapPeloton(Tap):
    """Peloton tap class."""

    name = "tap-peloton"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "username",
            th.StringType,
            required=True,
            description="Your Peloton Username.",
        ),
        th.Property(
            "password",
            th.StringType,
            required=True,
            description="Your Peloton Password.",
        ),
        th.Property(
            "recent_workouts_number",
            th.IntegerType,
            default=5,            
            description="The number of workouts to fetch.",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
