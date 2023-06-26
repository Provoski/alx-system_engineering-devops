# configuring remote server using puppet

file { '/home/vagrant/.ssh/config':
  ensure  => file,
  owner   => 'vagrant',
  group   => 'vagrant',
  mode    => '0600',
  content => "
    Host 34.207.57.139
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
