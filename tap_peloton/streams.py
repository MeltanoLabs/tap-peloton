"""Stream type classes for tap-peloton."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_peloton.client import PelotonStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class WorkoutsStream(PelotonStream):
    """Define custom stream."""

    name = "workouts"
    # path = "/users"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "achievement_templates",
            th.ArrayType(th.StringType),
        ),
        th.Property(
            "created",
            th.NumberType,
        ),
        th.Property(
            "created_at",
            th.IntegerType,
        ),
        th.Property(
            "device_time_created_at",
            th.IntegerType,
        ),
        th.Property(
            "device_type",
            th.StringType,
        ),
        th.Property(
            "device_type_display_name",
            th.StringType,
        ),
        th.Property(
            "end_time",
            th.IntegerType,
        ),
        th.Property(
            "fitbit_id",
            th.BooleanType,
        ),
        th.Property(
            "fitness_discipline",
            th.StringType,
        ),
        # th.Property(
        #     "ftp_info",
        #     th.ObjectType(th.ArrayType(th.StringType)),
        # ),
        th.Property(
            "has_leaderboard_metrics",
            th.BooleanType,
        ),
        th.Property(
            "has_pedaling_metrics",
            th.BooleanType,
        ),
        th.Property(
            "id",
            th.StringType,
        ),
        th.Property(
            "instructor_name",
            th.StringType,
        ),
        th.Property(
            "is_total_work_personal_record",
            th.BooleanType,
        ),
        th.Property(
            "leaderboard_rank",
            th.IntegerType,
        ),
        th.Property(
            "metrics_type",
            th.StringType,
        ),
        th.Property(
            "name",
            th.StringType,
        ),
        # th.Property(
        #     "overall_summary",
        #     th.ObjectType,
        # ),
        th.Property(
            "peloton_id",
            th.StringType,
        ),
        th.Property(
            "platform",
            th.StringType,
        ),
        # th.Property(
        #     "ride",
        #     th.ObjectType(th.StringType),
        # ),
        th.Property(
            "start_time",
            th.DateTimeType,
        ),
        th.Property(
            "status",
            th.StringType,
        ),
        th.Property(
            "strava_id",
            th.BooleanType,
        ),
        th.Property(
            "timezone",
            th.StringType,
        ),
        th.Property(
            "title",
            th.StringType,
        ),
        th.Property(
            "total_leaderboard_users",
            th.IntegerType,
        ),
        th.Property(
            "total_work",
            th.NumberType,
        ),
        th.Property(
            "user_id",
            th.StringType,
        ),
        th.Property(
            "workout_type",
            th.StringType,
        ),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        return {
            "workout_id": record["id"]
        }

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects.
        """

        resp = self.conn.GetRecentWorkouts(self.recent_workouts_number)
        for row in resp:
            yield row




class WorkoutMetricsStream(PelotonStream):

    name = "workout_metrics"
    primary_keys = ["id"]
    replication_key = None
    parent_stream_type = WorkoutsStream
    schema = th.PropertiesList(
        th.Property(
            "duration",
            th.IntegerType,
        ),
        th.Property(
            "is_class_plan_shown",
            th.BooleanType
        ),
        th.Property(
            "segment_list",
            th.ArrayType(th.StringType)
        ),
        th.Property(
            "seconds_since_pedaling_start",
            th.ArrayType(th.IntegerType)
        ),
        th.Property(
            "average_summaries",
            th.ArrayType(th.StringType)
        ),
        th.Property(
            "summaries",
            th.ArrayType(th.StringType)
        ),
        th.Property(
            "has_apple_watch_metrics",
            th.BooleanType
        ),
        th.Property(
            "location_data",
            th.ArrayType(th.StringType)
        ),
        th.Property(
            "is_location_data_accurate",
            th.StringType
        ),
        # th.Property(
        #     "splits_data",
        #     th.ObjectType
        # ),
        # th.Property(
        #     "target_metrics_performance_data",
        #     th.ObjectType
        # ),
        th.Property(
            "effort_zones",
            th.StringType
        )
    ).to_dict()

    def get_records(self, context: Optional[dict]) -> Iterable[dict]:
        """Return a generator of row-type dictionary objects.

        The optional `context` argument is used to identify a specific slice of the
        stream if partitioning is required for the stream. Most implementations do not
        require partitioning and should ignore the `context` argument.
        """
        resp = self.conn.GetWorkoutMetricsById(context.get("workout_id"))
        updated_row = resp
        updated_row["id"] = context.get("workout_id")
        yield updated_row
