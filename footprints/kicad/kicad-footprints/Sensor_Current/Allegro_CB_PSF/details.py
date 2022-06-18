###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Sensor_Current")
newPart.addTag("oompIndex", "Allegro_CB_PSF")

newPart.addTag("kicadDesc", "Allegro MicroSystems, CB-PSF Package (http://www.allegromicro.com/en/Products/Current-Sensor-ICs/Fifty-To-Two-Hundred-Amp-Integrated-Conductor-Sensor-ICs/ACS758.aspx)")
newPart.addTag("kicadTags", "Allegro CB-PSF")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/Allegro_CB_PSF.wrl")

OOMP.parts.append(newPart)