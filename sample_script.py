from csv import writer
import argparse

#Read in the hyperparameters through the command line arguments
parser = argparse.ArgumentParser(description='Script for Colab Tutorial')
parser.add_argument('--hyperparameter1', type=int, default=498)
parser.add_argument('--hyperparameter2', type=int, default=2)
parser.add_argument('--results_file', type=str, default= None)

args = parser.parse_args()

hyperparameter1 = args.hyperparameter1
hyperparameter2 = args.hyperparameter2
results_file = args.results_file

#Generate the result using these hyperparameters
#In most cases, this would be something more complicated, like training a model and computing its accuracy on a test set
result = hyperparameter1 + hyperparameter2

#Print this result in the notebook
print(result)

#Export the result to a csv file if a file was specified
if results_file is not None:

  #Construct a list containing the data to append to the csv file
  row_to_add = [hyperparameter1, hyperparameter2, result]
                  
  #Print this data to the csv file
  with open(results_file, 'a') as f_object:
      writer_object = writer(f_object)
      writer_object.writerow(row_to_add)
      f_object.close()
