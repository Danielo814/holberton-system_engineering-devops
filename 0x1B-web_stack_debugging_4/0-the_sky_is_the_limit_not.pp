# puppet script to fix limit of files that can be open

exec { 'fix ulimit':
  path    => '/bin:/usr/bin',
  command => "sed -i 's/15/30000/g' /etc/default/nginx; sudo service nginx restart;"
}
