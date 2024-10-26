"""Simple loading spinner thing."""

from threading import Thread
from typing import Callable
from time import sleep

class Loadable:
    """This is a class that the different Loading objects can use to track states."""
    
    def __init__(self, func: Callable, *args, **kwargs) -> None:
        self.completed = False
        self.error: Exception = None
        self.func = func 
        self.args = args
        self.kwargs = kwargs
        self.value = None
        
    def start(self):
        thread = Thread(target=self.threaded_run, daemon=True)
        thread.start()
        
    def threaded_run(self):
        try:
            self.value = self.func(*self.args, **self.kwargs)
        except Exception as e:
            self.error = e
        finally:
            self.completed = True

class LoadingSpinner:
    """Simple loading spinner thing."""

    def __init__(self):
        self.spinner = ['-', '\\', '|', '/']
        self.index = 0
        
    def start(self, message:str, obj: Loadable):
        obj.start()
        while not obj.completed and not obj.error:
            self.index = (self.index + 1) % len(self.spinner)
            print(f"\r{message} {self.spinner[self.index]}", end="")
            sleep(0.2)
        print(f"\r{message} Done!")
        if obj.error:
            raise obj.error
        
        return obj.value

class LoadingEllipse:
    """Simple loading ellipses (...)"""
    
    def __init__(self):
        self.count = 0
        
    def start(self, message:str, obj: Loadable):
        obj.start()
        
        print(message)
        print("Loading", end="")
        while not obj.completed and not obj.error:
            self.count += 1
            print(".", end="", flush=True)
            sleep(0.2)
            
        print(f"\n{message} Done!")
        
        if obj.error:
            raise obj.error
        
        return obj.value