codon = input('Input your codon, please:')
codon_tuple = ('UAA', 'UAG', 'UGA')
if codon == 'AUG':
    print ('This codon in the start codon.')
elif codon in codon_tuple:
        print('This is a stop codon.')
else:
    print('This in neither a start nor a stop codon')
