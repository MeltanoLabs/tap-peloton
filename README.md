# tap-peloton

`tap-peloton` is a Singer tap for Peloton data.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

This tap will sync workouts and metrics for those workouts. 
This uses the [Pylotoncycle library](https://github.com/justmedude/pylotoncycle/).

## Installation

```bash
pipx install tap-peloton
```

## Configuration

### Capabilities

* `sync`
* `catalog`
* `state`
* `discover`

### Settings

| Setting               | Required | Default | Description |
|:----------------------|:--------:|:-------:|:------------|
| username              | True     | None    | Your Peloton Username. |
| password              | True     | None    | Your Peloton Password. |
| recent_workouts_number| False    | 5       | The number of workouts to fetch. |

A full list of supported settings and capabilities is available by running: 

```bash
tap-peloton --about
```

### Source Authentication and Authorization

You must have a Peloton account to use this tap.

## Usage

You can easily run `tap-peloton` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-peloton --version
tap-peloton --help
tap-peloton --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_peloton/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-peloton` CLI interface directly using `poetry run`:

```bash
poetry run tap-peloton --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-peloton
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-peloton --version
# OR run a test `elt` pipeline:
meltano elt tap-peloton target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
