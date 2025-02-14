## About PyQGIS.

PyQGIS is the Python environment inside QGIS with a set of QGIS libraries <br>
plus the Python tools with the potential of running other powerful  <br>
libraries as Pandas, Numpy or Scikit-learn.

## Section one, here is links of spatial analyse python cources

=== "Unordered list"
    * Geospatial Analysis with [Python](https://ohm-np.github.io/Python_tutorial/intro.html) By Om Prakash Bhandari
    * Introduction to GIS [Programming](https://geog-312.gishub.org/) By Qiusheng Wu
    * OpenCourseWare for [GIS](https://courses.gisopencourseware.org//) IHE DELFT
    * Python Foundation for Spatial [Analysis](https://courses.spatialthoughts.com/python-foundation.html) by Ujaval Gandhi
    * Mapping and Data Visualization with [Python](https://courses.spatialthoughts.com/python-dataviz.html) by Ujaval Gandhi
    * Welcome to Geo-Python [2024!](https://geo-python-site.readthedocs.io/en/latest/)

### And this is section two where is python code added

```py title="DMS_DD.py" linenums="1" hl_lines="7 8"

def transformation(deg, min, sec):

    result = deg + min/60 + sec/3600

    return result

print(transformation(42, 12, 47.83))
print(transformation(43, 19, 27.72))

#შედეგი: 42.21328611111112 43.32436666666667
```