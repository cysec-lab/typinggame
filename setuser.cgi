#!/usr/bin/perl -w

$ENV{'HTTP_COOKIE'} =~ /userid\=(\d+)/;
my $userid = $1;
exit unless $userid;

print "Content-Type: text/html\n";
print "\n";
read(STDIN, $data, $ENV{'CONTENT_LENGTH'});

my $dd = "/var/www/typegame-data/${userid}";

if(!-d $dd) {
    mkdir($dd);
}
open(OUT, ">${dd}/profile.txt");
print $$, "\n";
print OUT $data;
close(OUT);
print "OK\n";
print $data;
