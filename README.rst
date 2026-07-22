pretalx-plugin-cookiecutter
===========================

A simple `cookiecutter`_ template to bootstrap a `pretalx`_ plugin.

Usage
-----

Let's pretend you want to create a pretalx plugin called "foobar"::

    $ cd <your-project-folder-parent>
    $ uvx cookiecutter https://github.com/pretalx/pretalx-plugin-cookiecutter


You'll be prompted for some questions. Answer them, and you will find a
project folder created for you::

    [1/8] human_name (pretalx FooBar plugin): pretalx JSON plugin
    [2/8] module_name (pretalx_json):
    [3/8] short_description (pretalx plugin for pretalx JSON plugin): pretalx plugin for custom JSON exports
    [4/8] author_name (Your name): Tobias Kunze
    [5/8] author_email (your-email@example.org): r@rixx.de
    [6/8] repo_url (https://github.com/r/pretalx-json): https://github.com/rixx/pretalx-json
    [7/8] Select create_github_repo
    1 - no
    2 - yes
    Choose from [1/2] (1): 1
    [8/8] Select category
    1 - FEATURE
    2 - INTEGRATION
    3 - CUSTOMIZATION
    4 - EXPORTER
    5 - RECORDING
    6 - LANGUAGE
    7 - OTHER
    Choose from [1/2/3/4/5/6/7] (1): 1

Now, change to the newly created directory::

    $ cd pretalx-foobar

Voilà, there's your plugin structure! See pretalx' `documentation`_ for more info.

.. _pretalx: https://github.com/pretalx/pretalx
.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _documentation: https://docs.pretalx.org/developer/plugins/plugins/
