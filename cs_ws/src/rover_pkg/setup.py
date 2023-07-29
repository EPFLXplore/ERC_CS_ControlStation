from setuptools import setup

package_name = 'rover_pkg'

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
            'rover = rover_pkg.rover:main',
            'cameras_publisher = rover_pkg.cameras_publisher:main',
            'gripper_camera = rover_pkg.gripper_camera:main'
        ],
    },
)