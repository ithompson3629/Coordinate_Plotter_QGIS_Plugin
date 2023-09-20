# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CoordinatePlotter
                                 A QGIS plugin
 This plugin plots cordinates for a vector layer from user input
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-09-20
        copyright            : (C) 2023 by Isaac
        email                : ithompson@pre-construct.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CoordinatePlotter class from file CoordinatePlotter.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Coordinate_Plotter import CoordinatePlotter
    return CoordinatePlotter(iface)
