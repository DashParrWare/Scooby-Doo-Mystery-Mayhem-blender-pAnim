from struct import pack
import bpy

def panim_write(f):
    #global FileSize
    ob = bpy.context.object
    f.write(pack(">I", 13))
    f.write(pack(">I", 4096))
    f.write(pack(">f", bpy.context.scene.frame_end/30.0))
    f.write(pack("B", len(ob.pose.bones)))

def panim_writing(filepath):
    with open(filepath, "wb") as f:
        panim_write(f)
