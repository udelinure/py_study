S = "bbbcccdddaaa"
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
line = 1
units = 0
for i in S:
    if widths[ord(i) - ord("a")] + units > 100:
        line += 1
        units = widths[ord(i) - ord("a")]
    else:
        units += widths[ord(i) - ord("a")]
print [line,units]
