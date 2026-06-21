class EventTrigger:
    def __init__(self):        
        self.callbacks = {}

    def process_event(self, event):
        if event.type in self.callbacks:
            for cb in self.callbacks[event.type]:
                cb(event)
    
    def bind(self, event_type, callback):
        if not event_type in self.callbacks:
            self.callbacks[event_type] = []
        self.callbacks[event_type].append(callback)
    
    def unbind(self, event_type, callback):
        if event_type in self.callbacks:
            self.callbacks[event_type] = [cb for cb in self.callbacks[event_type] if cb != callback]
