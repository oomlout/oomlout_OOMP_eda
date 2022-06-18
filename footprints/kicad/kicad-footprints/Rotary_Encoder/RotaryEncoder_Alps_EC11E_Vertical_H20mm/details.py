###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Rotary_Encoder")
newPart.addTag("oompIndex", "RotaryEncoder_Alps_EC11E_Vertical_H20mm")

newPart.addTag("kicadDesc", "Alps rotary encoder, EC12E... without switch (pins are dummy), vertical shaft, http://www.alps.com/prod/info/E/HTML/Encoder/Incremental/EC11/EC11E15204A3.html")
newPart.addTag("kicadTags", "rotary encoder")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Rotary_Encoder.3dshapes/RotaryEncoder_Alps_EC11E_Vertical_H20mm.wrl")

OOMP.parts.append(newPart)