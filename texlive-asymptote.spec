Name:		texlive-asymptote
Version:	64491
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
%{_texmfdistdir}/texmf-dist/tex/latex/asymptote
%{_texmfdistdir}/texmf-dist/tex/context/third/asymptote
%{_texmfdistdir}/texmf-dist/asymptote
%doc %{_texmfdistdir}/texmf-dist/doc/asymptote
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/xasy.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/xasy.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/asy.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/asy.1
%doc %{_texmfdistdir}/texmf-dist/doc/info
%doc %{_texmfdistdir}/texmf-dist/doc/info/asymptote.info
%doc %{_texmfdistdir}/texmf-dist/doc/info/asy-faq.info

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
