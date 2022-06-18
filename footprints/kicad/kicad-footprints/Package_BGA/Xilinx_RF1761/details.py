###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_RF1761")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_RF1761")

newPart.addTag("kicadDesc", "Virtex-7 BGA, 42x42 grid, 42.5x42.5mm package, 1mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=306, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 1760 1 RF1761")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_RF1761.wrl")

OOMP.parts.append(newPart)