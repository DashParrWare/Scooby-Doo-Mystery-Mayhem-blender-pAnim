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
    if BoneCount == 35:
        type1 = unpack("B", f.read(1))[0]
        if type1 == 0:
            type2 = unpack("B", f.read(1))[0]
            if type2 == 0:
                type3 = unpack("B", f.read(1))[0]
                if type3 == 0:
                    pass
                if type3 == 1:
                    Magic2 = unpack(">H", f.read(2))[0]
                    if Magic2 == 0:
                        keyframeType = unpack(">H", f.read(2))[0]
                        if keyframeType == 0:
                            pass
                        if keyframeType == 1:
                            pass
                        if keyframeType == 2:
                            pass
                        if keyframeType == 3:
                            pass
                        if keyframeType == 4:
                            pass
                        if keyframeType == 5:
                            pass
                        if keyframeType == 6:
                            pass
                        if keyframeType == 7:
                            pass
                        if keyframeType == 8:
                            pass
                        if keyframeType == 9:
                            pass
    if BoneCount == 38:
        pass
    if BoneCount == 43:
        pass
    if BoneCount == 45:
        pass
    if BoneCount == 46:
        pass
    if BoneCount == 47:
        pass
    if BoneCount == 55:
        pass
    if BoneCount == 56:
        pass
    if BoneCount == 57:
        pass

def panim_reading(filepath):
    with open(filepath, "rb") as f:
        panim_read(f, filepath)
