import re

m = re.findall("abc", "aaaaabcccabcc")
print m

m = re.findall("\d", "abc1ab2c")
print m

m = re.findall("\d\d\d\d", "123abc1234abc")
print m

m = re.findall(r"<div>(.*)</div>", "<div>hello</div>")
print m

m = re.findall(r"<div>(.*)</div>", "<div>hello</div><div>world</div>")
print m

m = re.findall(r"<div>(.*?)</div>", "<div>hello</div><div>world</div>")
print m

