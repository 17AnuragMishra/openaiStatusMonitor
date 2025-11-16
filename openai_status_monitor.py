import feedparser
import time
from datetime import datetime
from typing import Set


class StatusPageMonitor:
    def __init__(self, rss_url: str, poll_interval: int = 60):
        self.rss_url = rss_url
        self.poll_interval = poll_interval
        self.seen_ids: Set[str] = set()
    
    def check_for_updates(self):
        """Check RSS feed for new entries."""
        try:
            feed = feedparser.parse(self.rss_url)
            new_entries = []
            
            for entry in feed.entries:
                entry_id = entry.get('id') or entry.get('link', '')
                if entry_id and entry_id not in self.seen_ids:
                    self.seen_ids.add(entry_id)
                    new_entries.append({
                        'title': entry.get('title', ''),
                        'summary': entry.get('summary', ''),
                        'link': entry.get('link', ''),
                        'published': entry.get('published', '')
                    })
            
            return new_entries
        except Exception as e:
            print(f"Error: {e}")
            return []
    
    def print_update(self, entry):
        """Print update to console."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[{timestamp}] NEW UPDATE")
        print("=" * 60)
        print(f"Title: {entry['title']}")
        print(f"Status: {entry['summary'][:300]}")
        if entry['link']:
            print(f"Link: {entry['link']}")
        print("=" * 60)
    
    def run(self):
        """Start monitoring."""
        print("Initializing...")
        self.check_for_updates()  # Skip existing entries
        print(f"Monitoring {self.rss_url}")
        print(f"Checking every {self.poll_interval} seconds\n")
        
        try:
            while True:
                for entry in self.check_for_updates():
                    self.print_update(entry)
                time.sleep(self.poll_interval)
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    monitor = StatusPageMonitor("https://status.openai.com/history.rss", poll_interval=60)
    monitor.run()
