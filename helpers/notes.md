# notes

The redirect code of the `0-setup...sh` file i.e `/data/web_static/current/ to redirect to webcronx.tech/hbnb_static` should appear this way in line 38 of the `/etc/nginx/sites-available/default`

```
server {
	...
	...
	...
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}
```