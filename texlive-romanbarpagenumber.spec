Name:		texlive-romanbarpagenumber
Version:	36236
Release:	1
Summary:	Typesetting roman page numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/romanbarpagenumber
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbarpagenumber.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbarpagenumber.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbarpagenumber.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package romanbar allows to typeset roman numbers with bars.
This package allows you to use those roman numbers as page
number.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/romanbarpagenumber
%{_texmfdistdir}/tex/latex/romanbarpagenumber
%doc %{_texmfdistdir}/doc/latex/romanbarpagenumber

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
