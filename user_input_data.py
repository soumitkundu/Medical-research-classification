from pydantic import BaseModel

# defining the input data model
class InputData(BaseModel):
    P_incidence: float
    P_tilt: float
    L_angle: float
    S_slope: float
    P_radius: float
    S_Degree: float