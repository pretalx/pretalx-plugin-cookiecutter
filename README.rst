pretalx-plugin-cookiecutter
===========================

A simple `cookiecutter`_ template to bootstrap a `pretalx`_ plugin.

Usage
-----

Let's pretend you want to create a pretalx plugin called "superplugin".
First, create a virtual environment and install the ``cookiecutter``
package using pip. Next, use it to bootstrap your project folder::

    $ cd <your-project-folder-parent>
    $ cookiecutter https://github.com/pretalx/pretalx-plugin-cookiecutter


You'll be prompted for some questions. Answer them, and you will find a
project folder created for you::

    repo_name [pretalx-superplugin]: pretalx-superplugin
    repo_url [GitHub repository URL]: https://github.com/myuser/pretalx-superplugin
    module_name [pretalx_superplugin]: pretalx_superplugin
    human_name [The pretalx super plugin]: Super Plugin
    author_name [Your name]: J Random Developer
    author_email [Your email]: jrandom@example.org
    short_description [Short description]: The best plugin
    Select category:
    1 - FEATURE
    2 - INTEGRATION
    3 - CUSTOMIZATION
    4 - EXPORTER
    5 - RECORDING
    6 - LANGUAGE
    7 - OTHER
    Choose from 1, 2, 3, 4, 5 [1]: 1

Now, change to the newly created directory::

    $ cd pretalx-superplugin

Voilà, there's your plugin structure! See pretalx' `documentation`_ for more info.

.. _pretalx: https://github.com/pretalx/pretalx
.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _documentation: https://docs.pretalx.org/en/latest/developer/plugins/index.html
