# creating file#

user { 'www.data':
	ensure	=> present,
	managehome	=> false,
	home	=> '/var/www/data',
	shell	=> '/bin/bash',
}

file { '/tmp/school':
	ensure	=> file,
 	owner 	=> 'www.data',
 	group	=> 'www.data',
 	mode	=> '0744',
 	content	=> 'I love puppet'
}
