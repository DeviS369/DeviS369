"""
Program 1 : Write the python program using Function to which will do the following -
          a , The function will create a text file with current timestamp
          b , The content should have the content of the current timestamp

Program 2 : Write anotoher funtion to read a text file .The function will 
take the name of the text file and displays the content the text file into the console.  
"""
from datetime import datetime
def time_stamp():
  current_timestamp = datetime.now()
  current_timestamp =current_timestamp.strftime('%Y-%m-%d_%H.%M.%S')
  with open(f'timestamp_{current_timestamp}.txt','w') as w_file:
      w_file.write(current_timestamp)

def read_file():
    with open('timestamp_2024-07-16_19.27.47.txt','r') as r_file:
        content = r_file.read()
        print(content)
if __name__ == '__main__':
   time_stamp()
   read_file()


