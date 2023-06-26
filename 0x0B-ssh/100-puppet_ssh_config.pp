# configuring remote server using puppet

$ssh_user = $::id::user
$ssh_group = $::id::group
file { 'ssh_config':
  path    => '/etc/ssh/ssh_config',
  ensure  => file,
  owner   => $ssh_user,
  group   => $ssh_group,
  mode    => '0600',
  content => "
    Host 34.207.57.139
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
