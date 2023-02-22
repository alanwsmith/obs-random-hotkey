import obspython as obs
import json
from datetime import datetime
from random import randint

class Maker:
    def mcb(pressed):
        obs.obs_hotkey_unregister(Maker.mcb)
        print("mcb")
        register_hotkey("D")

m = Maker()

hotkeyStuff = None
callback = None 

def make_method():
    def _method(pressed):
        if pressed:
            print("HERE")
            register_hotkey("B")
            # obs.remove_current_callback()
            obs.obs_hotkey_unregister(callback)
            print("REMOVED")
    return _method

__cb4 = None

def cb(pressed):
    print("HASDASD")
    obs.obs_hotkey_unregister(cb)

def __move_it(pressed):
    # obs.remove_current_callback()
    obs.obs_hotkey_unregister(__cb4)
    register_hotkey("D")
    print("MOVEING")

def register_hotkey(letter):
    print(f"Registering: {letter}")
    id = f"RANDOM_LETTER_{letter}"
    prep = {}
    prep[id] = [{"key": f"OBS_KEY_{letter}"} ]
    input = json.dumps(prep)
    print(input)
    # method_id = f"asdf_{letter}"
    # setattr(m, method_id, make_method())
    # callback = m.asdf_A
    dataStuff = obs.obs_data_create_from_json(input)
    arrayStuff = obs.obs_data_get_array(dataStuff, id)
    __cb4 = lambda pressed : __move_it(pressed)
    # tmp = m.mcb
    hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, lambda pressed : __cb4(pressed) )
    # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, lambda pressed : Maker.mbc )
    # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, Maker.mcb)
    # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, cb)
    # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, callback )
    # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, lambda pressed : getattr(m, method_id)(pressed) )
    # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, lambda pressed : m.a() )
    #hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, aasdf)

    obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
    # obs.obs_data_array_release(arrayStuff)
    # obs.obs_data_release(dataStuff)


    #setattr(method_id, self.make_method(method_id))
    #dataStuff = obs.obs_data_create_from_json(input)
    #arrayStuff = obs.obs_data_get_array(dataStuff, id)

    # # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self.asdf)
    # # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, getattr(self, method_id))
    # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self['asdf_A'])
    # obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
    # obs.obs_data_array_release(arrayStuff)
    # obs.obs_data_release(dataStuff)


def script_load(settigs):
    register_hotkey("A")

# class Setter:
#     def __init__(self):
#         print("Making setter")
#         self.the_key = "A"
#         self.register_hotkey("A")

    # def make_method(self, name):
    #     def _method(self):
    #         print(f"Target: {self}")
    #     return _method


        # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self.callback)
        # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, lambda pressed : self.make_function(pressed))

        # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, lambda pressed : t.pinger(pressed))
        # obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
        # obs.obs_data_array_release(arrayStuff)
        # obs.obs_data_release(dataStuff)
        # # _hotkey = obs.obs_hotkey_register_frontend(id, id, lambda pressed : caught_keypress(pressed))



# def script_load(settigs):
#     s = Setter()



# class Thinger:
#     def __init__(self):
#         print("starting thinger")
#     def pinger(self, obj, pressed):
#         print("hit")


# class Ringer:
#     def __init__(self):
#         print("Starting Ringer")
#         # self.letter = "A"
#         # self.key_id = "randomthing"
#         # self.register_hotkey()
#         # self.register_hotkey3()

    # def set_key(self, the_key):
    #     if the_key == "A":




    # def make_function(self, pressed):
    #     def prototype(*args):
    #         print("In named funcion")
    #         print(args[0])
    #         # obs.obs_hotkey_unregister(self.callback)
    #         # self.register_hotkey2()
    #     date_string = int(datetime.now().timestamp())
    #     random_num = randint(1,10000)
    #     the_name = f"name_{date_string}_{random_num}"
    #     print(the_name)
    #     prototype.__name__ = the_name
    #     # obs.remove_current_callback()
    #     # self.register_hotkey3()
    #     self.register_hotkey3()
    #     return prototype

    # def json_text(self):
    #     tmp = {}
    #     tmp[self.key] = [ {"key": f"OBS_KEY_{self.letter}"} ] 
    #     return json.dumps(tmp)

    # def forwarder(self, pressed):
    #     print(pressed)




    # def register_hotkey(self):
    #     t = Thinger()
    #     # t.timestamp = datetime
    #     # self.callback = lambda pressed : t.pinger(pressed)
    #     # self.callback = lambda pressed : self.caught_keypress(pressed)
    #     # self.callback = lambda pressed : self.make_function(pressed)
    #     current_letter = "A"
    #     id = f"RANDOM_LETTER_A"
    #     prep = {}
    #     prep[id] = [{"key": f"OBS_KEY_{current_letter}"} ]
    #     input = json.dumps(prep)
    #     print(input)
    #     dataStuff = obs.obs_data_create_from_json(input)
    #     arrayStuff = obs.obs_data_get_array(dataStuff, id)
    #     # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self.callback)
    #     # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, lambda pressed : self.make_function(pressed))
    #     hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, lambda pressed : t.pinger(pressed))
    #     obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
    #     obs.obs_data_array_release(arrayStuff)
    #     obs.obs_data_release(dataStuff)
    #     # _hotkey = obs.obs_hotkey_register_frontend(id, id, lambda pressed : caught_keypress(pressed))

    #def register_hotkey3(self):
    #    #t = Thinger()
    #    #t.timestamp = datetime
    #    # self.callback = lambda pressed : t.pinger(pressed)
    #    #self.callback = lambda pressed : self.caught_keypress(pressed)
    #    self.callback = lambda pressed : self.make_function3(pressed)
    #    current_letter = "D"
    #    id = f"RANDOM_LETTER_D"
    #    prep = {}
    #    prep[id] = [{"key": f"OBS_KEY_{current_letter}"} ]
    #    input = json.dumps(prep)
    #    print(input)
    #    dataStuff = obs.obs_data_create_from_json(input)
    #    arrayStuff = obs.obs_data_get_array(dataStuff, id)
    #    # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self.callback)
    #    hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, lambda pressed : self.make_function3(pressed))
    #    obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
    #    obs.obs_data_array_release(arrayStuff)
    #    obs.obs_data_release(dataStuff)
    #    # _hotkey = obs.obs_hotkey_register_frontend(id, id, lambda pressed : caught_keypress(pressed))


    #def register_hotkey2(self):
    #    #t = Thinger()
    #    #t.timestamp = datetime
    #    # self.callback = lambda pressed : t.pinger(pressed)
    #    #self.callback = lambda pressed : self.caught_keypress(pressed)
    #    self.callback = self.make_function()
    #    current_letter = "B"
    #    id = f"RANDOM_LETTERB"
    #    prep = {}
    #    prep[id] = [{"key": f"OBS_KEY_{current_letter}"} ]
    #    input = json.dumps(prep)
    #    print(input)
    #    dataStuff = obs.obs_data_create_from_json(input)
    #    arrayStuff = obs.obs_data_get_array(dataStuff, id)
    #    hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self.callback)
    #    obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
    #    obs.obs_data_array_release(arrayStuff)
    #    obs.obs_data_release(dataStuff)
    #    # _hotkey = obs.obs_hotkey_register_frontend(id, id, lambda pressed : caught_keypress(pressed))


    # def caught_keypress(self, pressed):
    #     print(pressed)
    #     obs.obs_hotkey_unregister(self.callback)
    #     self.register_hotkey()





        #print("Registering")
        ## self.holder = Thinger()
        ## self.callback = self.holder.pinger
        ## self.hotkey_id = obs.obs_hotkey_register_frontend(self.key, self.key, self.callback)
        #self.hotkey_id = obs.obs_hotkey_register_frontend(self.key, self.key, self.forwarder)
        #print(self.hotkey_id)
        ## print(self.json_text())
        #dataStuff = obs.obs_data_create_from_json(self.json_text())
        ##print(dataStuff)
        #arrayStuff = obs.obs_data_get_array(dataStuff, self.key)
        ## print(arrayStuff)
        #obs.obs_hotkey_load(self.hotkey_id, arrayStuff) 
        #print("Done registering")



        #self.callback = lambda pressed: self.__key_passthrough(pressed)  # small hack to get around the callback signature reqs.
        # self.callback = newThing.ping
        # obs.obs_hotkey_load(self.hotkey_id, self.hotkey_saved_key)  # register new hotkey with GUI
    #     prep = {}
    #     prep[self.key1] = [{"key": f"OBS_KEY_{self.letter}"} ]
    #     input = json.dumps(prep)
    #     print(input)
    #     # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self.callback)
    #     # obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
    #     obs.obs_data_array_release(arrayStuff)





# class TrackGroup:
#     def __init__(self):
#         print("HER")
#         self.hotkey_saved_key = None
#         self.key1 = "key1"
#         self.callback = None
#         self.keyName = "RandomKeyer2"
#         self.letter = "A"


    # def update_source(self):
	    # self.__deregister_hotkey()  # source has changed! remove the existing hotkey...
	    # self.__unsave_hotkey()      # remove the saved reference to its name/value
	    # self.__register_hotkey()    # and re-register it under a new name

    # def __deregister_hotkey(self):
	    # if self.callback is not None:
		    # obs.obs_hotkey_unregister(self.callback)

    # def __register_hotkey(self):
    #     key_description = self.keyName
    #     self.callback = lambda pressed: self.__key_passthrough(pressed)  # small hack to get around the callback signature reqs.
    #     self.hotkey_id = obs.obs_hotkey_register_frontend(self.key1, self.key1, self.callback)
    #     # obs.obs_hotkey_load(self.hotkey_id, self.hotkey_saved_key)  # register new hotkey with GUI
    #     prep = {}
    #     prep[self.key1] = [{"key": f"OBS_KEY_{self.letter}"} ]
    #     input = json.dumps(prep)
    #     print(input)
    #     # hotkeyStuff = obs.obs_hotkey_register_frontend(id, id, self.callback)
    #     dataStuff = obs.obs_data_create_from_json(input)
    #     arrayStuff = obs.obs_data_get_array(dataStuff, self.key1)
    #     obs.obs_hotkey_load(self.hotkey_id, arrayStuff)  # register new hotkey with GUI
    #     # obs.obs_hotkey_load(hotkeyStuff, arrayStuff)
    #     obs.obs_data_array_release(arrayStuff)


    # def __unsave_hotkey(self):
	    # # clear the assigned key from the script's data array (when changing )
	    # obs.obs_data_erase(TrackGroup.obs_data, self.key1)

    # def __key_passthrough(self, pressed):
    #     if pressed:
    #         print("got it")
    #         self.letter ="B"
    #         self.update_source()




# def script_load(settings):
#     TrackGroup.obs_data = settings
#     x = TrackGroup()
#     x.update_source()




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



