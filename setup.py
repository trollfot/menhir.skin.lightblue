from setuptools import setup, find_packages
from os.path import join

name = 'menhir.skin.lightblue'
version = '0.1'
readme = open("README.txt").read()
history = open(join("docs", "HISTORY.txt")).read()

setup(name = name,
      version = version,
      description = 'Dolmen skin extension : lightblue',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      keywords = 'Grok Zope3 CMS Dolmen',
      author = 'Souheil Chelfouh',
      author_email = 'souheil@chelfouh.com',
      url = 'http://tracker.trollfot.org/',
      download_url = 'http://pypi.python.org/pypi/menhir.skin.lightblue',
      license = 'GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages = ['menhir', 'menhir.skin'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = True,
      install_requires=[
          'dolmen.app.layout',
          'dolmen.forms.crud',
          'fanstatic',
          'grokcore.viewlet',
          'js.jquery',
          'js.jquery_tablesorter',
          'megrok.chameleon',
          'megrok.pagetemplate',
          'setuptools',
      ],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Grok',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
      entry_points = """
      [fanstatic.libraries]
      lightblue = menhir.skin.lightblue:LightblueLibrary
      """,


)
