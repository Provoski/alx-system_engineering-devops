#!/usr/bin/env ruby
# Creates a Ruby script that accepts
# one argument and pass it to a regular expression matching method
# The word to match is "School"
#
puts ARGV[0].scan(/hbt{1,4}n/).join
