"""Phone number validation:
You can validate the number by length,
mobile operator's prefix ("093", "067" etc.),
allow number to be prefixed with "8" or country code (e.g. "+380" or "00380")."""

"""x = False
while x == False:
    if len(num) <= 13:
        if num.startswith('380') or num.startswith('+380') or num.startswith('00380'):
            print('all good')
            x = True
        else:
            print('wrong beginning')
            x = False
    else:
        print('wrong length')
        x = False"""
list_of_codes = ['067', '069']
num = '+380675968763'
reversed_num = num[::-1];                       print('reversed_num', reversed_num)
reversed_num_no_prefix = reversed_num[:10];     print('reversed_num_no_prefix', reversed_num_no_prefix)
num_no_prefix = reversed_num_no_prefix[::-1];   print('num_no_prefix', num_no_prefix)
operator_code = num_no_prefix[0:3];             print('operator_code', operator_code)
if operator_code in list_of_codes:
    print('all good')
else:
    print('wrong operator')



