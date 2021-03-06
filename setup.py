import setuptools
from setuptools import setup

using_setuptools = True

setup_args = {
    'name': 'flowopt',
    'version': '0.1.2',
    'url': 'https://github.com/ga1008/flow_operate',
    'description': 'control the mouse and keyboard todo repeat jobs',
    'long_description': open('README.md', encoding="utf-8").read(),
    'author': 'Guardian',
    'author_email': 'zhling2012@live.com',
    'maintainer': 'Guardian',
    'maintainer_email': 'zhling2012@live.com',
    'long_description_content_type': "text/markdown",
    'LICENSE': 'MIT',
    'packages': setuptools.find_packages(),
    'include_package_data': True,
    'zip_safe': False,
    'entry_points': {
        'console_scripts': [
            'flowopt = FlowOpt.flow_operation:start_missions',
            'ilocate = FlowOpt.flow_operation:locate_image',
            'clocate = FlowOpt.flow_operation:locate_color',
        ]
    },

    'classifiers': [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    'install_requires': [
        "matplotlib",
        "numpy==1.19.3",
        "pyautogui",
        "requests",
        "basecolors==0.0.2",
        "pillow",
        "scikit-image",
        "redis",
    ],
}

setup(**setup_args)
