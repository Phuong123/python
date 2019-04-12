# coding=utf-8

from MontagePy.main import mViewer

imgjson = """
{
   "image_type":"png",
   "true_color":1.50,
   "font_scale":1.1,

   "blue_file":
   {
      "fits_file":"SDSS/SDSS_u.fits",
      "stretch_min":"-0.1s",
      "stretch_max":"max",
      "stretch_mode":"gaussian-log"
   },

   "green_file":
   {
      "fits_file":"SDSS/SDSS_g.fits",
      "stretch_min":"-0.1s",
      "stretch_max":"max",
      "stretch_mode":"gaussian-log"
   },

   "red_file":
   {
      "fits_file":"SDSS/SDSS_r.fits",
      "stretch_min":"-0.1s",
      "stretch_max":"max",
      "stretch_mode":"gaussian-log"
   },

   "overlays":
   [
      {
         "type":"grid",
         "coord_sys":"Equ J2000",
         "color":"8080ff"
      },
      {
         "type":"imginfo",
         "data_file":"SDSS/irspeakup.tbl",
         "coord_sys":"Equ J2000",
         "color":"ff9090"
      },
      {
         "type":"catalog",
         "data_file":"SDSS/fp_2mass.tbl",
         "data_column":"j_m",
         "data_ref":16,
         "data_type":"mag",
         "symbol":"circle",
         "sym_size":1.0,
         "coord_sys":"Equ J2000",
         "color":"ffff00"
      }
   ]
}
"""

rtn = mViewer(imgjson, 'work/SDSS/SDSS.png', mode=1)

print(rtn)
