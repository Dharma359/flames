# function for remaining letters count
def remaining_letters(f11,f12):
    count = 0
    for x in f11:
        for y in f12:
            if x == y:
                f12.remove(y)
                count = count + 1
                break
        print(f11,f12)
    return f11,f12,count

def flames(total_length, flames_char):
    while len(flames_char)>1:
        rem = total_length%len(flames_char)
        re_char = flames_char[rem-1]
        flames_char.remove(re_char)
    return flames_char


if __name__ == '__main__':
    first_name = input("first_name")
    second_name = input("second_name")
    
    if first_name.isnumeric():
        print("please don't enter digits, run again with characters")
        exit()
    if second_name.isnumeric():
        print("don't enter digits, run again with characters")
        exit()
    
    f1 = list((first_name.replace(" ","")).lower())
    f2 = list((second_name.replace(" ","")).lower())

    
    flames_char = ['f','l','a','m','e','s']
    flames_char1 = ['f','l','a','m','e','s']
    flames_mean = ['friends','lovers','affection','marriage','enemies','sisters']


    r_f1, r_f2, r_count = remaining_letters(f1,f2)
    total_length = (len(r_f1)-r_count)+len(r_f2)
    final_result = flames(total_length, flames_char)
    print(final_result[0])
    print("Your relationship is : ",flames_mean[flames_char1.index(final_result[0])])

