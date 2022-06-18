###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SOIC-16_3.9x9.9mm_P1.27mm")

newPart.addTag("kicadDesc", "SOIC, 16 Pin (JEDEC MS-012AC, https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/soic_narrow-r/r_16.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "SOIC SO")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-16_3.9x9.9mm_P1.27mm.wrl")

OOMP.parts.append(newPart)