from metaflow import FlowSpec, step, batch
from dotenv import load_dotenv
import os


class EnvVarFlow(FlowSpec):
    
    @step
    def start(self):
        self.next(self.read_locally)
        
    @step
    def read_locally(self):
        from elephant.utils import run
        run()
        secret = os.getenv("AWS_SECRET")
        print(f"secret message: {secret} " ,
               "from local environment")
        self.next(self.end)
   
    @step
    def end(self):
        pass
        
if __name__ == "__main__":
    load_dotenv()
    EnvVarFlow()