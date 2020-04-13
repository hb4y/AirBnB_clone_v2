# Puppet script that sets up the servers for the deployment of web_static.

$cfg = "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By ${hostname};
	root   /var/www/html;
	index  index.html index.htm;
	location /hbnb_static {
		alias /data/web_static/current;
		index index.html;
	}
	location /redirect_me {
		return 301 http://cuberule.com/;
	}
	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}"

$cont = "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>\n"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
}

file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => $cont,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => yes,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/var/www':
  ensure => 'directory',
}

file { '/var/www/html':
  ensure => 'directory',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Holberton School by Puppet\n",
}

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $cfg,
}

exec { 'nginx restart':
  path => '/etc/init.d/'
}
