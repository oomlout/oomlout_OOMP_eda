###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "IQRF_TRx2D_KON-SIM-01")

newPart.addTag("kicadDesc", "8 pin SIM connector for IQRF TR-x2D(C)(T) modules, http://iqrf.org/weben/downloads.php?id=104")
newPart.addTag("kicadTags", "IQRF_KON-SIM-01 IQRF_TRx2D IQRF_TRx2DC")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/IQRF_TRx2D_KON-SIM-01.wrl")

OOMP.parts.append(newPart)