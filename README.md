-	My code written at python version 2.7.11, in order to compile the code use below command:
-	Python src.py Input_dataset.txt
It generates ‘Output.dot’ and ‘Testset Report.txt’ files

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
A: no, yes, yes, yes, before2010, short, low, journal, yes;
A: no, yes, no, yes, after2015, long, high, conferance, yes;
A: no, no, yes, no, after2015, short, low, conferance, no;
A: no, yes, yes, no, 2010-2015, short, low, conferance, yes;
A: no, no, no, no, before2010, short, high, conferance, yes;
A: yes, no, yes, no, before2010, long, low, journal, no;
A: yes, no, no, yes, after2015, short, high, conferance, no;
A: yes, yes, no, no, after2015, long, medium, journal, no;
A: yes, no, no, yes, before2010, long, high, conferance, no;
A: no, yes, yes, yes, before2010, long, high, journal, yes;
A: no, yes, no, no, 2010-2015, long, high, journal, yes;
A: yes, yes, yes, yes, after2015, short, medium, conferance, yes;
A: yes, yes, no, no, before2010, short, medium, conferance, no;
A: yes, yes, yes, no, after2015, short, medium, conferance, no;
A: no, no, no, yes, 2010-2015, short, low, journal, no;
A: no, yes, no, no, after2015, short, high, journal, yes;
A: no, yes, yes, yes, before2010, long, low, journal, yes;
A: no, yes, yes, yes, 2010-2015, long, low, conferance, yes;
A: no, no, no, yes, before2010, long, medium, journal, no;
A: yes, yes, no, yes, before2010, long, low, journal, no;
A: yes, no, no, yes, 2010-2015, short, medium, conferance, no;
A: no, yes, no, no, 2010-2015, long, medium, journal, no;
A: yes, no, no, no, 2010-2015, short, low, conferance, no;
A: no, no, no, no, before2010, short, high, conferance, no;
A: yes, no, no, no, after2015, short, low, conferance, no;
A: yes, yes, yes, yes, before2010, short, medium, conferance, yes;
A: yes, no, yes, yes, before2010, short, high, journal, yes;
A: no, no, yes, no, 2010-2015, short, high, journal, no;
A: yes, no, yes, yes, before2010, long, low, journal, no;
A: yes, yes, no, no, before2010, short, medium, journal, no;
A: no, yes, no, no, before2010, short, low, journal, no;
A: no, yes, no, no, before2010, short, high, conferance, yes;
A: no, no, no, yes, before2010, short, low, journal, no;
A: no, yes, no, yes, before2010, long, medium, conferance, no;
A: no, yes, yes, yes, 2010-2015, long, medium, conferance, yes;
A: yes, no, yes, no, after2015, short, medium, journal, no;
A: no, no, no, no, after2015, long, low, journal, no;
A: no, yes, no, no, 2010-2015, long, medium, journal, no;
A: yes, no, no, yes, after2015, long, high, conferance, no;
A: no, yes, yes, no, before2010, short, medium, journal, no;
A: yes, no, no, yes, before2010, short, high, conferance, no;

B: no, yes, yes, no, before2010, long, medium, conferance, no;
B: no, no, yes, yes, after2015, long, high, journal, yes;
B: no, no, yes, yes, before2010, short, low, conferance, no;
B: no, yes, yes, yes, before2010, long, medium, journal, yes;
B: no, yes, no, no, 2010-2015, short, low, journal, no;
B: yes, no, no, no, 2010-2015, long, medium, conferance, no;
B: yes, yes, no, yes, before2010, long, medium, journal, no;
B: no, no, no, no, after2015, long, low, conferance, no;
B: yes, no, yes, no, after2015, short, low, conferance, no;
B: yes, no, no, yes, after2015, long, low, conferance, no;
