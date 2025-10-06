# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global jspspec 2.3
%global major_version 9
%global minor_version 0
%global micro_version 87
%global packdname tomcat-%{major_version}.%{minor_version}.%{micro_version}.redhat-00012-src
%global servletspec 4.0
%global elspec 3.0
%global tcuid 53

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir %{_var}/lib/tomcat
%global appdir %{basedir}/webapps
%global homedir %{_datadir}/tomcat
%global bindir %{homedir}/bin
%global confdir %{_sysconfdir}/tomcat
%global libdir %{_javadir}/tomcat
%global logdir %{_var}/log/tomcat
%global cachedir %{_var}/cache/tomcat
%global tempdir %{cachedir}/temp
%global workdir %{cachedir}/work
%global _systemddir /lib/systemd/system

Name:          tomcat9
Epoch:         1
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:       5%{?dist}.3
Summary:       Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

License:       Apache-2.0
URL:           http://tomcat.apache.org/
Source0:       %{packdname}.zip
Source1:       tomcat-%{major_version}.%{minor_version}.conf
Source3:       tomcat-%{major_version}.%{minor_version}.sysconfig
Source4:       tomcat-%{major_version}.%{minor_version}.wrapper
Source5:       tomcat-%{major_version}.%{minor_version}.logrotate
Source6:       tomcat-%{major_version}.%{minor_version}-digest.script
Source7:       tomcat-%{major_version}.%{minor_version}-tool-wrapper.script
Source11:      tomcat-%{major_version}.%{minor_version}.service
Source21:      tomcat-functions
Source30:      tomcat-preamble
Source31:      tomcat-server
Source32:      tomcat-named.service
Source33:      java-9-start-up-parameters.conf

Patch0:        tomcat-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1:        tomcat-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
Patch3:        tomcat-%{major_version}.%{minor_version}-catalina-policy.patch
Patch4:        rhbz-1857043.patch
Patch6:        tomcat-%{major_version}.%{minor_version}-bnd-annotation.patch
Patch7:        JmxRemoteLifecycleListener.patch

BuildArch:     noarch

BuildRequires: ant
BuildRequires: ecj >= 1:4.10
BuildRequires: findutils
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: aqute-bnd
BuildRequires: aqute-bndlib
BuildRequires: systemd

Requires:      java-headless
Requires:      javapackages-tools
Requires:      %{name}-lib = %{epoch}:%{version}-%{release}

Requires(pre):    shadow-utils
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

Conflicts: tomcat
Obsoletes: tomcat < 1:10.0.0-1

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%package admin-webapps
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
Conflicts: tomcat
Conflicts: tomcat-admin-webapps
Obsoletes: tomcat-admin-webapps < 1:10.0.0-1

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
Conflicts: tomcat
Conflicts: tomcat-docs-webapp
Obsoletes: tomcat-docs-webapps < 1:10.0.0-1

%description docs-webapp
The docs web application for Apache Tomcat.

%package jsp-%{jspspec}-api
Summary: Apache Tomcat JavaServer Pages v%{jspspec} API Implementation Classes
Provides: jsp = %{jspspec}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Conflicts: tomcat
Conflicts: tomcat-jsp-2.3-api
Conflicts: tomcat-jsp-3.1-api
Obsoletes: tomcat-jsp-%{jspspec}-api < 1:10.0.0-1

%description jsp-%{jspspec}-api
Apache Tomcat JSP API Implementation Classes.

%package lib
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: ecj >= 1:4.10
Requires(preun): coreutils
Conflicts: tomcat
Conflicts: tomcat-lib
Conflicts: tomcat-jsp-2.3-api
Conflicts: tomcat-jsp-3.1-api
Conflicts: tomcat-servlet-4.0-api
Conflicts: tomcat-servlet-6.0-api
Conflicts: tomcat-el-3.0-api
Conflicts: tomcat-el-5.0-api
Obsoletes: tomcat-lib < 1:10.0.0-1

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Summary: Apache Tomcat Java Servlet v%{servletspec} API Implementation Classes
Provides: servlet = %{servletspec}
Provides: servlet6
Provides: servlet3
Conflicts: tomcat
Conflicts: tomcat-servlet-4.0-api
Conflicts: tomcat-servlet-6.0-api
Obsoletes: tomcat-servlet-%{servletspec}-api < 1:10.0.0-1

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API Implementation Classes.

%package el-%{elspec}-api
Summary: Apache Tomcat Expression Language v%{elspec} API Implementation Classes
Provides: el_api = %{elspec}
Conflicts: tomcat-el-3.0-api
Conflicts: tomcat-el-5.0-api
Obsoletes: tomcat-el-%{elspec}-api < 1:10.0.0-1

%description el-%{elspec}-api
Apache Tomcat EL API Implementation Classes.

%package webapps
Summary: The ROOT web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
Conflicts: tomcat
Conflicts: tomcat-webapps
Obsoletes: tomcat-webapps < 1:10.0.0-1

%description webapps
The ROOT web application for Apache Tomcat.

%prep
%setup -q -n apache-%{packdname}
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch -P0 -p0
%patch -P1 -p0
%patch -P3 -p0
%patch -P4 -p0
%patch -P6 -p0
%patch -P7 -p1

# Remove webservices naming resources as it's generally unused
%{__rm} -rf java/org/apache/naming/factory/webservices

# Configure maven files
%mvn_package ":tomcat-el-api" tomcat-el-api
%mvn_alias "org.apache.tomcat:tomcat-el-api" "org.eclipse.jetty.orbit:javax.el"
%mvn_package ":tomcat-jsp-api" tomcat-jsp-api
%mvn_alias "org.apache.tomcat:tomcat-jsp-api" "org.eclipse.jetty.orbit:javax.servlet.jsp"
%mvn_package ":tomcat-servlet-api" tomcat-servlet-api


%build
export OPT_JAR_LIST="xalan-j2-serializer"
# we don't care about the tarballs and we're going to replace
# tomcat-dbcp.jar with apache-commons-{collections,dbcp,pool}-tomcat5.jar
# so just create a dummy file for later removal
touch HACK

# who needs a build.properties file anyway
%{ant} -Dbase.path="." \
  -Dbuild.compiler="modern" \
  -Dcommons-daemon.jar="HACK" \
  -Dcommons-daemon.native.src.tgz="HACK" \
  -Djdt.jar="$(build-classpath ecj/ecj)" \
  -Dtomcat-native.tar.gz="HACK" \
  -Dtomcat-native.home="." \
  -Dcommons-daemon.native.win.mgr.exe="HACK" \
  -Dnsis.exe="HACK" \
  -Djaxrpc-lib.jar="HACK" \
  -Dwsdl4j-lib.jar="HACK" \
  -Dbnd.jar="$(build-classpath aqute-bnd/biz.aQute.bnd)" \
  -Dbnd-annotation.jar="$(build-classpath aqute-bnd/biz.aQute.bnd.annotation)" \
  -Dversion="%{version}" \
  -Dversion.build="%{micro_version}" \
  deploy

# remove some jars that we'll replace with symlinks later
%{__rm} output/build/lib/ecj.jar
# Remove the example webapps per Apache Tomcat Security Considerations
# see https://tomcat.apache.org/tomcat-9.0-doc/security-howto.html
%{__rm} -rf output/build/webapps/examples


%install
# build initial path structure
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sbindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_systemddir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{appdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{bindir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}/conf.d
/bin/echo "Place your custom *.conf files here. Shell expansion is supported." > ${RPM_BUILD_ROOT}%{confdir}/conf.d/README
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{libdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{logdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{_localstatedir}/lib/tomcats
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{homedir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{tempdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{workdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_unitdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_libexecdir}/tomcat

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    %{__cp} -a bin/*.{jar,xml} ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} -a conf/*.{policy,properties,xml,xsd} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
    %{__cp} -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd

%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > ${RPM_BUILD_ROOT}%{confdir}/tomcat.conf
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE3} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/tomcat
%{__install} -m 0644 %{SOURCE4} \
    ${RPM_BUILD_ROOT}%{_sbindir}/tomcat
%{__install} -m 0644 %{SOURCE11} \
    ${RPM_BUILD_ROOT}%{_unitdir}/tomcat.service
%{__sed} -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE5} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/tomcat.disabled
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > ${RPM_BUILD_ROOT}%{_bindir}/tomcat-digest
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE7} \
    > ${RPM_BUILD_ROOT}%{_bindir}/tomcat-tool-wrapper

%{__install} -m 0644 %{SOURCE21} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/tomcat/functions
%{__install} -m 0755 %{SOURCE30} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/tomcat/preamble
%{__install} -m 0755 %{SOURCE31} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/tomcat/server
%{__install} -m 0644 %{SOURCE32} \
    ${RPM_BUILD_ROOT}%{_unitdir}/tomcat@.service

%{__install} -m 0644 %{SOURCE33} ${RPM_BUILD_ROOT}%{confdir}/conf.d/

# Substitute libnames in catalina-tasks.xml
sed -i \
   "s,el-api.jar,tomcat-el-%{elspec}-api.jar,;
    s,servlet-api.jar,tomcat-servlet-%{servletspec}-api.jar,;
    s,jsp-api.jar,tomcat-jsp-%{jspspec}-api.jar,;" \
    ${RPM_BUILD_ROOT}%{bindir}/catalina-tasks.xml

# create jsp and servlet API symlinks
pushd ${RPM_BUILD_ROOT}%{_javadir}
   %{__mv} tomcat/jsp-api.jar tomcat-jsp-%{jspspec}-api.jar
   %{__ln_s} tomcat-jsp-%{jspspec}-api.jar tomcat-jsp-api.jar
   %{__mv} tomcat/servlet-api.jar tomcat-servlet-%{servletspec}-api.jar
   %{__ln_s} tomcat-servlet-%{servletspec}-api.jar tomcat-servlet-api.jar
   %{__mv} tomcat/el-api.jar tomcat-el-%{elspec}-api.jar
   %{__ln_s} tomcat-el-%{elspec}-api.jar tomcat-el-api.jar
popd

pushd output/build
    %{_bindir}/build-jar-repository lib ecj 2>&1
popd

pushd ${RPM_BUILD_ROOT}%{libdir}
    # symlink JSP and servlet API jars
    %{__ln_s} ../../java/tomcat-jsp-%{jspspec}-api.jar .
    %{__ln_s} ../../java/tomcat-servlet-%{servletspec}-api.jar .
    %{__ln_s} ../../java/tomcat-el-%{elspec}-api.jar .
    %{__ln_s} $(build-classpath ecj/ecj) jasper-jdt.jar
    %{__cp} -a ../../tomcat/bin/tomcat-juli.jar .
popd

# symlink to the FHS locations where we've installed things
pushd ${RPM_BUILD_ROOT}%{homedir}
    %{__ln_s} %{appdir} webapps
    %{__ln_s} %{confdir} conf
    %{__ln_s} %{libdir} lib
    %{__ln_s} %{logdir} logs
    %{__ln_s} %{tempdir} temp
    %{__ln_s} %{workdir} work
popd

# Install the maven metadata for the spec impl artifacts as other projects use them
#%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_mavenpomdir}
pushd res/maven
    for pom in *.pom; do
        # fix-up version in all pom files
        sed -i 's/@MAVEN.DEPLOY.VERSION@/%{version}/g' $pom
    done
popd

# Configure and install maven artifacts
%mvn_file org.apache.tomcat:tomcat-el-api tomcat/tomcat-el-api
%mvn_artifact res/maven/tomcat-el-api.pom output/build/lib/el-api.jar

%mvn_file org.apache.tomcat:tomcat-jsp-api tomcat/tomcat-jsp-api
%mvn_artifact res/maven/tomcat-jsp-api.pom output/build/lib/jsp-api.jar

%mvn_file org.apache.tomcat:tomcat-servlet-api tomcat/tomcat-servlet-api
%mvn_artifact res/maven/tomcat-servlet-api.pom output/build/lib/servlet-api.jar

%mvn_file org.apache.tomcat:tomcat-annotations-api tomcat/annotations-api
%mvn_artifact res/maven/tomcat-annotations-api.pom ${RPM_BUILD_ROOT}%{libdir}/annotations-api.jar

%mvn_file org.apache.tomcat:tomcat-api tomcat/tomcat-api
%mvn_artifact res/maven/tomcat-api.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-api.jar

%mvn_file org.apache.tomcat:tomcat-catalina-ant tomcat/catalina-ant
%mvn_artifact res/maven/tomcat-catalina-ant.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-ant.jar

%mvn_file org.apache.tomcat:tomcat-catalina-ha tomcat/catalina-ha
%mvn_artifact res/maven/tomcat-catalina-ha.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-ha.jar

%mvn_file org.apache.tomcat:tomcat-catalina tomcat/catalina
%mvn_artifact res/maven/tomcat-catalina.pom ${RPM_BUILD_ROOT}%{libdir}/catalina.jar

%mvn_file org.apache.tomcat:tomcat-coyote tomcat/tomcat-coyote
%mvn_artifact res/maven/tomcat-coyote.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-coyote.jar

%mvn_file org.apache.tomcat:tomcat-dbcp tomcat/tomcat-dbcp
%mvn_artifact res/maven/tomcat-dbcp.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-dbcp.jar

%mvn_file org.apache.tomcat:tomcat-i18n-cs tomcat/tomcat-i18n-cs
%mvn_artifact res/maven/tomcat-i18n-cs.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-cs.jar

%mvn_file org.apache.tomcat:tomcat-i18n-de tomcat/tomcat-i18n-de
%mvn_artifact res/maven/tomcat-i18n-de.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-de.jar

%mvn_file org.apache.tomcat:tomcat-i18n-es tomcat/tomcat-i18n-es
%mvn_artifact res/maven/tomcat-i18n-es.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-es.jar

%mvn_file org.apache.tomcat:tomcat-i18n-fr tomcat/tomcat-i18n-fr
%mvn_artifact res/maven/tomcat-i18n-fr.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-fr.jar

%mvn_file org.apache.tomcat:tomcat-i18n-ja tomcat/tomcat-i18n-ja
%mvn_artifact res/maven/tomcat-i18n-ja.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-ja.jar

%mvn_file org.apache.tomcat:tomcat-i18n-ko tomcat/tomcat-i18n-ko
%mvn_artifact res/maven/tomcat-i18n-ko.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-ko.jar

%mvn_file org.apache.tomcat:tomcat-i18n-pt-BR tomcat/tomcat-i18n-pt-BR
%mvn_artifact res/maven/tomcat-i18n-pt-BR.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-pt-BR.jar

%mvn_file org.apache.tomcat:tomcat-i18n-ru tomcat/tomcat-i18n-ru
%mvn_artifact res/maven/tomcat-i18n-ru.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-ru.jar

%mvn_file org.apache.tomcat:tomcat-i18n-zh-CN tomcat/tomcat-i18n-zh-CN
%mvn_artifact res/maven/tomcat-i18n-zh-CN.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-i18n-zh-CN.jar

%mvn_file org.apache.tomcat:tomcat-jasper-el tomcat/jasper-el
%mvn_artifact res/maven/tomcat-jasper-el.pom ${RPM_BUILD_ROOT}%{libdir}/jasper-el.jar

%mvn_file org.apache.tomcat:tomcat-jasper tomcat/jasper
%mvn_artifact res/maven/tomcat-jasper.pom ${RPM_BUILD_ROOT}%{libdir}/jasper.jar

%mvn_file org.apache.tomcat:tomcat-jaspic-api tomcat/jaspic-api
%mvn_artifact res/maven/tomcat-jaspic-api.pom ${RPM_BUILD_ROOT}%{libdir}/jaspic-api.jar

%mvn_file org.apache.tomcat:tomcat-jdbc tomcat/tomcat-jdbc
%mvn_artifact res/maven/tomcat-jdbc.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-jdbc.jar

%mvn_file org.apache.tomcat:tomcat-jni tomcat/tomcat-jni
%mvn_artifact res/maven/tomcat-jni.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-jni.jar

%mvn_file org.apache.tomcat:tomcat-juli tomcat/tomcat-juli
%mvn_artifact res/maven/tomcat-juli.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-juli.jar

%mvn_file org.apache.tomcat:tomcat-ssi tomcat/catalina-ssi
%mvn_artifact res/maven/tomcat-ssi.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-ssi.jar

%mvn_file org.apache.tomcat:tomcat-storeconfig tomcat/catalina-storeconfig
%mvn_artifact res/maven/tomcat-storeconfig.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-storeconfig.jar

%mvn_file org.apache.tomcat:tomcat-tribes tomcat/catalina-tribes
%mvn_artifact res/maven/tomcat-tribes.pom ${RPM_BUILD_ROOT}%{libdir}/catalina-tribes.jar

%mvn_file org.apache.tomcat:tomcat-util-scan tomcat/tomcat-util-scan
%mvn_artifact res/maven/tomcat-util-scan.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-util-scan.jar

%mvn_file org.apache.tomcat:tomcat-util tomcat/tomcat-util
%mvn_artifact res/maven/tomcat-util.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-util.jar

%mvn_file org.apache.tomcat:tomcat-websocket-api tomcat/websocket-api
%mvn_artifact res/maven/tomcat-websocket-api.pom ${RPM_BUILD_ROOT}%{libdir}/websocket-api.jar

%mvn_file org.apache.tomcat:tomcat-websocket tomcat/tomcat-websocket
%mvn_artifact res/maven/tomcat-websocket.pom ${RPM_BUILD_ROOT}%{libdir}/tomcat-websocket.jar

%mvn_file org.apache.tomcat:tomcat tomcat/tomcat
%mvn_artifact res/maven/tomcat.pom

%mvn_install

%pre
# add the tomcat user and group
getent group tomcat >/dev/null || %{_sbindir}/groupadd -f -g %{tcuid} -r tomcat
if ! getent passwd tomcat >/dev/null ; then
    if ! getent passwd %{tcuid} >/dev/null ; then
        %{_sbindir}/useradd -r -u %{tcuid} -g tomcat -d %{homedir} -s /sbin/nologin -c "Apache Tomcat" tomcat
        # Tomcat uses a reserved ID, so there should never be an else
    fi
fi
exit 0

%post
# install but don't activate
%systemd_post tomcat.service

%post jsp-%{jspspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/jsp.jar jsp \
    %{_javadir}/tomcat-jsp-%{jspspec}-api.jar 20200

%post servlet-%{servletspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/servlet.jar servlet \
    %{_javadir}/tomcat-servlet-%{servletspec}-api.jar 30000

%post el-%{elspec}-api
%{_sbindir}/update-alternatives --install %{_javadir}/elspec.jar elspec \
   %{_javadir}/tomcat-el-%{elspec}-api.jar 20300

%preun
# clean tempdir and workdir on removal or upgrade
%{__rm} -rf %{workdir}/* %{tempdir}/*
%systemd_preun tomcat.service

%postun
%systemd_postun_with_restart tomcat.service

%postun jsp-%{jspspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove jsp \
        %{_javadir}/tomcat-jsp-%{jspspec}-api.jar
fi

%postun servlet-%{servletspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove servlet \
        %{_javadir}/tomcat-servlet-%{servletspec}-api.jar
fi

%postun el-%{elspec}-api
if [ "$1" = "0" ]; then
    %{_sbindir}/update-alternatives --remove elspec \
        %{_javadir}/tomcat-el-%{elspec}-api.jar
fi

%files
%defattr(0664,root,tomcat,0755)
%doc {LICENSE,NOTICE,RELEASE*}
%attr(0755,root,root) %{_bindir}/tomcat-digest
%attr(0755,root,root) %{_bindir}/tomcat-tool-wrapper
%attr(0755,root,root) %{_sbindir}/tomcat
%attr(0644,root,root) %{_unitdir}/tomcat.service
%attr(0644,root,root) %{_unitdir}/tomcat@.service
%attr(0755,root,root) %dir %{_libexecdir}/tomcat
%attr(0755,root,root) %dir %{_localstatedir}/lib/tomcats
%attr(0644,root,root) %{_libexecdir}/tomcat/functions
%attr(0755,root,root) %{_libexecdir}/tomcat/preamble
%attr(0755,root,root) %{_libexecdir}/tomcat/server
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/tomcat
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/tomcat.disabled
%attr(0755,root,tomcat) %dir %{basedir}
%attr(0755,root,tomcat) %dir %{confdir}

%defattr(0664,tomcat,root,0770)
%attr(0770,tomcat,root) %dir %{logdir}

%defattr(0664,root,tomcat,0770)
%attr(0770,root,tomcat) %dir %{cachedir}
%attr(0770,root,tomcat) %dir %{tempdir}
%attr(0770,root,tomcat) %dir %{workdir}

%defattr(0644,root,tomcat,0775)
%attr(0775,root,tomcat) %dir %{appdir}
%attr(0775,root,tomcat) %dir %{confdir}/Catalina
%attr(0775,root,tomcat) %dir %{confdir}/Catalina/localhost
%attr(0755,root,tomcat) %dir %{confdir}/conf.d
%{confdir}/conf.d/README
%{confdir}/conf.d/java-9-start-up-parameters.conf
%config(noreplace) %{confdir}/tomcat.conf
%config(noreplace) %{confdir}/*.policy
%config(noreplace) %{confdir}/*.properties
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{confdir}/server.xml
%attr(0640,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%attr(0664,root,tomcat) %{confdir}/tomcat-users.xsd
%attr(0664,root,tomcat) %config(noreplace) %{confdir}/jaspic-providers.xml
%attr(0664,root,tomcat) %{confdir}/jaspic-providers.xsd
%config(noreplace) %{confdir}/web.xml
%dir %{homedir}
%{bindir}/bootstrap.jar
%{bindir}/catalina-tasks.xml
%{homedir}/lib
%{homedir}/temp
%{homedir}/webapps
%{homedir}/work
%{homedir}/logs
%{homedir}/conf

%files admin-webapps
%defattr(0664,root,tomcat,0755)
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%{appdir}/docs

%files lib -f .mfiles
%dir %{libdir}
%{libdir}/*.jar
%{_javadir}/*.jar
%{bindir}/tomcat-juli.jar
%exclude %{libdir}/tomcat-el-%{elspec}-api.jar
%exclude %{libdir}/tomcat-servlet-%{servletspec}*.jar
%exclude %{libdir}/tomcat-jsp-%{jspspec}*.jar
%exclude %{_javadir}/tomcat-servlet-%{servletspec}*.jar
%exclude %{_javadir}/tomcat-el-%{elspec}-api.jar
%exclude %{_javadir}/tomcat-jsp-%{jspspec}*.jar
%exclude %{_javadir}/tomcat-servlet-api.jar
%exclude %{_javadir}/tomcat-el-api.jar
%exclude %{_javadir}/tomcat-jsp-api.jar
%exclude %{_jnidir}/*

%files jsp-%{jspspec}-api -f .mfiles-tomcat-jsp-api
%{_javadir}/tomcat-jsp-%{jspspec}*.jar
%{libdir}/tomcat-jsp-%{jspspec}*.jar
%{_javadir}/tomcat-jsp-api.jar

%files servlet-%{servletspec}-api -f .mfiles-tomcat-servlet-api
%doc LICENSE
%{_javadir}/tomcat-servlet-%{servletspec}*.jar
%{libdir}/tomcat-servlet-%{servletspec}*.jar
%{_javadir}/tomcat-servlet-api.jar

%files el-%{elspec}-api -f .mfiles-tomcat-el-api
%doc LICENSE
%{_javadir}/tomcat-el-%{elspec}-api.jar
%{libdir}/tomcat-el-%{elspec}-api.jar
%{_javadir}/tomcat-el-api.jar

%files webapps
%defattr(0644,tomcat,tomcat,0755)
%{appdir}/ROOT

%changelog
* Mon Aug 18 2025 Adam Krajcik <akrajcik@redhat.com> - 1:9.0.87-5.el10_0.3
- Resolves: RHEL-102187
  tomcat: http/2 "MadeYouReset" DoS attack through HTTP/2 control frames (CVE-2025-48989)

* Wed Aug 13 2025 Adam Krajcik <akrajcik@redhat.com> - 1:9.0.87-5.el10_0.2
- Resolves: RHEL-108484
  tomcat: Apache Commons FileUpload DOS via part headers (CVE-2025-48976)
- Resolves: RHEL-108492
  tomcat: Dos in multipart upload (CVE-2025-48988)
- Resolves: RHEL-108500
  tomcat: Security constraint bypass for pre/post-resources (CVE-2025-49125)
- Resolves: RHEL-108508
  tomcat: Denial of service (CVE-2025-52434)
- Resolves: RHEL-108520
  tomcat: Denial of service (CVE-2025-52520)
- Resolves: RHEL-108516
  tomcat: Denial of service (CVE-2025-53506)

* Mon May 26 2025 Adam Krajcik <akrajcik@redhat.com> - 1:9.0.87-5.el10_0.1
- Resolves: RHEL-91748
  tomcat: DoS via malformed HTTP/2 PRIORITY_UPDATE frame (CVE-2025-31650)
- Resolves: RHEL-94959
  tomcat: Incomplete fix for CVE-2024-50379 - RCE due to TOCTOU issue in JSP compilation (CVE-2024-56337)

* Mon Apr 14 2025 Adam Krajcik <akrajcik@redhat.com> - 1:9.0.87-5
- Resolves: RHEL-82927
  tomcat: Potential RCE and/or information disclosure and/or information corruption with partial PUT (CVE-2025-24813)

* Thu Feb 13 2025 Joe Orton <jorton@redhat.com> - 1:9.0.87-4
- add Obsoletes to aid upgrade path from tomcat-9.x
  Resolves: RHEL-79313

* Mon Feb 03 2025 Adam Krajcik <akrajcik@redhat.com> - 1:9.0.87-3
- Resolves: RHEL-77325 Missing conflicts in spec file

* Fri Jan 24 2025 Adam Krajcik <akrajcik@redhat.com> - 1:9.0.87-2
- Initial commit on c10s
  Resolves: RHEL-69841
- tomcat: RCE due to TOCTOU issue in JSP compilation (CVE-2024-50379)
