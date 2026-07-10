import pytest
from tax_calculator import TelecomTaxCalculator


def test_telecom_tax_calculator():
    """Validates the telecom tax calculator functionality with standard, edge, and invalid inputs."""
    # 1. Standard calculation verification
    calculator = TelecomTaxCalculator(vat_rate=0.20, sct_rate=0.15)
    assert calculator.calculate(100.0) == 35.0
    assert calculator.calculate(200.0) == 70.0
    
    # 2. Zero base amount verification
    assert calculator.calculate(0.0) == 0.0
    
    # 3. Custom rates verification
    custom_calculator = TelecomTaxCalculator(vat_rate=0.10, sct_rate=0.05)
    assert custom_calculator.calculate(100.0) == 15.0

    # 4. Input validation (negative base amount)
    with pytest.raises(ValueError):
        calculator.calculate(-50.0)

    # 5. Input validation (negative tax rates)
    with pytest.raises(ValueError):
        TelecomTaxCalculator(vat_rate=-0.10)
