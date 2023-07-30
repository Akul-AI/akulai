#!/usr/bin/perl

use strict;
use warnings;
use Weather::Google;

my $location = shift;

my $weather = Weather::Google->new($location);

print "The weather in $location is currently " . $weather->condition->temp . "F and " . $weather->condition->text . "\n";
