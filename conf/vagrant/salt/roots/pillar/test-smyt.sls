test-smyt:
  django_addr: http://127.0.0.1:8000
  server_name: test-smyt.loc
  venv_dir: /home/vagrant/env/test-smyt-env
  work_dir: /test-smyt

python2:
  lookup:
    pkg: python2.7

mysql:
  charset: utf8
  server:
    root_password: 'somepass'
    bind-address: 127.0.0.1
    port: 3306
    user: mysql

  # Manage databases
  database:
    - smyt
  schema:
    smyt:
      load: False

  # Manage users
  user:
    - name: smyt
      password: 'somepass'
      host: localhost
      databases:
        - database: smyt
          grants: ['all privileges']