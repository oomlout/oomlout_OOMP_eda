###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Module")
newPart.addTag("oompIndex", "Raspberry_Pi_Zero_Socketed_THT_FaceDown_MountingHoles")

newPart.addTag("kicadDesc", "Raspberry Pi Zero using through hole straight pin socket, 2x20, 2.54mm pitch, https://www.raspberrypi.org/documentation/hardware/raspberrypi/mechanical/rpi_MECH_Zero_1p2.pdf")
newPart.addTag("kicadTags", "raspberry pi zero through hole")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Module.3dshapes/Raspberry_Pi_Zero_Socketed_THT_FaceDown_MountingHoles.wrl")

OOMP.parts.append(newPart)