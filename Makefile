

install:
	install -m 755 bak /etc/cron.daily/bak
	install -m 644 bak.conf /etc/bak.conf
