from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    """Abstract base class representing a tax calculator interface."""

    @abstractmethod
    def calculate(self, amount: float) -> float:
        """Calculates tax on a given amount.

        Args:
            amount: The base amount.

        Returns:
            The calculated tax value.
        """
        pass


class TelecomTaxCalculator(TaxCalculator):
    """Calculates telecommunication taxes based on a structured rate."""

    def __init__(self, vat_rate: float = 0.20, sct_rate: float = 0.15):
        """Initializes the calculator with VAT and Special Communication Tax (SCT) rates.

        Default rates are based on typical telecom regulations (e.g., 20% VAT, 15% SCT).
        """
        if vat_rate < 0 or sct_rate < 0:
            raise ValueError("Tax rates cannot be negative.")
        self.vat_rate = vat_rate
        self.sct_rate = sct_rate

    def calculate(self, amount: float) -> float:
        """Calculates the total tax amount (VAT + SCT) for a given bill base amount.

        Args:
            amount: The base bill amount before taxes.

        Returns:
            The total calculated tax value.
        """
        if amount < 0:
            raise ValueError("Base amount cannot be negative.")
        
        vat_amount = amount * self.vat_rate
        sct_amount = amount * self.sct_rate
        return round(vat_amount + sct_amount, 2)
