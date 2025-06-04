from setuptools import setup

package_name = 'romana_controller'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Edson Contreras',
    maintainer_email='edrecon@gmail.com',
    description='Software de control de pesa romana',
    license='Licencia MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'romana_serial_node = romana_controller.romana_serial_node:main',
            'romana_software_node = romana_controller.romana_software_node:main'
        ],
    },
)
