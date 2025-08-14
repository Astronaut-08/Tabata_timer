'''This is backend of Tabata timer, here we write all operations with table "presets"
and main User GIU write on the Tkinter library'''
import time
import threading

class Timer:
    '''This is timer, we gonna use him tabata timer label'''
    def __init__(self, second, callback):
        self.second = second
        self._callback = callback
        self.interval = 1
        self._thread = None
        self._stop = threading.Event()

    def start(self):
        '''Starting the timer'''
        if self.is_runnig():
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def stop(self):
        '''stoping the timer'''
        self._stop.set()

    def is_runnig(self):
        '''Check timer on work'''
        return self._thread is not None and self._thread.is_alive()

    def _run(self):
        '''working login of the timer'''
        remaining = self.second
        while remaining >= 0 and not self._stop.is_set():
            self._callback(remaining)
            time.sleep(self.interval)
            remaining -=1
