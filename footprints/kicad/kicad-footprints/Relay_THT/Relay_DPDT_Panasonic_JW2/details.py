###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Relay_THT")
newPart.addTag("oompIndex", "Relay_DPDT_Panasonic_JW2")

newPart.addTag("kicadDesc", "Panasonic Relay DPDT, http://www3.panasonic.biz/ac/e_download/control/relay/power/catalog/mech_eng_jw.pdf?via=ok")
newPart.addTag("kicadTags", "Panasonic Relay DPDT")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPDT_Panasonic_JW2.wrl")

OOMP.parts.append(newPart)