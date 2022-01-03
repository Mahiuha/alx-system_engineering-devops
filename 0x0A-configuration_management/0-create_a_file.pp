#This creates a file in the /tmp directory.

file { 'create':
    path => '/tmp/school',
    mode => '0744',
    owner => 'www-data',
    group => 'www-data',
    content => 'I love Puppet',
}

