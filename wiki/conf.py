# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

html_theme = 'alabaster'



project = 'distro Wiki'
copyright = 'distro 2023'
author = 'karahan'
language = 'tr'
version= '1.0'
extensions = ['sphinx.ext.autodoc', 'rst2pdf.pdfbuilder']
smartquotes = False

# -- Options for PDF output --
extensions = ['sphinx.ext.autodoc', 'rst2pdf.pdfbuilder']

pdf_documents = [('index', u'rst2pdf', u'Kendi Linux`unu Yap', u'KLY'),]

pdf_stylesheets = ['style-main.yaml', 'tango', 'mytheme']  # .style uzantısını yazma

pdf_style_path = ['.', 'wiki/_static']

pdf_use_coverpage = False
pdf_use_toc = False
pdf_default_dpi = 96
pdf_compressed = True
pdf_language = "tr_TR"
pdf_fit_mode = "shrink"

# -- Options for HTML output --

html_baseurl = 'https://kendilinuxunuyap.github.io/'
#html_theme = 'alabaster'


html_static_path = ['_static']
html_theme_options = {
    'font_family' : 'monospace',
    'footnote_bg': 'none',
    'page_width': '100%',
    'body_max_width': 'auto',
    'logo': 'logo.svg',

}
html_css_files = [
    'custom.css',
]
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
    ]
}

latex_elements = {
    'preamble': r'''
\usepackage{xcolor}
\usepackage{tcolorbox}
\tcbset{listing engine=listings}

\newtcblisting{mybashlisting}{
    listing only,
    listing options={language=bash, basicstyle=\ttfamily\small},
    colback=gray!5,
    colframe=gray!90,
    width=0.9\textwidth,
    height=0.3\textheight,
    floatplacement=h!,
}

\hypersetup{
    colorlinks=true,
    linkcolor=red,   % <== :ref: bağlantı rengi (değiştirebilirsin)
    urlcolor=black,
    citecolor=black
}
''',
}

