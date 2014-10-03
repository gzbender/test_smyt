{% set app_name = 'test-smyt' %}
{% set app = pillar[app_name] %}

{{ app_name }}.pkgs:
  pkg.installed:
    - names:
      - git
      - python-dev
      - libev4
      - libev-dev
      - build-essential

{{ app_name }}.venv:
  virtualenv.managed:
    - name: {{ app['venv_dir'] }}
    - system_site_packages: True
    - require:
      - pkg: python2

{{ app_name }}.pip:
  pip.installed:
    - bin_env: {{ app['venv_dir'] }}
    - requirements: salt://{{ app_name }}/requirements.txt
    - require:
      - virtualenv: {{ app_name }}.venv
      - pkg: {{ app_name }}.pkgs

{{ app_name }}.nginx.conf:
  file.managed:
    - name: {{ app['work_dir'] }}/conf/nginx.conf
    - source: salt://{{ app_name }}/nginx.conf
    - context: # помимо переменных вроде pillar, мы можем передать дополнительный контекст для тепмлейта
      django_addr: {{ app['django_addr'] }}
      server_name: {{ app['server_name'] }}
      path: {{ app['work_dir'] }}
    - template: jinja
    - makedirs: True
    - watch_in:
      - service: nginx

{{ app_name }}.run.sh:
  file.managed:
    - name: {{ app['work_dir'] }}/run.sh
    - source: salt://{{ app_name }}/run.sh
    - context:
      path: {{ app['work_dir'] }}
      wsgi_app: {{ app['settings'] }}.wsgi:application
      log_file: {{ app['log_file'] }}
      workers: {{ app['workers_count'] }}
      user: {{ app['run_user'] }}
      group: {{ app['run_group'] }}
      port: {{ app['port'] }}
      env_path: {{ app['venv_dir'] }}
    - template: jinja
    - makedirs: True

{{ app_name }}.supervisor.conf:
  file.managed:
    - name: {{ app['work_dir'] }}/conf/supervisor.conf
    - source: salt://{{ app_name }}/supervisor.conf
    - context:
      app: {{ app_name }}
      path: {{ app['work_dir'] }}
      user: {{ app['run_user'] }}
      run_script: {{ app['work_dir'] }}/run.sh
      log_file: {{ app['log_file'] }}
      error_log_file: {{ app['error_log_file'] }}
    - template: jinja
    - makedirs: True

supervisor.conf:
  cmd.run:
    - unless:
      - file.exist: /etc/supervisor.conf
    - source: salt://{{ app_name }}/supervisor_conf.sh
    - require:
      - virtualenv: {{ app_name }}.venv

/etc/supervisor/conf.d/{{ app_name }}.conf:
  file.symlink:
    - target: {{ app['work_dir'] }}/conf/supervisor.conf
    - makedirs: True
    - require:
      - cmd: supervisor.conf

/etc/nginx/sites-enabled/{{ app_name }}.conf:
  file.symlink:
    - target: {{ app['work_dir'] }}/conf/nginx.conf
    - watch_in:
      - service: nginx
    - require:
      - pkg: nginx
      - file: {{ app_name }}.nginx.conf
