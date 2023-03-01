exec { 'restart-apache':
  command => '/etc/init.d/apache2 restart',
}
