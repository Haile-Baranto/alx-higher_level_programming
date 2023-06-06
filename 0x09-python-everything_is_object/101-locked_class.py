class LockedClass:
    __slots__ = ("first_name",)
    
    def __init__(self):
        self.first_name = None
    
    def __setattr__(self, name, value):
        if not hasattr(self, "first_name") and name != "first_name":
            raise AttributeError(f"{name} cannot be set on LockedClass")
        super().__setattr__(name, value)
