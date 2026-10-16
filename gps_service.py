class GPSSignalLostError(Exception):
    """Ngoai le tuy chinh khi thiet bi mat tin hieu dinh vi GPS."""


def get_current_location():
    """Mo phong truy cap GPS de lay toa do hien tai."""
    return 10.0, 105.0
