%global tl_name romanbarpagenumber
%global tl_revision 36236

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typesetting roman page numbers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/romanbarpagenumber
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbarpagenumber.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbarpagenumber.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/romanbarpagenumber.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package romanbar allows to typeset roman numbers with bars. This
package allows you to use those roman numbers as page number.

