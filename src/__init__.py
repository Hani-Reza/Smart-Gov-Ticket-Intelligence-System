"""
SmartGov Triage System - UAE Government Ticket Intelligence Platform
Enterprise-grade AI/ML system for automated ticket classification and routing
"""

__version__ = "1.0.0"
__author__ = "SmartGov AI Team"
__license__ = "Proprietary - UAE Government"

from .processor import TicketProcessor
from .model_train import ModelTrainer
from .data_gen import DataGenerator

__all__ = ['TicketProcessor', 'ModelTrainer', 'DataGenerator']