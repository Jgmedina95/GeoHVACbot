import pickle
from pydantic import BaseModel
from typing import List,Any,Optional,Dict,Tuple,Union
from openai.embeddings_utils import get_embedding, cosine_similarity

class HVACsystem(BaseModel):

    heat_load: int = 0 #BTU/hr
    size_per_pump:int  = 12.000 #tons
    number_of_pumps:int = 1
    pump_type:str = "water-water"
    pump_efficiency:float = 0.75
    pump_power:float = 0.746 #kW
    bore_required:float = 0.0 #ft
    bore_diameter:float = 0.0 #in
    bore_depth:float = 0.0 #ft
    bore_cost:float = 0.0 #USD
    bore_material:str = "HDPE"
    bore_spacing:float = 0.0 #ft

DocKey = Any

class Doc(BaseModel):
    docname: str
    citation: str
    dockey: DocKey


class Text(BaseModel):
    text: str
    name: str
    doc: Doc
    embeddings: Optional[List[float]] = None
    similarity: Optional[float] = None

    #@validator("embeddings")
    #def check_embeddings(cls, v):
    #    if v is None:

    def calculate_embeddings(self, model="text-embedding-ada-002"):
        if self.embeddings is None:
            self.embeddings = get_embedding(self.text, model)
        return self.embeddings

def search_texts(texts: List[Text], product_description, n=3, pprint=False):
    product_embedding = get_embedding(
        product_description,
        "text-embedding-ada-002"
    )
    for text in texts:
        text.similarity = cosine_similarity(text.embeddings, product_embedding)

    results = sorted(texts, key=lambda x: x.similarity, reverse=True)[:n]

    if pprint:
        for r in results:
            print(r.text[:200])
            print()
    return results

def load_texts(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

