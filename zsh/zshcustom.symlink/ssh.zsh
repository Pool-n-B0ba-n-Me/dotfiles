# short cut to ssh into remote hosts

alias afs="ssh ruoyul@unix.andrew.cmu.edu"
alias afsx="ssh -X ruoyul@unix.andrew.cmu.edu"
alias shark="ssh ruoyul@shark.ics.cs.cmu.edu"
alias sharkx="ssh -X ruoyul@shark.ics.cs.cmu.edu"

ece()       { ssh ruoyul@ece0"$@".ece.cmu.edu }
ecex()      { ssh -X ruoyul@ece0"$@".ece.cmu.edu }
ghc()       { ssh ruoyul@ghc"$@".ghc.andrew.cmu.edu }
ghcx()      { ssh -X ruoyul@ghc"$@".ghc.andrew.cmu.edu }
