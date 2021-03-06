httpie-apikeyquery
==================

For situations where the API key is passed as a parameter in the query.

Very much based on code in requests_auth_.

.. _requests_auth: https://github.com/Colin-b/requests_auth

Installing
----------

Clone the repository then `cd` into the cloned directory and run:

.. code-block:: shell

    python3 setup.py install

Ensure that the Python used here is the same one that HTTPie runs with.

Confirm installation by running `http --help` and referring to the Authentication `auth-type` section where you should find an entry for apikey.

Usage
-----

Set --auth-type to apikey and for credentials set -a to "query parameter name:key value". If you skip the query parameter name, it will default to `api_key`.

For example:

.. code-block:: shell

    https --auth-type apikey -a ":7e23cee5bfb742e781fccc26b9e9009f" api.themoviedb.org/3/movie/550


Usage with sessions
-------------------

This is most useful when used with HTTPie sessions_.

.. _sessions: https://httpie.io/docs#sessions

Perform a request with `--session name` and the `--auth-type` and `-a` settings like so:

.. code-block:: shell

   https --session tmdb --auth-type apikey -a ":7e23cee5bfb742e781fccc26b9e9009f" api.themoviedb.org/3/movie/550

The named session retains the authentication data, so now you just refer to that session to make a new query:

.. code-block:: shell

   https --session tmdb api.themoviedb.org/3/movie/551




