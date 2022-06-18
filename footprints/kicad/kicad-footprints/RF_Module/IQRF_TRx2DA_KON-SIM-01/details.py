###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "IQRF_TRx2DA_KON-SIM-01")

newPart.addTag("kicadDesc", "8 pin SIM connector for IQRF TR-x2DA(T) modules, http://iqrf.org/weben/downloads.php?id=104")
newPart.addTag("kicadTags", "IQRF_KON-SIM-01 IQRF_TRx2DA")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/IQRF_TRx2DA_KON-SIM-01.wrl")

OOMP.parts.append(newPart)