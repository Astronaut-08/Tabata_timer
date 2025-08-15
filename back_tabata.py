'''This is backend of Tabata timer, here we write all operations with table "presets"
and main User GIU write on the Tkinter library'''
import time
import threading

class Timer:
    '''This is timer, we gonna use him tabata timer label'''
    def __init__(self, second=None, callback=None):
        self.second = second
        self._callback = callback
        self.interval = 1
        self._thread = None
        self._stop = threading.Event()
        self._paused = threading.Event()
        self._paused.clear()

    def start(self):
        '''Starting the timer'''
        if self.is_runnig():
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def pause(self):
        '''Pausing the timer'''
        self._paused.set()

    def resume(self):
        '''Resuming the timer'''
        self._paused.clear()

    def stop(self):
        '''stoping the timer'''
        self._stop.set()
        self._paused.clear()

    def is_runnig(self):
        '''Check timer on work'''
        return self._thread is not None and self._thread.is_alive()

    def _run(self):
        '''working login of the timer'''
        remaining = self.second
        while remaining >= 0 and not self._stop.is_set():
            if self._paused.is_set():
                time.sleep(0.1)
                continue
            self._callback(remaining)
            time.sleep(self.interval)
            remaining -=1
