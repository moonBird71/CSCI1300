#!/usr/bin/perl

use Modern::Perl;
use Mail::Sendmail;

use CGI qw/:standard/;

use CGI::Carp qw/fatalsToBrowser/;

print header(), start_html();
#-title=>''
#-style=>{'src'=>'my.css'}
#);

#something else here - block?

#use param() to declare variables
my $from = param ("from");
my $to = param ("to");
my $topic = param ("topic");
my $message = param ("message");

my %mail = ( To => $to,
		From => $from,
		Subject => $topic,
		Message => $message,
		'Content-Type' => 'text/plain'
	);
#need some way to produce error messages if a field not filled

if (sendmail %mail)
{
	print p("Congratulations, your mail was sent!");
}
else
{
if ($from ~~ /^\s*$/ )
{
	print p("Please enter your e-mail address!");
}

if ($to ~~ /^\s*$/ )
{
	print p("Please enter the recipient's e-mail address!");
}

if ($topic ~~ /^\s*$/ )
{
	print p("Please enter a subject!");
}

if ($message ~~ /^\s*$/ )
{
	print p("Please enter a message!");
}
	print a ( 
	{
		-href=>'javascript:history.back();'
	},
	"Go back and fill all fields");
}
#need to set a "you-have-sent-your-message" message
#have a go back button?

print end_html();
