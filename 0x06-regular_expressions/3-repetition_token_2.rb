#!/usr/bin/env ruby
# Creates a Ruby script that accepts
# one argument and pass it to a regular expression matching method
puts ARGV[0].scan(/hbt{1,1000}n/).join
