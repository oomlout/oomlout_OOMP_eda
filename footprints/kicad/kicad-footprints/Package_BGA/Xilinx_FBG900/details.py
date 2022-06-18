###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_FBG900")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_FBG900")

newPart.addTag("kicadDesc", "Kintex-7 BGA, 30x30 grid, 31x31mm package, 1mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=289, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 900 1 FB900 FBG900 FBV900")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_FBG900.wrl")

OOMP.parts.append(newPart)