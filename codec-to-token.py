from datasets import load_dataset
import json


class Vocabulary:
    """Class to map codes from huggingface dataset to tokens in Llama 3-8B token"""

    def __init__(self):
        self.stoi = {}
        self.itos = {}
    
    def build_vocabulary(self, parquet_files, tokenizer_file="tokenizer.json"):
        '''
        creates the vocabulary from the Llama 3 tokenizer and hugging face dataset
        Args:
            tokenizer_file(str): file downloaded from Llama 3(8B) which contains the vocabulary for the model
            parquet_files(list): director with the dataset from hugging face in parquet format

        '''
        # Open the JSON file
        with open(tokenizer_file, 'r') as file:
            # Load the JSON data
            data = json.load(file)
        
        llama_stoi = data['model']['vocab']
        llama_itos = {value:key for key,value in llama_stoi.items()}

        #load hugging face data
        dataset = load_dataset('parquet', data_files=parquet_files)
        vocabulary = set()

        for sent in dataset["train"]["txt"]:
            for word in sent.split():
                vocabulary.add(word)
        
        self.itos = {value:llama_itos[int(value)] for value in vocabulary}
        self.stoi = {value:key for key,value in self.itos.items()}
    
    def save(self, file_path):
        '''
        saves the the int to string(llama token) to a json file to be loaded later
        Args:
            file_path(str): file where dict will be saved

        '''
        with open(file_path, "w") as file:
            json.dump(self.itos, file, indent=4)


if __name__ == "__main__":
    test_dir = [f"dataset/default/partial-train/000{i}.parquet" for i in range(10)]
    vocab = Vocabulary()

    vocab.build_vocabulary(test_dir)
    vocab.save("snac-to-llama.json")
        
        

        