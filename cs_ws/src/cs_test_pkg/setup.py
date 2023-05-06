from setuptools import setup

package_name = 'cs_test_pkg'

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
    maintainer='evan',
    maintainer_email='evanmassonnet@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'science_test_node = cs_test_pkg.science_test_node:main',
            'elec_test_node = cs_test_pkg.elec_test_node:main',
            'hd_test_node = cs_test_pkg.hd_test_node:main',
            'nav_test_node = cs_test_pkg.nav_test_node:main',
            'gamepad_test_node = cs_test_pkg.gamepad_test_node:main',
        ],
    },
)
