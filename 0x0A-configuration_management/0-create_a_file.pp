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
}
