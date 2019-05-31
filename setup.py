from setuptools import setup, find_packages

setup(
    name='fpython',
    version='0.0.1',
    keywords=('utils', 'packages'),
    description='packages',
    license='Free',
    author='Wall-js',
    author_email='307606056@qq.com',
    url='https://github.com/Wall-js/fpython',
    platforms='any',
    packages=find_packages('absolute path or relative path of src'),
    package_dir={'': 'absolute path or relative path of src'},
    classifiers=[
        'Development Status :: 3 - Alpha',  # 当前开发进度等级（测试版，正式版等）

        'Intended Audience :: Developers',  # 模块适用人群
        'Topic :: Software Development :: Build Tools',  # 给模块加话题标签

        'License :: OSI Approved :: MIT License',  # 模块的license

        'Programming Language :: Python :: 2',  # 模块支持的Python版本
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

)
