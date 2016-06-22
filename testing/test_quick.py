import math, cmath
import numpy
import vectorfieldplot as vfp

def test_dipole():

  sources = vfp.SourceCollection()
  sources.add_source( vfp.PointCharge( [0, 1], q= 1 ) )
  sources.add_source( vfp.PointCharge( [0,-1], q=-1 ) )
  sources.add_source( vfp.PointCharge( [1,-1], q=-2 ) )

  doc = vfp.FieldplotDocument( 'ElectricDipole', width=800,height=600,unit=100)
  doc.draw_sources(sources)

  fieldlines = vfp.FieldLineCollection()
  fieldlines.add_lines_to_point_charges( sources, 10 )

  doc.draw_fieldlines( fieldlines )



  doc.write()




