Name:		texlive-munich
Version:	15878
Release:	2
Summary:	An alternative authordate bibliography style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/munich
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/munich.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/munich.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Munich BibTeX style is produced with custom-bib, as a
German (and, more generally, Continental European) alternative
to such author-date styles as harvard and oxford.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/munich/munich.bst
%doc %{_texmfdistdir}/doc/latex/munich/README
%doc %{_texmfdistdir}/doc/latex/munich/documenation_munich_Bibtex_style.pdf
%doc %{_texmfdistdir}/doc/latex/munich/documenation_munich_Bibtex_style.tex
%doc %{_texmfdistdir}/doc/latex/munich/example_DB.bib
%doc %{_texmfdistdir}/doc/latex/munich/example_munich_Bibtex_style.pdf
%doc %{_texmfdistdir}/doc/latex/munich/example_munich_Bibtex_style.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
