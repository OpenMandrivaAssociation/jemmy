# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

# Install time macros
%global target_jar build/%{name}.jar
%global target_javadoc build/javadoc/*


Name:           jemmy
Version:        2.3.0.0
Release:        4
Summary:        Java UI testing library

Group:          Development/Java
License:        CDDL
URL:            https://jemmy.dev.java.net

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#
# svn export https://jemmy.dev.java.net/svn/jemmy/trunk/Jemmy2 jemmy-2.3.0.0 --username <username>
# tar -czvf jemmy-2.3.0.0.tar.gz jemmy-2.3.0.0
#
# where <username> is a name of the user registered here: https://www.dev.java.net/servlets/Join
Source0:        jemmy-2.3.0.0.tar.gz

BuildRequires:  ant >= 1.6.5
BuildRequires:  java-devel >= 0:1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  java-rpmbuild >= 0:1.5.32

Requires:       java >= 0:1.6.0
Requires:       jpackage-utils

BuildArch:      noarch

%description
Jemmy is a Java UI testing library. Jemmy represents the most natural way to 
test Java UI - perform the testing right from the Java code. Jemmy is a Java 
library which provides clear and straightforward API to access Java UI. Tests 
are then just java programs, which use the API. Having the tests in Java allows 
to use all the flexibility of high level language to capture test logic and 
also do any other operations needed to be done from test.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
find . -type f -name '*.jar' | xargs -t rm
echo "Please, visit https://jemmy.dev.java.net for more info about Jemmy." > README.txt

%build
%ant jar javadoc

%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__cp -a %{target_jar} %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}
cp -pr %{target_javadoc}/* %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.txt
%{_javadir}/*.jar

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.0.0-2mdv2011.0
+ Revision: 619796
- the mass rebuild of 2010.0 packages

* Fri Sep 25 2009 Jaroslav Tulach <jtulach@mandriva.org> 2.3.0.0-1mdv2010.0
+ Revision: 448735
- First Mandriva package for jemmy (originally part of NetBeans, now separated)
- create jemmy

