test-smyt:
  django_addr: http://127.0.0.1:8000
  port: 8000
  server_name: test-smyt.loc
  venv_dir: /home/vagrant/env/test-smyt-env
  work_dir: /test_smyt
  settings: test_smyt_project
  log_file: /test_smyt/log/log.txt
  error_log_file: /test_smyt/log/error_log.txt
  workers_count: 3
  run_user: vagrant
  run_group: vagrant


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
    - name: smyt
      charset: utf8
    - name: test_smyt
      charset: utf8
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
        - database: test_smyt
          grants: ['all privileges']