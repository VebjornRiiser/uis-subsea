import time
import threading

class Stopwatch:
    def __init__(self, func) -> None:
        self.start_time: float = -1
        self.time_passed = 0
        self.is_running = False
        self.laptime: list[int] = []
        self.function_to_run: function = func
        if func is None:
            self.function_to_run = self.print_time_to_console
        self.print_time_to_console()

    def start(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
            a = threading.Thread(target=self.time_updater, daemon=True)
            a.start()
        while True:
            cmd = input()

            if cmd == "stop":
                self.stop()
            elif cmd == "reset":
                self.reset()
            elif cmd == "start":
                self.start()
        
    def print_time_to_console(self):
        print(f"\rtime passed: {self.time_passed}", end="                                               ")
        pass

    def stop(self):
        self.is_running = False


    def reset(self):
        self.is_running = False
        self.time_passed = 0
        self.print_time_to_console()



    def time_updater(self):
        try:
            while self.is_running:
                self.time_passed = time.time() - self.start_time
                self.function_to_run()
                time.sleep(0.2)
            self.time_passed = time.time() - self.start_time
        except KeyboardInterrupt:
            exit(0)



if __name__ == "__main__":
    stpwtch = Stopwatch(None)
    stpwtch.start()
    while True:
        time.sleep(1)
    