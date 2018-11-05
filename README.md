# binary_life
- Download project
    ```
      $ git clone git@github.com:Jedore/binary_life.git
      $ cd binary_life
    ```
- Install Anaconda 3
  - after installation create a environment with python 3.6
    ```
    $ conda create -n binary_life python=3.6
    ```
  - install essential package
    ```
    $ su
    $ conda env update -f binary_life.yml
    ```
- Configure settings.py file

  ```
  vim binary_life/settings.py
  ```
  add you ip address to `ALLOWED_HOSTS`
  ```
  ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'jedoremad.com']
  ```
- Collect static resource for Django
  ```
  $ python manage.py collectstatic
  ```
- Run
  ```
  $ python manage.py runserver 0.0.0.0:8000
  ```
- Access the website from browser
