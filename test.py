from PIL import Image
first = True
if first:
    print('hi ma')
    first = False
if not first:
    print('hi dad')

def test(firstpass):
    if firstpass:
        print('hi')
        firstpass = False

for i in range(1):
    test(True)