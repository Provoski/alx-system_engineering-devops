<<<<<<< HEAD
# creates a file

file { '/tmp/school':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
=======
# creating file#

user { 'www.data':
 ensure => present,
 managehome => false,
}

file { '/tmp/shool':
 ensure => file,
 owner => 'www.data',
 group => 'www.data',
 mode => '0744',
 content => 'I love puppet'
>>>>>>> d26f1f1292c3d145d1c98434b2b7f5dd027e766b
}
