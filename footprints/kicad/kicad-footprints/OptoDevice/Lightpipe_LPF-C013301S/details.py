###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Lightpipe_LPF-C013301S")

newPart.addTag("kicadDesc", "https://www.lumex.com/spec/LPF-C013301S.pdf")
newPart.addTag("kicadTags", "lightpipe triple tower right angle 3mm")
newPart.addTag("kicadAttr", "exclude_from_pos_files")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Lightpipe_LPF-C013301S.wrl")

OOMP.parts.append(newPart)