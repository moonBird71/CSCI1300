#!/usr/bin/perl

use Modern::Perl;

use CGI qw/:standard/;

use CGI::Carp qw/fatalsToBrowser/;

#Honor pledge on this page?

print header();
print start_html(
    -style=>{'src'=>'project.css'},
    -title=>'Conseek'
);

#
#Search for cons in the state
#Need textbox/dropbox for input
#Process and display
#

my $search = param("seeker");

if (!$search) {
    print p("Please select a state");

}
elsif ($search eq "AL") {
    print p("Alabama is host to:");
    print p("AnniCon on February 6, 2016 at the Anniston City Meeting Center in Anniston, AL");
}

elsif ($search eq "AK") {
    print p("Alaska does not have any conventions scheduled in 2016");
}

elsif ($search eq "AZ") {
    print p("Arizona is host to:");
    print p ("Taiyou Con on January 15-17, 2016 at the Mesa Convention Center in Mesa, AZ");
}

elsif ($search eq "AR") {
    print p("Arkansas is host to:");
    print p ("AnimeCon Arkansas on April 8-10, 2016 at the Holiday Inn Airport Conference Center in Little Rock, AR");
}

elsif ($search eq "CA") {
    print p("California is host to:");
    print p("Sac-Anime on January 1-3, 2016 at the Sacramento Convention Center in Sacramento, CA");
}

elsif ($search eq "CO") {
    print p("Colorado is host to:");
    print p("Colorado Anime Fest on February 12-14, 2016 in the Renaissance Denver Hotel in Denver, CO");
}
elsif ($search eq "CT") {
    print p("Connecticut is host to:");
    print p("CampAnime on August 26-28, 2016 at the YMCA Camp Woodstock in Woodstock Valley, CT");
}

elsif ($search eq "DE") {
    print p("Delaware does not have any conventions scheduled in 2016");
}

elsif ($search eq "FL") {
    print p("Florida is host to:");
    print p("Tampa Anime Day on January 9, 2016 at the Embassy Suites Tampa-Brandon in Tampa, FL");
}

elsif ($search eq "GA") {
    print p("Georgia is host to:");
    print p("Seishun Con on February 5-7, 2016 at the Marriott Perimeter Center in Atlanta, GA");
}

elsif ($search eq "HI") {
    print p("Hawaii is host to:");
    print p("Kawaii Kon on April 8-10, 2016 at the Hawaii Convention Center in Honoloulu, HI");
}

elsif ($search eq "ID") {
    print p("Idaho is host to:");
    print p("Anime Oasis on May 27-30, 2016 at The Grove Hotel/CenturyLink Arena Boise/Boise Centre in Boise, ID");
}

elsif ($search eq "IL") {
    print p("Illinois is host to:");
    print p("Anime-Zap! on January 8-10, 2016 at the Embassy Suites East Peoria-Hotel & Riverfront Conference Center in East Peoria, IL");
}

elsif ($search eq "IN") {
    print p("Indiana is host to:");
    print p("Anime Crossroads on February 19-21, 2016 at the Wyndham Indianapolis West in Indianapolis, IN");
}

elsif ($search eq "IA") {
    print p("Iowa is host to:");
    print p("AnimeIowa on July 29-31, 2016 at the Marriott Hotel & Conference Center in Coralville, IA");
}

elsif ($search eq "KS") {
    print p("Kansas is host to:");
    print p("Naka-Kon on March 11-13, 2016 at the Overland Park Convention Center in Overland Park, KS");
}

elsif ($search eq "KY") {
    print p("Kentucky is host to:");
    print p("OMG!con on June 10-12, 2016 at the Owensboro Convention Center in Owensboro, KY");
}

elsif ($search eq "LA") {
    print p("Louisiana is host to:");
    print p("LouisiANIME on March 25-27, 2016 at the Marriott at Baton Rouge, LA");
}

elsif ($search eq "ME") {
    print p("Maine is host to:");
    print p("PortConMaine on June 23-26, 2016 at the DoubleTree by Hilton Hotel Portland in South Portland, ME");
}

elsif ($search eq "MD") {
    print p("Maryland is host to:");
    print p("AniMore on January 22-24, 2016 at the Hyatt Regency in Baltimore, MD");
}

elsif ($search eq "MA") {
    print p("Massachusetts is host to:");
    print p("Anime Boston on March 25-27, 2016 at the Hynes Convention Center in Boston, MA");
}

elsif ($search eq "MI") {
    print p("Michigan is host to:");
    print p("Shuto Con on March 18-20, 2016 at the Lansing Convention Center/Radisson Hotel in Lansing, MI");
}

elsif ($search eq "MN") {
    print p("Minnesota is host to:");
    print p("Anime Detour on April 22-24, 2016 at the DoubleTree by Hilton Bloomington Minneapolis South in Bloomington, MN");
}

elsif ($search eq "MS") {
    print p("Mississippi is host to:");
    print p("Anime Blues Winterfest Remix on January 16, 2016 at the Landers Center in Southaven, MS");
}

elsif ($search eq "MO") {
    print p("Missouri is host to:");
    print p("Ahn!Con on January 8-10, 2016 at the Howard Johnson Plaza Kansas City Hotel and Conference Center in Kansas City, MO");
}

elsif ($search eq "MT") {
    print p("Montana does not have any conventions scheduled in 2016");
}

elsif ($search eq "NE") {
    print p("Nebraska does not have any conventions scheduled in 2016");
}

elsif ($search eq "NV") {
    print p("Nevada is host to:");
    print p("Otakon Vegas on January 15-17, 2016 at the Planet Hollywood Resort and Casino in Las Vegas, NV");
}

elsif ($search eq "NH") {
    print p("New Hampshire is host to:");
    print p("Queen City Kamikaze on March 12, 2016 at Manchester Memorial High School in Manchester, NH");
}

elsif ($search eq "NJ") {
    print p("New Jersey is host to:");
    print p("KotoriCon on January 8-9, 2016 at Rowan College at Gloucester County in Sewell, NJ");
}

elsif ($search eq "NM") {
    print p("New Mexico is host to:");
    print p("LAs Cruces Anime Days on January 23-24, 2016 at New Mexico State University, Corbett Center at Las Cruces, NM");
}

elsif ($search eq "NY") {
    print p("New York is host to:");
    print p("Tatsu-Con on July 29-31, 2016 at the Buffalo Niagara Convention Center in Buffalo, NY");
}

elsif ($search eq "NC") {
    print p("North Carolina is host to:");
    print p("Animazement on May 11-13, 2016 at the Raleigh Convention Center at Raleigh, NC");
}

elsif ($search eq "ND") {
    print p("North Dakota does not have any conventions scheduled for 2016");
}

elsif ($search eq "OH") {
    print p("Ohio is host to:");
    print p("Ohayocon on January 15-17, 2016 at the Hyatt Regency Columbus/Greater Columbus Convention Center at Columbus, OH");
}

elsif ($search eq "OK") {
    print p("Oklahoma is host to:");
    print p("Tokyo in Tulsa on July 15-17, 2016 at the Cox Business Center in Tulsa, OK");
}

elsif ($search eq "OR") {
    print p("Oregon is host to:");
    print p("Newcon PDX on January 15-17, 2016 at the DoubleTree by Hilton Portland in Portland, OR");
}

elsif ($search eq "PA") {
    print p("Pennsylvania is host to:");
    print p("Setsucon on January 30-31, 2016 at the Toftrees Golf Resort & Conference Center in State College, PA");
}

elsif ($search eq "RI") {
    print p("Rhode Island is host to:");
    print p("RhodyCon on July 30-31, 2016 at the Dovetail Auction Gallery in Cranston, RI");
}

elsif ($search eq "SC") {
    print p("South Carolina is host to:");
    print p("AgamaCon on March 4-6, 2016 at the Hilton Garden Inn in Aiken, SC");
}

elsif ($search eq "TN") {
    print p("Tennessee is host to:");
    print p("Knoxville Anime Day on January 30, 2016 at the Holiday Inn Knoxville West-Cedar Bluff Rd in Knoxville, TN");
}

elsif ($search eq "TX") {
    print p("Texas is host to:");
    print p("Ikkicon ojn January 1-3, 2016 at the Renaissance Austin Hotel in Austin, TX");
}

elsif ($search eq "UT") {
    print p("Utah is host to:");
    print p("Fannatiku Fest on March 25-26, 2016 at the Dixie Convention Center in Saint George, UT");
}

elsif ($search eq "VT") {
    print p("Vermont is host to:");
    print p("Bakurestu Con on October 28-30, 2016 at Hampton Inn Burlington in Colchester, VT");
}

elsif ($search eq "VA") {
    print p("Virginia is host to:");
    print p("Star City Anime on February 5-7, 2016 at the Holiday Inn Roanoke-Valley View in Roanoke, VA");
}

elsif ($search eq "WA") {
    print p("Washingtion is host to:");
    print p("Sakura-Con on March 25-27, 2016 at the Washington State Convention & Trade Center in Seattle, WA");
}

elsif ($search eq "WV") {
    print p("West Virginia is host to:");
    print p("Tsubasacon on September 30-October 2, 2016 at Big Sandy Superstore Arena in Huntingon, WV");
}

elsif ($search eq "WI") {
    print p("Wisconsin is host to:");
    print p("YourMiniCon-Wisconsin on February 6-7, 2016 at Sheraton Madison Hotel in Madison, WI");
}

elsif ($search eq "WY") {
    print p("Wyoming does not have any conventions scheduled for 2016");
}

print end_html();
