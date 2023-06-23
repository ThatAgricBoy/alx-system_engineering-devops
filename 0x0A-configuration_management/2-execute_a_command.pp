# How to use the exec resource of Puppet

exec { 'kill_process':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  refreshonly => true,
  }
