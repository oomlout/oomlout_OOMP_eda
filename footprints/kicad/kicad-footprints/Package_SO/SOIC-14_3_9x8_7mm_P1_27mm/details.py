###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SOIC-14_3.9x8.7mm_P1.27mm")

newPart.addTag("kicadDesc", "SOIC, 14 Pin (JEDEC MS-012AB, https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/soic_narrow-r/r_14.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "SOIC SO")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-14_3.9x8.7mm_P1.27mm.wrl")

OOMP.parts.append(newPart)