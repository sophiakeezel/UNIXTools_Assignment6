#!/usr/bin/perl

use strict;
use warnings;
use File::Find;

# declare variables for command line arguments
my $directory = $ARGV[0];
my $first = $ARGV[1];
my $second = $ARGV[2];

# search through the directory by calling dirLoop function
find(\&dirLoop, $directory);

# if is a file in the directory, replace $second ending with the $first
sub dirLoop {
        
        if (-f) {
            (my $i = $_) =~ s/$first/$second/g;
            rename($_, $i); 
        }
}

    
    


