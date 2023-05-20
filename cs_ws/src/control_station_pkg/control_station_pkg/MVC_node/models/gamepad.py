import numpy as np

class Gamepad:

    class Profile:
        def __init__(self, name, buttons_mapping, axes_mapping):
            self.name = name
            self.buttons_mapping = buttons_mapping
            self.axes_mapping    = axes_mapping

    def __init__(self):

        self.nav_profiles = []
        self.hd_profiles  = []
        self.selected_nav_profile = None
        self.selected_hd_profile  = None

        default_nav = self.Profile("Default", [], [])
        self.nav_profiles.append(default_nav)
        default_hd  = self.Profile("Default", [], [])
        self.hd_profiles.append(default_hd)


    def get_nav_profile(self):
        return self.nav_profiles
    
    def get_hd_profile(self):
        return self.hd_profiles
    
    def set_nav_profile(self, profile):
        self.selected_nav_profile = profile
    
    def set_hd_profile(self, profile):
        self.selected_hd_profile = profile
    

    def hd_maping(self, axes, buttons):
        new_buttons = buttons.copy()
        new_axes    = axes.copy()

        for i in range(len(self.selected_hd_profile.axes)):
            new_axes[i] = axes[self.selected_hd_profile.axes[i]]

        for i in range(len(self.selected_hd_profile.buttons)):
            new_buttons[i] = buttons[self.selected_hd_profile.buttons[i]]

        return new_axes, new_buttons

    

        
