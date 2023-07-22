bl_info = {
        'name'			: 'Scooby Doo Mystery Mayhem Panimation',
	'author'		: 'Calum Underwood',
	'version'		: (0, 0, 1),
	'blender'		: (3, 0, 0),
	'location'		: 'File > Import',
	'description'           : 'Import Panim Animation',
	'category'		: 'Scooby-Doo Mystery Mayhem pAnim',
}
import os
import bpy
import importlib
from bpy.props import CollectionProperty, StringProperty, BoolProperty, EnumProperty, FloatProperty, IntProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper

from.import panim_load, panim_save

class ImportPanim(bpy.types.Operator, ImportHelper):
        bl_idname  = 'import_mystery_mayhem.panim'
        bl_label   = 'Mystery Mayhem pAnim'
        bl_options = {'UNDO'}
        filename_ext = '.pAnim'
        files: CollectionProperty(
                name	    = 'File path',
                description = 'File path used for finding the pAnim file',
                type	    = bpy.types.OperatorFileListElement
        )
        directory: StringProperty()
        filter_glob: StringProperty(default = '*.pAnim', options = {'HIDDEN'})
        
        def execute(self, context):
                paths = [os.path.join(self.directory, name.name) for name in self.files]
                if not paths: paths.append(self.filepath)
                importlib.reload(panim_load)
                for path in paths: panim_load.panim_reading(path)
                return {'FINISHED'}

class ExportPanim(bpy.types.Operator, ExportHelper):
        bl_idname  = 'export_mystery_mayhem.panim'
        bl_label   = 'Mystery Mayhem pAnim'
        bl_options = {'UNDO'}
        filename_ext = '.pAnim'
        files: CollectionProperty(
                name	    = 'File path',
                description = 'File path used for finding the pAnim file',
                type	    = bpy.types.OperatorFileListElement
        )

        directory: StringProperty()
        filter_glob: StringProperty(default = '*.pAnim', options = {'HIDDEN'})

        def execute(self, context):
            importlib.reload(panim_save)
            panim_save.panim_writing(self.filepath)
            return {"FINISHED"}

        
        

        
	
def menu_func_import(self, context):
        self.layout.operator(ImportPanim.bl_idname, text='Scooby Doo Mystery Mayhem (.pAnim)')

def menu_func_export(self, context):
        self.layout.operator(ExportPanim.bl_idname, text='Scooby Doo Mystery Mayhem (.pAnim)')
def register():
        bpy.utils.register_class(ImportPanim)
        bpy.utils.register_class(ExportPanim)
        bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
        bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
def unregister():
        bpy.utils.unregister_class(ImportPanim)
        bpy.utils.unregister_class(ExportPanim)
        bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
        bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
if __name__ == '__main__': register()
