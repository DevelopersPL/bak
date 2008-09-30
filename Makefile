prefix=

install:
	mkdir -p $(prefix)/etc/cron.daily
	install -m 755 bak $(prefix)/etc/cron.daily/bak
	install -m 644 bak.conf $(prefix)/etc/bak.conf


version=0.1
archive:
	git archive --format=tar --prefix=bak-$(version)/ HEAD | gzip > bak-$(version).tar.gz