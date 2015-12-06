#!/usr/bin/env python
#Working with string


name = "AAA aaa BBB bbb CCC ccc"
n    = str("ABC abc");
con_cat = name + n;
con_cat2 = " %s ZZZ %s" % (name , n) ;

print (name);
print(n);
print(con_cat);
print(con_cat2);
print( " Name in lower = %s " % name.lower());
print( " Name in upper = %s " % name.upper());
print( " Name in replace AAA with ZZZ YYY  = %s " % name.replace('AAA', 'ZZZ YYY'));
