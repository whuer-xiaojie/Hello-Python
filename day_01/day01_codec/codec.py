#!/usr/bin/python3
# -*- coding: utf-8 -*-

#ascii code test
s='abcdef'
print('the number of \'%s\' is:'%s,len(s))
s='A'
print('the ascii of \'%s\' is:'%s,ord(s))

#utf-8 code test
s='代泽杨'
print('the chinese of \'%s\' lenth is:'%s,len(s))


last_year_score=int(input('please input your last year score:'))
this_year_score=int(input('please input you this year score:'))
if this_year_score >last_year_score:
    print('your score is batter than last year has %.2f%% higher'%((this_year_score-last_year_score)/this_year_score*100))
elif this_year_score<last_year_score:
    print('your score is worse than last year has %.2f%% lower'%((last_year_score-this_year_score)/this_year_score*100))
else:
    print('your score is same as last year')