###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "Hamamatsu_C12880")
newPart.addTag("oompName", "kicad-footprints/OptoDevice/Hamamatsu_C12880")

newPart.addTag("kicadDesc", "Hamamatsu spectrometer, see http://www.hamamatsu.com/resources/pdf/ssd/c12880ma_kacc1226e.pdf")
newPart.addTag("kicadTags", "opto spectrometer Hamamatsu")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Hamamatsu_C12880.wrl")

OOMP.parts.append(newPart)