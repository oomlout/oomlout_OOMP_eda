###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector")
newPart.addTag("oompIndex", "FanPinHeader_1x04_P2.54mm_Vertical")
newPart.addTag("oompName", "kicad-footprints/Connector/FanPinHeader_1x04_P2.54mm_Vertical")

newPart.addTag("kicadDesc", "4-pin CPU fan Through hole pin header, e.g. for Wieson part number 2366C888-007 Molex 47053-1000, Foxconn HF27040-M1, Tyco 1470947-1 or equivalent, see http://www.formfactors.org/developer%5Cspecs%5Crev1_2_public.pdf")
newPart.addTag("kicadTags", "pin header 4-pin CPU fan")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector.3dshapes/FanPinHeader_1x04_P2.54mm_Vertical.wrl")

OOMP.parts.append(newPart)