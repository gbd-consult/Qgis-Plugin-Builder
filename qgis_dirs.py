""" Get the deployment directory for QGIS plugins based on operating system"""
import os
from qgis.core import QgsApplication

# Deployment directory
def deployment_dir():
    dir = os.path.relpath(
        QgsApplication.qgisSettingsDirPath(),
        os.environ['HOME']
    )
    print(dir)
    return(dir)
