###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_FFG1157_FFG1158")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_FFG1157_FFG1158")

newPart.addTag("kicadDesc", "Virtex-7 BGA, 34x34 grid, 35x35mm package, 1mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=299, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 1156 1 FF1157 FFG1157 FFV1157 FF1158 FFG1158 FFV1158")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_FFG1157_FFG1158.wrl")

OOMP.parts.append(newPart)