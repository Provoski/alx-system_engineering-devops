# Script to install nginx using puppet

exec { 'configure':
  command  => 'sudo sed -i "/^http {/a         add_header X-Served-By  $(hostname);" /etc/nginx/nginx.conf',
  onlyif   => '! grep -q "add_header X-Served-By" /etc/nginx/nginx.conf',
  provider => shell,
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}

