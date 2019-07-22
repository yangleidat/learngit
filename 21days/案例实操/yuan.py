r = 16
for i in range(2*r+1):
    ban = (r**2-(r-i)**2)**0.5
    start = round(r-ban)
    mid = round(2*ban)
    if i % 2:
        print('  ' * start +'*'+ '  ' * mid + '*')
    else:
        print('  ' * start +'*'+ '  ' * mid + '*')