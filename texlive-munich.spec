# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/munich
# catalog-date 2007-03-10 12:18:05 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-munich
Version:	20070310
Release:	1
Summary:	An alternative authordate bibliography style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/munich
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/munich.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/munich.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The Munich BibTeX style is produced with custom-bib, as a
German (and, more generally, Continental European) alternative
to such author-date styles as harvard and oxford.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
