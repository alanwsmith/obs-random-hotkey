# OBS Random Hotkey

GOAL: Make a hotkey that moves around randomly in obs

## Status

I can't figure out how to do this. Whenever
I remove a hotkey I can't add a new one. 
I've put 10hrs into it and I'm calling it. 

I found this note:

---

Nearly all of wrapper functions are generated 
automatically by SWIG during OBS build, based 
on the API functions definition in C. For a 
few complex C functions and structures, for 
which SWIG would not generate proper code 
automatically, wrapper functions are written 
manually. This is the case for frontend-related 
functions, source_info and functions with 
callback arguments (see the section other 
differences from the C API).

Even if most functions are usable as intended 
(especially the ones specifically re-designed 
for scripting), a few functions with SWIG-written 
wrappers cannot be used directly for scripting 
so far, because SWIG cannot interpret properly 
the data types of arguments or return values 
given in the C definition. Typically, with 
values passed by reference or buffers, C 
pointers and pointer-pointer types are inherently 
ambiguous.

---

-- [Source](https://obsproject.com/kb/scripting-guide)

That may be related to what I'm seeing. 

Next step (if I decide to get back into it) is to check
the Rust create to see if it's possible that way. 

