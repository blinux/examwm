#-
# Copyright 2015 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:		examwm
Version:        0.13
Release:        0
Summary:        EXAM Window Manager
License:        BSD-2-Clause
Group:          System/X11/Windowmanagers

Source0:        examwm
Source1:	examwm_do
Source2:	examwm.desktop
Source3:	exam_get_subject
Source4:	exam_rendu

Requires:	wpa_supplicant-gui
Requires:	icewm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Vendor:         Bocal
Packager:       Emmanuel Vadot <elbarto@bocal.org>
Url:            http://www.blinux.fr

%description
Window manager for Blinux exam mode

%prep

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/share/xsessions/
mkdir -p %{buildroot}/home/exam/end/
mkdir -p %{buildroot}/home/exam/rendu/
mkdir -p %{buildroot}/home/exam/sujet/
install -D -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/
install -D -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}/
install -D -p -m 755 %{SOURCE3} %{buildroot}/%{_bindir}/
install -D -p -m 755 %{SOURCE4} %{buildroot}/%{_bindir}/
install -D -p -m 755 %{SOURCE2} %{buildroot}/usr/share/xsessions/
touch %{buildroot}/home/exam/end/time

%clean
rm -rf %{buildroot}

%post
rm -f /usr/share/xsessions/icewm.desktop
mkdir /home/exam/.gnome2/
mkdir /home/exam/.gnome2_private/
mkdir /home/exam/.config/terminator/
chown exam:users /home/exam/.gnome2/
chown exam:users /home/exam/.gnome2_private/
chown exam:users /home/exam/.config/terminator/

%files
%defattr(-,root,root)
%{_bindir}/examwm
%{_bindir}/examwm_do
%{_bindir}/exam_get_subject
%{_bindir}/exam_rendu
/usr/share/xsessions/examwm.desktop
%attr(0755, exam, users) /home/exam/end/
%attr(0755, exam, users) /home/exam/end/time
%attr(0755, exam, users) /home/exam/rendu/
%attr(0755, exam, users) /home/exam/sujet/

%changelog
* Sat Oct 04 2014 Emmanuel Vadot <elbarto@bocal.org> - 0.6-0
- Update exam_rendu

* Thu Aug 28 2014 Emmanuel Vadot <elbarto@bocal.org> - 0.5-0
- Update examwm_do

* Thu Aug 28 2014 Emmanuel Vadot <elbarto@bocal.org> - 0.4-0
- Update exam_rendu

* Thu Aug 28 2014 Emmanuel Vadot <elbarto@bocal.org> - 0.1-0
- Package creation
