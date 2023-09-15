from setuptools import setup

package_name = 'control_station_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zedrichu',
    maintainer_email='zedrichu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control_station = control_station_pkg.control_station:main',
            'cameras_reciever = control_station_pkg.cameras_reciever',
            'camera_subscriber = control_station_pkg.camera_subscriber:main'
        ],
    },
)
