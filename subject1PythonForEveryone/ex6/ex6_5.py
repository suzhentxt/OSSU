<<<<<<< HEAD
text = "X-DSPAM-Confidence:    0.8475"
bg = text.find('.')
n = float(text[bg-1:])
=======
text = "X-DSPAM-Confidence:    0.8475"
bg = text.find('.')
n = float(text[bg-1:])
>>>>>>> c86c51b107c58c35667363688dc1ba559b89806d
print('%g' % n)