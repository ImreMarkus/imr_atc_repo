from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'kisbeadando_feladat'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ImreMarkus',
    maintainer_email='hitex98@gmail.com',
    description='Kisbeadandó',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
            'console_scripts': [
                    'lidar_simulator = kisbeadando_feladat.lidar_simulator:main',
                    'obstacle_monitor = kisbeadando_feladat.obstacle_monitor:main',
        ],
    },
)
