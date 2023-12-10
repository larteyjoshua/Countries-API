from pydantic import BaseModel
from typing import Any, List, Optional

class Map(BaseModel):
    googleMaps:  Optional[str] = None
    openStreetMaps:  Optional[str] = None

class Currency(BaseModel):
    name: Optional[str] = None
    symbol: Optional[str] = None
    
class NativeName(BaseModel):
    official: Optional[str] = None
    common: Optional[str] = None
class ShowCountries(BaseModel):
    name: str
    zip_code: str
    flag: str
    short: str
    region:str
    capital:str
    population:int
    location:List[float]
    borders:Optional[List[str]] = []
    sub_region: str
    tld:Optional[List[str]] = []
    languages:List[str]
    map:Map
    currencies: Any
    nativeName: List[NativeName]
    cca3:str
    
    
    class Config():
        from_attributes = True