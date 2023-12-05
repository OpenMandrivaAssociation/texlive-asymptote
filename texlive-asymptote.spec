Name:		texlive-asymptote
Version:	67300
Release:	1
Summary:	2D and 3D TeX-Aware Vector Graphics Language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/asymptote
License:	lgpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asymptote.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Asymptote is a powerful descriptive vector graphics language
for technical drawing, inspired by MetaPost but with an
improved C++-like syntax. Asymptote provides for figures the
same high-quality level of typesetting that LaTeX does for
scientific text.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/tex/latex/asymptote
%{_texmfdistdir}/tex/context/third/asymptote
%{_texmfdistdir}/asymptote
%doc %{_texmfdistdir}/doc/asymptote
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/info/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
