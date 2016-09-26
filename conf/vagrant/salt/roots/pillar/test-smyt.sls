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

postgres:
  pg_hba.conf: salt://postgres/pg_hba.conf

  use_upstream_repo: True

  lookup:
    id: '9.4'

  users:
    user:
      password: 'pass'
      createdb: True

  # This section cover this ACL management of the pg_hba.conf file.
  # <type>, <database>, <user>, [host], <method>
  acls:
    - ['local', 'db', 'user', 'trust']

  databases:
    db:
      owner: 'user'
      user: 'user'
      template: 'template0'
      lc_ctype: 'C.UTF-8'
      lc_collate: 'C.UTF-8'

  # This section will append your configuration to postgresql.conf.
  postgresconf: |
    listen_addresses = 'localhost,*'