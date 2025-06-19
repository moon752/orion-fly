def test_vpn_placeholder():
    from core import vpn_manager
    assert hasattr(vpn_manager, "rotate"), "VPN manager needs a rotate() function"
