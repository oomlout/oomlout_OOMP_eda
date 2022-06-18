###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_RF1156")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_RF1156")

newPart.addTag("kicadDesc", "Zynq-7000 BGA, 34x34 grid, 35x35mm package, 1mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug865-Zynq-7000-Pkg-Pinout.pdf#page=95, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 1156 1 RF1156")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_RF1156.wrl")

OOMP.parts.append(newPart)