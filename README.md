# Random Name Generator

A script to generate a bunch random, pronounceable names


## Usage

    python random_name.py [Limit] [Max-Length] [Min-Length] [Use-Letters]
	
####Limit
Limit is the maximum number of names to generate, Default is 10
	
####Max-Length
The maxiumm length of a name, Default is `2`
	
####Min-Length
The minimum length of a name, Default is `Max-Length` when available, `2` otherwise
	
####Use-Letters or Avoid-Letters
A string of letters from which to create names from, Default: All of the alphabet `a-z`
Note: You can avoid letters instead of using them by adding a `-` at the begining


## Example output

When called with
    
    python random_name.py 5 7 7 -xyzfgd
    
It may give

    Limit: 5
    Max-Length: 7
    Min-Length: 7
    Vowels used: aeiou
    Consonants used: bchjklmnpqrstvw

    polesub
    wilulaw
    qavuwom
    natenav
    uwacuqe

## License
[CC-BY](http://creativecommons.org/licenses/by/3.0/).
