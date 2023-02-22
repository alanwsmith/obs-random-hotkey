import obspython as obs
import json


class TrackGroup:
    def __init__(self):
        print("HER")
        self.hotkey_saved_key = None
        self.key1 = "key1"
        self.callback = None
        self.keyName = "RandomKeyer2"
        self.letter = "A"

    def update_source(self):
	    self.__deregister_hotkey()  # source has changed! remove the existing hotkey...
	    self.__unsave_hotkey()      # remove the saved reference to its name/value
	    self.__register_hotkey()    # and re-register it under a new name

    def __deregister_hotkey(self):
	    if self.callback is not None:
		    obs.obs_hotkey_unregister(self.callback)

    def __register_hotkey(self):
        key_description = self.keyName
        self.callback = lambda pressed: self.__key_passthrough(pressed)  # small hack to get around the callback signature reqs.
        self.hotkey_id = obs.obs_hotkey_register_frontend(self.key1, self.key1, self.callback)
        # obs.obs_hotkey_load(self.hotkey_id, self.hotkey_saved_key)  # register new hotkey with GUI
        prep = {}
        prep[self.key1] = [{"key": f"OBS_KEY_{self.letter}"} ]
        input = json.dumps(prep)
        print(input)
        # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self.callback)
        dataStuff = obs.obs_data_create_from_json(input)
        arrayStuff = obs.obs_data_get_array(dataStuff, self.key1)
        obs.obs_hotkey_load(self.hotkey_id, arrayStuff)  # register new hotkey with GUI
        # obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
        obs.obs_data_array_release(arrayStuff)


    def __unsave_hotkey(self):
	    # clear the assigned key from the script's data array (when changing )
	    obs.obs_data_erase(TrackGroup.obs_data, self.key1)

    def __key_passthrough(self, pressed):
        if pressed:
            print("got it")



def script_load(settings):
    TrackGroup.obs_data = settings
    x = TrackGroup()
    x.update_source()




# class KeyMover():
#     def __init__(self):
#         self.counter = 1
#         print("Loading mover...")
#         self.register_key("A")
#         # self.register_key("D")

    # def register_key(self, letter):
    #     self.callback = lambda pressed: self.process(pressed)
    #     id = f"RANDOM LETTER"
    #     prep = {}
    #     prep[id] = [{"key": f"OBS_KEY_{letter}"} ]
    #     input = json.dumps(prep)
    #     print(input)
    #     hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self.callback)

        # dataStuff = obs.obs_data_create_from_json(input)
        # arrayStuff = obs.obs_data_get_array(dataStuff, id)
        # obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
        # # obs.obs_data_array_release(arrayStuff)
        # # obs.obs_data_release(dataStuff)


#     obs.obs_data_array_release(arrayStuff)
#     obs.obs_data_release(dataStuff)
#     # _hotkey = obs.obs_hotkey_register_frontend(id, id, lambda pressed : caught_keypress(pressed))

    # def process(self, pressed):
    #     if pressed:
    #         print("hit process")
    #         self.counter += 1
    #         if self.counter == 4:
    #             self.counter = 0
    #             if self.callback is not None:
    #                 print("clearing")
    #                 obs.obs_hotkey_unregister(self.callback)
    #                 self.register_key("D")

            # print(self.counter)



# def script_load(settings):
#     print("Script loading...")
#     km = KeyMover()

    # global counter
    # counter = 0
    # global config
    # config = settings
    # # global current_letter
    # # current_letter = "D"
    # set_key("G")




#def caught_keypress(pressed):
#    print(pressed)
#    global counter
#    global config 
#    print(counter)
#    if counter == 2:
#        #obs.obs_hotkey_unregister(caught_keypress)
#        # obs.remove_current_callback()
#        set_key("D")
#        obs.obs_data_erase(config, "RANDOM LETTER")
#    counter += 1
    

# def set_key(current_letter):
#     id = f"RANDOM LETTER"
#     prep = {}
#     prep[id] = [{"key": f"OBS_KEY_{current_letter}"} ]
#     input = json.dumps(prep)
#     print(input)
#     dataStuff = obs.obs_data_create_from_json(input)
#     arrayStuff = obs.obs_data_get_array(dataStuff, id)
#     hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, caught_keypress)
#     obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
#     obs.obs_data_array_release(arrayStuff)
#     obs.obs_data_release(dataStuff)
#     # _hotkey = obs.obs_hotkey_register_frontend(id, id, lambda pressed : caught_keypress(pressed))


# def script_load(settings):
#     print("Script loading...")
#     global counter
#     counter = 0
#     global config
#     config = settings
#     # global current_letter
#     # current_letter = "D"
#     set_key("G")


#def caught_click(props, prop):
#    obs.blog(300,"Got a click")
#    set_key()
#    #set_key2()


# def caught_keypress(pressed):
#     set_key2()
#     print('asdf')
#     global counter
#     global current_letter 
#     if pressed:
#         print("pressed")
#         print(counter)
#         counter += 1
#         if counter == 8:
#             if current_letter == "A":
#                 current_letter = "D"
#             else:
#                 current_letter = "A"
#             counter = 0
#             obs.remove_current_callback()
#             print("HHHHH")
#             set_key2()

# def caught_keypress2(pressed):
#     print('asdf')
#     global counter
#     global current_letter 
#     if pressed:
#         print("pressed")
#         print(counter)
#         counter += 1
#         if counter == 8:
#             if current_letter == "A":
#                 current_letter = "D"
#             else:
#                 current_letter = "A"
#             counter = 0
#             obs.remove_current_callback()
#             print("HHHHH")
#             set_key2()

# def set_key():
#     # obs.obs_hotkey_unregister(caught_keypress)
#     global current_letter
#     id = f"Random Letter Trigger {current_letter}"
#     prep = {}
#     prep[id] = [{"key": f"OBS_KEY_{current_letter}"}]
#     ready = json.dumps(prep)
#     print(ready)
#     _data = obs.obs_data_create_from_json(ready)
#     _array = obs.obs_data_get_array(_data, id)
#     # _hotkey = obs.obs_hotkey_register_frontend(id, id, caught_keypress)
#     _hotkey = obs.obs_hotkey_register_frontend(id, id, lambda pressed : caught_keypress(pressed))
#     obs.obs_hotkey_load(_hotkey, _array)
#     obs.obs_data_array_release(_array)
#     obs.obs_data_release(_data)
    

#def set_key2():
#    print("set_key2()")
#    # obs.obs_hotkey_unregister(caught_keypress)
#    #global current_letter
#    id = f"Random Letter Trigger B"
#    prep = {}
#    prep[id] = [{"key": f"OBS_KEY_B"}]
#    ready = json.dumps(prep)
#    print(ready)
#    _data = obs.obs_data_create_from_json(ready)
#    _array = obs.obs_data_get_array(_data, id)
#    _hotkey = obs.obs_hotkey_register_frontend(id, id, caught_keypress2)
#    obs.obs_hotkey_load(_hotkey, _array)
#    obs.obs_data_array_release(_array)
#    obs.obs_data_release(_data)
#    print("bravo")



