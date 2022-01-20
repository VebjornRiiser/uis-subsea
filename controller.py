import pygame, time, sys
DPAD = 1538
BUTTON_DOWN = 1539
BUTTON_UP = 1540
JOYSTICK = 1536


class Controller:
    def __init__(self, connection, joystick_deadzone=7) -> None:
        self.joystick_deadzone = joystick_deadzone # deadzone in percent
        self.connection = connection
        self.buttons = [0]*10
        self.joysticks = [0]*6
        self.dpad = [0]*2
        self.controller_stop_point = 1.000030518509476
        self.first_run = True
        self.button_names = {0: "A", 1: "B", 2: "X", 3: "Y", 4: "Left button back", 5: "Right button back", 6: "Back", 7: "Start", 8: "Thumb button left", 9: "Thumb button right"}
        self.canbus_id = {}
        pygame.init()
        self.clock = pygame.time.Clock()
        self.wait_for_controller()


    def reset_button(self, event) -> None:
        self.buttons[event.button] = 0 
        # self.buttons = [0]*10

    # wait_for_controller will attempt to connect to the controller until it can find it
    def wait_for_controller(self):
        while True:    
            try:
                print("Attempting to Connect to controller")
                if not self.first_run:
                    pygame.joystick.quit()
                pygame.joystick.init()
                global joystick
                if pygame.joystick.get_count() > 1:
                    print("Found several controllers. Connecting to controller 0 only")
                joystick = pygame.joystick.Joystick(0)
                print(f"Connected to {joystick.get_name()}")
                break
            except:
                self.first_run = False
                for sec in range(5,0,-1):
                        sys.stdout.write("\r" + f"Could not find controller. if it is already connected, try reconnecting it! retrying in {sec} seconds")
                        time.sleep(1)
                        sys.stdout.flush()
                print("")
        joystick.init()

    def normalize_joysticks(self, event):
        # (x-min)/(max-min)
        if event.axis == 4 or event.axis == 5:
            return round((event.value--self.controller_stop_point)/(self.controller_stop_point--self.controller_stop_point)*100)
        return round((2*(event.value--self.controller_stop_point)/(self.controller_stop_point--self.controller_stop_point)-1)*100)

    def write_controller_values(self):
        writestring = f"{self.buttons} - {self.joysticks} - {self.dpad}"
        return writestring
        
        # for i in range(len(self.joysticks)):
        #     writestring += f"axis {i} : {self.joysticks}%"
        # sys.stdout.write("\r" + f"{writestring}")
        # sys.stdout.flush()
        # sys.stdout.write("\r" + f"{self.buttons} - {self.joysticks}                     ")
        # sys.stdout.flush()


    def get_events_loop(self, debug=False, debug_all=False):
        while True:
            if pygame.joystick.get_count() < 1:
                self.wait_for_controller()
            can = {}
            duration = self.clock.tick(20)
            # print(duration)
            for event in pygame.event.get():
                if event.type == DPAD: #dpad (both up and down)
                    self.dpad = event.value

                if event.type == BUTTON_DOWN: #button down
                    self.buttons[event.button] = 1

                    if debug_all:
                        if event.button == 0:
                            print("A")
                            pygame.joystick.Joystick.rumble(1,1,1)

                        if event.button == 1:
                            print("B")
                        if event.button == 2:
                            print("X")
                        if event.button == 3:
                            print("Y")
                        if event.button == 4:
                            print("Left button")
                        if event.button == 5:
                            print("Right button")
                        if event.button == 6:
                            print("Back")
                        if event.button == 7:
                            print("Start")
                        if event.button == 8:
                            print("Thumb button left")
                        if event.button == 9:
                            print("Thumb button right")


                    # print(event.button)
                if event.type == BUTTON_UP: #button up
                    self.reset_button(event)
                    
                    if debug_all:
                        if event.button == 0:
                            pygame.joystick.Joystick.stop_rumble()
                            print("A up")
                        if event.button == 1:
                            print("B up")
                        if event.button == 2:
                            print("X up")
                        if event.button == 3:
                            print("Y up")
                        if event.button == 4:
                            print("Left button up")
                        if event.button == 5:
                            print("Right button up")
                        if event.button == 6:
                            print("Back up")
                        if event.button == 7:
                            print("Start up")
                        if event.button == 8:
                            print("Thumb button left up")
                        if event.button == 9:
                            print("Thumb button right up")
                    self.reset_button(event)

                elif event.type == JOYSTICK: #joystick movement
                    self.joysticks[event.axis] = self.normalize_joysticks(event)
                    
                    if debug_all:
                        if event.axis == 0:
                            if event.value > 0:
                                print(f"Roboten kjører mot høyre med {self.normalize_joysticks(event)}% kraft")
                            else:
                                print(f"Roboten kjører mot venstre med {self.normalize_joysticks(event)}% kraft")
                        elif event.axis == 1:
                            if event.value > 0:
                                print(f"Roboten kjører framover med {self.normalize_joysticks(event)}% kraft")
                            else:
                                print(f"Roboten kjører bakover med {self.normalize_joysticks(event)}% kraft")
                        elif event.axis == 2:
                            if event.value > 0:
                                print(f"Roboten roterer mot klokka med {self.normalize_joysticks(event)}% kraft")
                            else:
                                print(f"Roboten roterer med klokka med {self.normalize_joysticks(event)}% kraft")
                        elif event.axis == 3:
                            if event.value > 0:
                                print(f"Roboten tilter kamera med {self.normalize_joysticks(event)}% kraft")
                            else:
                                print(f"Roboten tilter kamera med {self.normalize_joysticks(event)}% kraft")
                        elif event.axis == 4:
                                print(f"Roboten går ned med {self.normalize_joysticks(event)}% kraft")
                        elif event.axis == 5:
                                print(f"Roboten går opp med {self.normalize_joysticks(event)}% kraft")
                if debug:
                    self.connection.send([self.buttons, self.dpad, self.joysticks])
                    # self.connection.close()


def run(connection, debug=True, debug_all=False):
    c = Controller(connection)
    c.get_events_loop(debug=debug, debug_all=debug_all)

if __name__ == "__main__":
    c = Controller()
    c.get_events_loop(debug=True)