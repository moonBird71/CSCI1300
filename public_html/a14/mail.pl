#!/usr/bin/perl

use Modern::Perl;
use Mail::Sendmail;

my $mailTo = 'nialiu7@yahoo.com';

my $mailFrom = 'nialiu7@yahoo.com';

my $subjectLine = "Subject";

my $message = "Sample Message!";

my %mail = ( To  => $mailTo,
            From => $mailFrom,
            Subject => $subjectLine,
            Message => $message,
            'Content-Type' => 'text/plain'
            );

if ( sendmail %mail )
{
    print "Successfully sent mail to $mailTo.  Check your box!\n";
}
else
{
    print "Error sending mail: $Mail::Sendmail::error \n";
}

