import pygame


class Input:
    def __init__(self):
        # Has the user quit the application?
        self._quit = False
        # lists to store key states
        # down, up: discrete event; lasts for one iteration
        # pressed: continuous event, between down and up events
        self._key_down_list = []
        self._key_pressed_list = []
        self._key_up_list = []
        # lists to store mouse states
        # down, up: discrete event; lasts for one iteration
        # pressed: continuous event, between down and up events
        self._button_down_list = []
        self._button_pressed_list = []
        self._button_up_list = []
        # store lasts for one iteration boolean value
        self._mouse_moved = False
        # store lasts for all time mouse position
        # None if mouse wasn't moved for all time
        self._current_mouse_position = None

    @property
    def key_down_list(self):
        return self._key_down_list

    @property
    def key_pressed_list(self):
        return self._key_pressed_list

    @property
    def key_up_list(self):
        return self._key_up_list

    @property
    def button_down_list(self):
        return self._button_down_list

    @property
    def button_pressed(self):
        return self._button_pressed_list

    @property
    def button_up_list(self):
        return self._button_up_list

    @property
    def mouse_position(self):
        return self._current_mouse_position

    @property
    def quit(self):
        return self._quit

    # functions to check key states
    def is_key_down(self, key_code):
        return key_code in self._key_down_list

    def is_key_pressed(self, key_code):
        return key_code in self._key_pressed_list

    def is_key_up(self, key_code):
        return key_code in self._key_up_list

    # functions to check mouse buttons states
    def is_button_down(self, button_code):
        return button_code in self._button_down_list

    def is_button_pressed(self, button_code):
        return button_code in self._button_pressed_list

    def is_button_up(self, button_code):
        return button_code in self._button_up_list

    def is_mouse_moved(self):
        return self._mouse_moved

    def update(self):
        # Reset discrete key states
        self._key_down_list = []
        self._key_up_list = []
        # Reset discrete mouse states
        self._button_down_list = []
        self._button_up_list = []
        self._mouse_moved = False
        # Iterate over all user input events (such as keyboard or mouse)
        # that occurred since the last time events were checked
        for event in pygame.event.get():
            # Quit event occurs by clicking button to close window
            if event.type == pygame.QUIT:
                self._quit = True
            # Check for key-down and key-up events;
            # get name of key from event and append to or remove from corresponding lists
            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                self._key_down_list.append(key_name)
                self._key_pressed_list.append(key_name)
            if event.type == pygame.KEYUP:
                key_name = pygame.key.name(event.key)
                self._key_pressed_list.remove(key_name)
                self._key_up_list.append(key_name)
            # Check for button-down and button-up events;
            # get code of button from event and append to or remove from corresponding lists
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_code = event.button
                self._button_down_list.append(button_code)
                self._button_pressed_list.append(button_code)
            if event.type == pygame.MOUSEBUTTONUP:
                button_code = event.button
                self._button_pressed_list.remove(button_code)
                self._button_up_list.append(button_code)
            if event.type == pygame.MOUSEMOTION:
                self._mouse_moved = True
                self._current_mouse_position = pygame.mouse.get_pos()