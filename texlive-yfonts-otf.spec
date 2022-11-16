Name:		texlive-yfonts-otf
Version:	64075
Release:	1
Summary:	OpenType version of the Old German fonts designed by Yannis Haralambous
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yfonts-otf
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an OpenType version of the Old German fonts yfrak,
ygoth, yswab designed by Yannis Haralambous in Metafont. The
OpenType features make it easier to deal with the long/round s
and with older forms of umlauts (small e over the letter). A
style file yfonts-otf.sty is provided as a replacement, for
LuaLaTeX and XeLaTeX, of yfonts.sty or oldgerm.sty.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/yfonts-otf
%{_texmfdistdir}/fonts/opentype/public/yfonts-otf
%doc %{_texmfdistdir}/doc/fonts/yfonts-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
