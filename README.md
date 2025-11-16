# OpenAI Status Page Monitor

A Python script that automatically tracks and logs service updates from the OpenAI Status Page using an event-based RSS feed monitoring approach.

## Features

- **Automatic Detection**: Monitors the OpenAI Status Page RSS feed for new incidents, outages, and degradation updates
- **Efficient Polling**: Uses change detection to only report new updates, avoiding duplicate notifications
- **Service Identification**: Automatically identifies affected OpenAI API products (Chat Completions, Embeddings, etc.)
- **Scalable Design**: Can be easily extended to monitor multiple status pages

## Installation

1. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the monitor script:

```bash
python openai_status_monitor.py
```

The script will:
1. Perform an initial scan to identify existing entries (these won't be reported)
2. Continuously monitor for new updates every 60 seconds
3. Print new incidents/updates to the console with:
   - Affected service(s)
   - Latest status message
   - Publication timestamp
   - Link to the status page entry

Press `Ctrl+C` to stop monitoring.

## How It Works

- Uses RSS feed monitoring (no API keys required)
- Tracks seen entry IDs to detect only new updates
- Polls every 60 seconds (configurable)
- Extracts affected services from update content
- Prints formatted updates to console

## Extending to Multiple Status Pages

To monitor multiple status pages, you can:

1. Create multiple `StatusPageMonitor` instances
2. Run them in separate threads or processes
3. Or modify the script to accept a list of RSS feed URLs

Example for multiple monitors:

```python
monitors = [
    StatusPageMonitor("https://status.openai.com/history.rss"),
    StatusPageMonitor("https://status.otherservice.com/history.rss"),
]
# Run in parallel using threading or multiprocessing
```

