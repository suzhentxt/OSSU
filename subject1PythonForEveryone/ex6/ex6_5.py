text = "X-DSPAM-Confidence:    0.8475"
bg = text.find('.')
n = float(text[bg-1:])
print('%g' % n)