from struct import unpack, pack
import bpy
import os

def panim_read(f, filepath):
    #global FileSize
    FileSize = unpack(">I", f.read(4))[0]
    Magic = unpack(">I", f.read(4))[0]
    FrameRate = unpack(">f", f.read(4))[0] # multiply by 30 example 0.3333 is 1
    BoneCount = unpack("B", f.read(1))[0]
    bpy.context.scene.frame_end = int(FrameRate * 30)
    type1 = unpack("B", f.read(1))[0]
    if type1 == 0:
        type2 = unpack("B", f.read(1))[0]
        if type2 == 0:
            type3 = unpack("B", f.read(1))[0]
            if type3 == 0:
                for i in range(FileSize//58): # only mummy gets completed there needs to be a workaround to this???
                    
                    Magic2 = unpack(">H", f.read(2))[0]
                    if Magic2 == 0:
                        bone_id = unpack(">H", f.read(2))[0]
                        KeyframeType = unpack(">H", f.read(2))[0]
                        size = unpack(">H", f.read(2))[0]
                    elif Magic2 == 4096:
                        bone_id = unpack(">H", f.read(2))[0]
                        KeyframeType = unpack(">H", f.read(2))[0]
                        size = unpack(">H", f.read(2))[0]
            if type3 == 1:
                for i in range(FileSize//58): # only mummy gets completed there needs to be a workaround to this???
                    
                    Magic2 = unpack(">H", f.read(2))[0]
                    if Magic2 == 0:
                        bone_id = unpack(">H", f.read(2))[0]
                        KeyframeType = unpack(">H", f.read(2))[0]
                        size = unpack(">H", f.read(2))[0]
                        print(f.tell())
                    elif Magic2 == 4096:
                        bone_id = unpack(">H", f.read(2))[0]
                        KeyframeType = unpack(">H", f.read(2))[0]
                        size = unpack(">H", f.read(2))[0]
                        print(f.tell()) # nope not matching for some reason
                        

def panim_reading(filepath):
    with open(filepath, "rb") as f:
        panim_read(f, filepath)
