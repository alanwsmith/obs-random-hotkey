import obspython as obs
import json

# ID = "htk_id"
# JSON_DATA = '{"%s":[{"key":"OBS_KEY_G"}]}' % ID

def caught_key(pressed):
    global counter
    if pressed:
        print("pressed")
        print(counter)
        counter += 1

def set_key(letter):
    id = "htk_id"
    prep = {}
    prep[id] = [{"key": f"OBS_KEY_{letter}"}]
    ready = json.dumps(prep)
    print(ready)
    _data = obs.obs_data_create_from_json(ready)
    _array = obs.obs_data_get_array(_data, id)
    _hotkey = obs.obs_hotkey_register_frontend(id, id, caught_key)
    obs.obs_hotkey_load(_hotkey, _array)
    obs.obs_data_array_release(_array)
    obs.obs_data_release(_data)



#     ID = "htk_id"
#     JSON_DATA = f'''{"{ID}":[{"key":"OBS_KEY_{letter}"}]}'''

#     _data = obs.obs_data_create_from_json(JSON_DATA)
#     _array = obs.obs_data_get_array(_data, ID)
#     _hotkey = obs.obs_hotkey_register_frontend(ID, ID, caught_key)
#     obs.obs_hotkey_load(_hotkey, _array)
#     obs.obs_data_array_release(_array)
#     obs.obs_data_release(_data)

def script_load(settings):
    print("on")
    global counter
    counter = 0
    set_key("C")


    # _data = obs.obs_data_create_from_json(JSON_DATA)
    # _array = obs.obs_data_get_array(_data, ID)
    # _hotkey = obs.obs_hotkey_register_frontend(ID, ID, caught_key)
    # obs.obs_hotkey_load(_hotkey, _array)
    # obs.obs_data_array_release(_array)
    # obs.obs_data_release(_data)

