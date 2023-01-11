#a puppet configuration
class ssh_config {

  file { '/etc/ssh/ssh_config':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => template('ssh_config.erb'),
  }
}

