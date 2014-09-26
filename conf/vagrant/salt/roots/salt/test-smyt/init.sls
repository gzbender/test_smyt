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
        - name: /etc/nginx/sites-enabled/{{ app_name }}.conf
        - source: salt://{{ app_name }}/nginx.conf
        - context: # помимо переменных вроде pillar, мы можем передать дополнительный контекст для тепмлейта
            django_addr: {{ app['django_addr'] }}
            server_name: {{ app['server_name'] }}
            path: {{ app['work_dir'] }}
        - template: jinja
        - makedirs: True
        - watch_in:
            - service: nginx