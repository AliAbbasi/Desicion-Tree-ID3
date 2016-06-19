
It generates ‘Output.dot’ and ‘Testset Report.txt’ files

Output.dot is a file which in 'graphiz' format

--------------------------------------------------------------------------------------------

Input dateset must have this format: (The example dataset)

%  'T:' Identifies the Attribute Title Line

%  'A:' Identifies Training Set Examples

%  'B:' Identifies Test Set Examples

T: ReadBefore, RelatedTopic, HotTopic, InterestedIn, PublishYear, Length, HelpfulDegree, Type, WillRead;

A: no, no, yes, yes, 2010-2015, long, high, journal, no;

A: yes, yes, no, no, after2015, short, high, conferance, no;

A: no, yes, yes, yes, before2010, long, low, conferance, no;

A: no, no, no, yes, after2015, short, high, conferance, yes;

A: yes, yes, no, yes, after2015, long, low, journal, no;

A: yes, no, yes, no, 2010-2015, long, high, conferance, no;

A: yes, yes, no, yes, 2010-2015, long, low, journal, no;

B: no, yes, yes, no, before2010, long, medium, conferance, no;

B: no, no, yes, yes, after2015, long, high, journal, yes;

B: no, no, yes, yes, before2010, short, low, conferance, no;

