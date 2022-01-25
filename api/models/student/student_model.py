import datetime
from typing import Dict, List, Optional
from uuid import uuid4
from ..general_use_models import PydanticObjectId
from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr, Field, AnyHttpUrl


class CompanyLetterModel(BaseModel):
    """Company Letters Model"""

    uid: Indexed(str, unique=True) = str(uuid4())
    company_name: str
    letter_type: str
    letter_link: str
    is_verified: bool = False


class JobExperienceModel(BaseModel):
    """Job Experience Model"""

    uid: Indexed(str, unique=True) = str(uuid4())
    company_name: str
    employment_type: str
    role: str
    is_current_company: bool = False
    start_month: int
    start_year: int
    end_month: Optional[int] = None
    end_year: Optional[int] = None

class CertificationModel(BaseModel):
    """Certifications Model"""

    uid: Indexed(str, unique=True) = str(uuid4())
    course_name: str
    certificate_link: str
    is_verified: bool = False


class ScorecardModel(BaseModel):
    """Scorecard Model"""

    uid: Indexed(str, unique=True) = str(uuid4())
    exam_name: str
    scorecard_link: str
    is_verified: bool = False


class SocialModel(BaseModel):
    """Social Media Platform Model"""

    uid: Indexed(str, unique=True) = str(uuid4())
    platform_name: str
    profile_link: AnyHttpUrl

class AddressModel(BaseModel):
    """Address Model"""

    pincode: str = ''
    state: str = ''
    district: str = ''
    country: str = ''
    address_line_1: str = ''
    address_line_2: Optional[str] = None


class StudentModel(Document):
    """Maps student model to database document. """

    # Extra functionality use fields
    is_account_active: bool = False
    is_banned: bool = False
    token: Optional[str] = ''
    student_id: Indexed(str, unique=True) = str(uuid4())
    events: Optional[List[str]] = []
    
    # Personal info 
    fname: str
    lname: Optional[str] = None
    roll_no: Indexed(str, unique=True)
    batch: int 
    branch: str
    gender: str
    email: Indexed(str, unique=True) 
    phone: Optional[str] = None
    password: str 
    
    # Additional info
    category: str = '' 
    minority: Optional[bool] = None
    handicap: Optional[bool] = None
    dob: str = '' 

    # Educational info
    matric_pcnt: Optional[float] = None 
    yop_matric: Optional[int] = None 
    hs_pcnt: Optional[float] = None 
    yop_hs: Optional[int] = None 
    sgpa: List[float] = [] 
    cgpa: Optional[float] = None 

    # Skills info
    skills: List[PydanticObjectId] = [] 
    
    # Address info
    permanent_address: Optional[AddressModel] = {}
    is_permanent_equals_present: bool = False
    present_address: Optional[AddressModel] = None
    
    # Application info
    applied_positions: Optional[List[PydanticObjectId]] = []
    
    # Company Letters info
    company_letters: Optional[List[CompanyLetterModel]] = []
    
    # Job experience info
    job_experience: List[JobExperienceModel] = []
    
    # Certification info
    certifications: Optional[List[CertificationModel]] = []
    
    # Score card info
    score_cards: Optional[List[ScorecardModel]] = []
    
    # Social info
    social_links: Optional[List[SocialModel]] = []



    class Config:
        anystr_lower = True
        

    class Collection:
        name = "student"
