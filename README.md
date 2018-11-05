# binary_life
- Download project
  ```
  $ git clone git@github.com:Jedore/binary_life.git
  $ cd binary_life
  ```
- Create Env With Anaconda 3
  ```
  $ conda env create -p /home/jedore/anaconda3/envs/binary_life -f binary_life.yml
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
