# Client configuration file with Puppet
file_line {  'passw_no_autentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line {  'passw_direction':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
