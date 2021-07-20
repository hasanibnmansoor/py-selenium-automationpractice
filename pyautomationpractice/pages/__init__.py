from .home import *
from .women import *
from .cartmodal import *
from .authentication import *
from .cartsummary import *
from .address import *
from .shipping import *
from .payment import *
from .productdetails import *

__all__ = (
    home.__all__ + 
    women.__all__ + 
    cartmodal.__all__ + 
    authentication.__all__ +
    cartsummary.__all__ +
    address.__all__ + 
    shipping.__all__ +
    payment.__all__ + 
    productdetails.__all__
)
