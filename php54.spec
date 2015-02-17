# This is a sample spec file for php54

%define _topdir	 	/home/vagrant/rpmbuild
%define name		php54
%define release		1
%define version 	1.0
%define buildroot %{_topdir}/%{name}-%{version}

BuildRoot:	%{buildroot}
Summary: 		GNU php version 5.4.37 named as php54
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/usr
Group: 			Development/Tools

%description
PHP54 hack currently on 5.4.37

%prep
rm -rf %{_topdir}/BUILD/*

%setup -q

%build
bash configure --with-pdo-pgsql --with-zlib-dir --with-freetype-dir \
        --enable-mbstring --with-libxml-dir=/usr --enable-soap --enable-calendar --with-curl --with-mcrypt \
        --with-zlib --with-gd --with-pgsql --disable-rpath --enable-inline-optimization --with-bz2 \
        --with-zlib --enable-sockets --enable-sysvsem --enable-sysvshm --enable-pcntl --enable-mbregex \
        --with-mhash --enable-zip --with-pcre-regex --with-mysql --with-pdo-mysql --with-mysqli --with-jpeg-dir=/usr \
        --with-png-dir=/usr --enable-gd-native-ttf --with-openssl --with-fpm-user=nginx --with-fpm-group=nginx \
        --with-libdir=lib64 --enable-ftp --with-imap --with-imap-ssl --with-kerberos --with-gettext --enable-fpm;
make

%install
%make_install
#/bin/echo "installing under /opt/%{name}"
#make install DESTDIR=${RPM_BUILD_ROOT}
#/bin/mkdir -p /opt/php54
#rm -rf /opt/php54/*
#/bin/cp -rf * /opt/php54
#/bin/ln -sf /opt/%{name}/bin/php /usr/bin/php54

%files
%defattr(-,root,root)
/usr/php54
#%doc %attr(0444,root,root) prefix=/opt/%{name}/php/man/man1/php.1

%clean
rm -rf $RPM_BUILD_ROOT