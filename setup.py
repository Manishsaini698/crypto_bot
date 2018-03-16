setup(
    name='crypto_bot',
    version='0.1',
    description='A simple Telegram Bot',
    long_description=readme,
    author='Manish Saini',
    url='http://github.com/Manishsaini698/crypto_bot',
    license=license,
    packages=find_packages(where='src'),
    package_dir={'':'src'},
    install_requires=['requests','bs4','lxml','telepot','redis'],
    entry_points={
        '':['crypto_bot=crypto_bot.']
    })