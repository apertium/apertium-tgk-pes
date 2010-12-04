#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy;


sys.stdin  = codecs.getreader('utf-8')(sys.stdin);
sys.stdout = codecs.getwriter('utf-8')(sys.stdout);
sys.stderr = codecs.getwriter('utf-8')(sys.stderr);

printing = 0;
in_table = 0;

def sym_to_tag(s): #{
	t = '<'.join(s.split('<')[1:]);
	
	return t.replace('"/><s n="', '.').replace('"/>', '').replace('s n="', '').strip();
#}

for line in sys.stdin.read().split('\n'): #{
	if line.count('"unchecked"') > 0: #{
		printing = 1;
	#}

	if line.count('</section>') > 0: #{
		printing = 0;
		if in_table == 1: #{
			print '|}';
			in_table = 0;
		#}
	#}

	if line.count('<e') > 0 and printing == 1: #{
		print '|-';
		line = line.replace('<e><p><l>', '').replace('</r></p></e>', '');
		row = line.split('</l><r>');
		tglem = row[0].split('<')[0];
		falem = row[1].split('<')[0];
		tgtags = sym_to_tag(row[0]);
		fatags = sym_to_tag(row[1]);
		print '| ' +  tglem + '|| <code>' + tgtags + '</code> || ' + falem + ' || <code>' + fatags + '</code>';
		
	#}

	if line.count('UNCHECKED') > 0: #{
		if in_table == 1: #{
			print '|}';
			in_table = 0;
		#}
		print line.replace('<!--', '==').replace('-->', '==').strip();
		print '{|';
		print '! Tajik !! Tajik tags !! Iranian Persian !! Iranian Persian tags';
		in_table = 1;
	#}
	
#}
