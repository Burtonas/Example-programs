
def arithmetic_arranger(problems, reveal):

    # Checking if we have no more than 5 problems to solve
    if len(problems) > 0 and len(problems) <6:         
        
        first_num_value = []
        operator = []
        second_num_value = []
        result_value = []
        final_col_width = []

        for item in problems:
            chunk = item.split()
            col_width = 0

            # Checking if input value is a number
            for piece in chunk:
                if len(piece) > col_width:
                    col_width = len(piece)
            try:
                temp_1 = int(chunk[0])
                temp_2 = int(chunk[2])
            except:
                print('Error: Numbers must only contain digits.')
                break

            # Checking if digit is not larger than 4 chars
            if len(chunk[0]) > 4 or len(chunk[2]) > 4:
                print('Error: Numbers cannot be more than four digits.')
                break
            else:
            
                # Checking if operator is either + or - (others are not allowed)
                if chunk[1] == "+":
                    result = int(chunk[0]) + int(chunk[2])
                    result_value.append(result)
                elif chunk[1] == "-":
                    result = int(chunk[0]) - int(chunk[2])
                    result_value.append(result)
                else:
                    print('Error: Operator must be '+' or '-'.')
                
                position_0 = str(chunk[0])
                position_1 = str(chunk[1])
                position_2 = str(chunk[2])

                first_num_value.append(position_0)
                operator.append(position_1)
                second_num_value.append(position_2)
                final_col_width.append(col_width)
                
                # Displaying problem
                print('{0:>{length}}'.format(position_0, length = int(col_width) + 2))
                print('{operator}{0:>{length}}'.format(position_2, operator = position_1, length = int(col_width) + 1))
                print('{:-^{length}s}'.format('-', length = int(col_width) + 2))

                # Displaying the result if we have been asked for it 
            if reveal == True:
                print('{0:>{length}}'.format(result, length = int(col_width) + 2))
            else:
                continue

    else:
        print('Error: Too many problems.')
   
    return problems