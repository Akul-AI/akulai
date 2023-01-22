use strict;
use warnings;
use Cwd qw(chdir);
use File::Copy qw(move);
use File::Path qw(rmtree);
use LWP::Simple qw(getstore);
use Archive::Extract;
use File::Basename qw(dirname);

chdir("..");

my $repo_url = "https://github.com/Akul-AI/akulai-plugins";
my $subdir = "plugins";

system("git submodule add $repo_url");
system("git submodule update --init --recursive");

move("akulai-plugins/$subdir", "akulai/");

rmtree("akulai-plugins");

my $vosk_url = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip";
getstore($vosk_url, "vosk-model-small-en-us-0.15.zip");

my $ae = Archive::Extract->new(archive => "vosk-model-small-en-us-0.15.zip");
$ae->extract(to => "akulai");

rename("akulai/vosk-model-small-en-us-0.15", "akulai/vosk_model");

unlink("vosk-model-small-en-us-0.15.zip");

my $current_os = $^O;

if ($current_os eq "MSWin32") {
# Download and install Node.js
my $node_url = "https://nodejs.org/dist/latest-version/node-x64.msi";
getstore($node_url, "node-x64.msi");
system("msiexec /i node-x64.msi /quiet");

} elsif ($current_os eq "linux") {
# Install Node.js
system("sudo apt-get update");
system("sudo apt-get install -y nodejs");
