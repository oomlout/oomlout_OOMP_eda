###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Audio_Module")
newPart.addTag("oompIndex", "Reverb_BTDR-1V")

newPart.addTag("kicadDesc", "Digital Reverberation Unit, http://www.belton.co.kr/inc/downfile.php?seq=17&file=pdf (footprint from http://www.uk-electronic.de/PDF/BTDR-1.pdf)")
newPart.addTag("kicadTags", "audio belton reverb")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Audio_Module.3dshapes/Reverb_BTDR-1V.wrl")

OOMP.parts.append(newPart)