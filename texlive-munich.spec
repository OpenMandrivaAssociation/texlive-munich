# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/munich
# catalog-date 2007-03-10 12:18:05 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-munich
Version:	20070310
Release:	4
Summary:	An alternative authordate bibliography style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/munich
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/munich.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/munich.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070310-2
+ Revision: 754234
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070310-1
+ Revision: 719088
- texlive-munich
- texlive-munich
- texlive-munich
- texlive-munich

