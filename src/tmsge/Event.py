class Event:
    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data

    def __getattr__(self, key):
        try:
            return self.data[key]
        except KeyError:
            raise AttributeError(f"'Event' object has no attribute '{key}'")
