from tenzing.core import tenzing_model
from tenzing.core.typesets import tenzingTypeset
from tenzing.core.model.types import *


class tenzing_standard_set(tenzingTypeset):
    """The standard tenzing typesets

    Includes support for the following types:

    - tenzing_float
    - tenzing_integer
    - tenzing_bool
    - tenzing_object
    - tenzing_string
    - tenzing_complex
    - tenzing_categorical
    - tenzing_datetime
    - tenzing_timedelta

    """

    def __init__(self):
        types = [
            tenzing_object,
            tenzing_bool,
            tenzing_float,
            tenzing_object,
            tenzing_complex,
            tenzing_categorical,
            tenzing_datetime,
            tenzing_timedelta,
            tenzing_integer,
            tenzing_string,
            missing_generic,
            infinite_generic,
            tenzing_generic,
            tenzing_model
        ]
        partitioners = [missing_generic, infinite_generic, tenzing_generic]
        super().__init__(partitioners, types)


class tenzing_geometry_set(tenzingTypeset):
    """Standard tenzing typeset with shapely geometry support

    Includes support for the following types:

    - tenzing_float
    - tenzing_integer
    - tenzing_bool
    - tenzing_object
    - tenzing_string
    - tenzing_complex
    - tenzing_categorical
    - tenzing_datetime
    - tenzing_timedelta
    - tenzing_geometry

    """

    def __init__(self):
        types = [
            tenzing_bool,
            tenzing_float,
            tenzing_object,
            tenzing_complex,
            tenzing_categorical,
            tenzing_datetime,
            tenzing_timedelta,
            tenzing_integer,
            tenzing_string,
            tenzing_geometry,
            missing_generic,
            infinite_generic,
            tenzing_generic,
            tenzing_model
        ]
        partitioners = [missing_generic, infinite_generic, tenzing_generic]
        super().__init__(partitioners, types)


class tenzing_complete_set(tenzingTypeset):
    """Complete tenzing typeset with all supported types

    Includes support for the following types:

    - tenzing_float
    - tenzing_integer
    - tenzing_bool
    - tenzing_object
    - tenzing_string
    - tenzing_complex
    - tenzing_categorical
    - tenzing_datetime
    - tenzing_date
    - tenzing_time
    - tenzing_timedelta
    - tenzing_geometry
    - tenzing_path
    - tenzing_existing_path
    - tenzing_image_path
    - tenzing_url
    - tenzing_ip

    """

    def __init__(self):
        types = [
            tenzing_bool,
            tenzing_float,
            tenzing_object,
            tenzing_complex,
            tenzing_categorical,
            tenzing_datetime,
            tenzing_timedelta,
            tenzing_integer,
            tenzing_string,
            tenzing_geometry,
            tenzing_url,
            tenzing_path,
            tenzing_date,
            tenzing_time,
            tenzing_existing_path,
            tenzing_image_path,
            tenzing_ip,
            missing_generic,
            infinite_generic,
            tenzing_generic,
            tenzing_model
        ]
        partitioners = [missing_generic, infinite_generic, tenzing_generic]
        super().__init__(partitioners, types)
