#!/usr/bin/perl

use LWP::UserAgent;

sub fetch_stock_price {
    my $ticker = shift;

    # Get stock information from Google Finance
    my $url = "https://www.google.com/finance?q=$ticker";
    my $ua = LWP::UserAgent->new;
    my $response = $ua->get($url);

    # Check if request was successful
    if ($response->is_success) {
        my $html = $response->decoded_content;

        # Extract the stock price
        if ($html =~ /ref_.*_l">(.*?)<\/span>/i) {
            return "The current stock price for $ticker is $1.";
        } else {
            return "Unable to find stock price for $ticker.";
        }
    } else {
        return "Error fetching stock price for $ticker: " . $response->status_line;
    }
}

sub handle {
    my $command = shift;
    if ($command =~ /stock price for (.*)/i) {
        return fetch_stock_price($1);
    }
    return "Invalid command.";
}

1;
