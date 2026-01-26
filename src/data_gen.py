"""
GCC Smart-Gov Ticket Intelligence System
Synthetic Data Generation Module
Author: Principal AI/ML Engineer
Created for UAE Government Enterprise Deployment
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import re
from typing import List, Dict, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TicketDataGenerator:
    """
    Generates realistic synthetic service tickets for UAE government entities
    with balanced distribution and realistic UAE context.
    """
    
    # UAE Government Entities
    UAE_ENTITIES = [
        "DEWA", "RTA", "Etisalat", "ICA", "Tasheel", "Dubai Police",
        "Abu Dhabi Government", "Dubai Municipality", "Sharjah Municipality",
        "DHA", "ADNOC", "Dubai Courts", "GDRFA", "Mohre",
        "Dubai Land Department", "Civil Defense", "DED", "Du", "Amer"
    ]
    
    # Service Categories
    CATEGORIES = [
        "Facilities",
        "Technical / IT", 
        "Billing",
        "Inquiry",
        "Safety / Emergency"
    ]
    
    # Sentiment Levels
    SENTIMENTS = ["Positive", "Neutral", "Negative"]
    
    # Priority Levels
    PRIORITIES = ["Low", "Medium", "High", "Critical"]
    
    # UAE-specific keywords
    UAE_KEYWORDS = {
        "DEWA": ["electricity", "water", "bill", "charges", "outage", "green charger"],
        "RTA": ["nol card", "metro", "salik", "driving license", "bus", "traffic"],
        "Etisalat": ["internet", "mobile", "bill", "data", "connection"],
        "ICA": ["emirates id", "passport", "visa", "immigration"],
        "Tasheel": ["visa renewal", "labor contract", "document", "appointment"],
        "Safety / Emergency": ["fire", "gas leak", "accident", "urgent", "emergency", "trapped"]
    }
    
    # Sentence templates for each category and sentiment
    TICKET_TEMPLATES = {
        "Facilities": {
            "Positive": [
                "New {facility} installed in {area} - excellent work",
                "{entity} maintenance team was very professional",
                "Public {facility} renovation completed ahead of schedule",
                "{area} community center improvements are appreciated"
            ],
            "Neutral": [
                "Request for {facility} maintenance in {area}",
                "{facility} inspection needed at {location}",
                "Schedule {facility} repair for {area}"
            ],
            "Negative": [
                "{facility} not working at {location} for {duration}",
                "Poor condition of {facility} in {area}",
                "Urgent repair needed for {facility} at {location}"
            ]
        },
        "Technical / IT": {
            "Positive": [
                "{entity} online portal working smoothly now",
                "Technical issue resolved quickly by {entity} team",
                "System upgrade completed successfully"
            ],
            "Neutral": [
                "{entity} system access issue",
                "Need assistance with {entity} online services",
                "Technical query regarding {system}"
            ],
            "Negative": [
                "{entity} website down since {time}",
                "Cannot login to {entity} portal - error message",
                "{system} crashed during {operation}"
            ]
        },
        "Billing": {
            "Positive": [
                "Bill payment process was seamless",
                "Thank you for resolving billing discrepancy",
                "Payment refund processed quickly"
            ],
            "Neutral": [
                "Query about {entity} charges for {period}",
                "Need clarification on billing statement",
                "Invoice details request"
            ],
            "Negative": [
                "Incorrect charges on {entity} bill",
                "Overcharged for {service} by {entity}",
                "Payment made but still showing as pending"
            ]
        },
        "Inquiry": {
            "Positive": [
                "Excellent service at {entity} center",
                "Thank you for prompt response to my query",
                "Information provided was very helpful"
            ],
            "Neutral": [
                "Need information about {entity} {service}",
                "Query regarding {process} requirements",
                "Status check for {application}"
            ],
            "Negative": [
                "No response to my inquiry about {topic}",
                "Conflicting information received from {entity}",
                "Cannot get clear answer about {issue}"
            ]
        },
        "Safety / Emergency": {
            "Positive": [
                "Emergency response was very quick - thank you",
                "Safety inspection completed thoroughly",
                "Hazard reported and resolved promptly"
            ],
            "Neutral": [
                "Report of potential safety issue at {location}",
                "Request for safety inspection at {area}",
                "Need guidance on safety protocols for {situation}"
            ],
            "Negative": [
                "URGENT: {hazard} at {location} - immediate action needed",
                "Safety hazard reported but no response",
                "Emergency situation at {location} - help required"
            ]
        }
    }
    
    # UAE locations
    UAE_LOCATIONS = [
        "Dubai Marina", "Al Barsha", "Sheikh Zayed Road", "Abu Dhabi City",
        "Sharjah Industrial Area", "Deira", "Bur Dubai", "Jumeirah",
        "Al Ain", "Ras Al Khaimah", "Fujairah", "Ajman", "Umm Al Quwain",
        "Business Bay", "Downtown Dubai", "Silicon Oasis", "Motor City"
    ]
    
    # Facilities/Systems
    FACILITIES = [
        "AC system", "elevator", "parking machine", "street lights",
        "water fountain", "public restroom", "playground equipment",
        "lighting system", "security cameras", "fire alarm"
    ]
    
    def __init__(self, seed: int = 42):
        """Initialize generator with random seed for reproducibility."""
        random.seed(seed)
        np.random.seed(seed)
        logger.info("TicketDataGenerator initialized with UAE context")
    
    def generate_emirates_id(self) -> str:
        """Generate realistic UAE Emirates ID number."""
        # Format: 784-YYYY-XXXXXXX-X
        year = random.randint(1980, 2005)
        sequence = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        check_digit = random.randint(1, 9)
        return f"784-{year}-{sequence}-{check_digit}"
    
    def generate_phone_number(self) -> str:
        """Generate realistic UAE phone number."""
        # UAE mobile prefixes
        prefixes = ["50", "52", "54", "55", "56", "58"]
        prefix = random.choice(prefixes)
        number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        return f"+971{prefix}{number}"
    
    def generate_ticket_text(self, category: str, sentiment: str, entity: str) -> str:
        """Generate realistic ticket text based on category and sentiment."""
        templates = self.TICKET_TEMPLATES[category][sentiment]
        template = random.choice(templates)
        
        # Fill template with appropriate values
        replacements = {
            "{facility}": random.choice(self.FACILITIES),
            "{area}": random.choice(self.UAE_LOCATIONS),
            "{location}": random.choice(self.UAE_LOCATIONS),
            "{entity}": entity,
            "{duration}": f"{random.randint(1, 24)} hours",
            "{time}": f"{random.randint(1, 12)}:{random.choice(['00', '30'])}",
            "{system}": random.choice(["portal", "app", "website", "payment system"]),
            "{operation}": random.choice(["renewal", "payment", "registration", "booking"]),
            "{period}": random.choice(["November", "December", "last month", "Q4 2024"]),
            "{service}": random.choice(["internet", "electricity", "water", "mobile"]),
            "{process}": random.choice(["renewal", "application", "registration", "payment"]),
            "{application}": random.choice(["Emirates ID", "visa", "license", "permit"]),
            "{topic}": random.choice(["charges", "requirements", "status", "documents"]),
            "{issue}": random.choice(["fees", "timeline", "requirements", "process"]),
            "{hazard}": random.choice(["gas leak", "fire", "electrical hazard", "structural damage"]),
            "{situation}": random.choice(["construction", "public event", "school zone", "parking"])
        }
        
        text = template
        for key, value in replacements.items():
            text = text.replace(key, value)
        
        return text
    
    def determine_priority(self, category: str, sentiment: str) -> str:
        """Determine priority based on category and sentiment."""
        if category == "Safety / Emergency":
            return "Critical" if sentiment == "Negative" else "High"
        elif category == "Technical / IT":
            if sentiment == "Negative":
                return random.choice(["High", "Medium"])
            return "Medium"
        elif category == "Billing":
            return "Medium"
        elif category == "Facilities":
            return "High" if sentiment == "Negative" else random.choice(["Medium", "Low"])
        else:  # Inquiry
            return "Low"
    
    def generate_tickets(self, num_tickets: int = 150) -> pd.DataFrame:
        """
        Generate balanced synthetic tickets for UAE government entities.
        
        Args:
            num_tickets: Number of tickets to generate
            
        Returns:
            DataFrame with synthetic ticket data
        """
        logger.info(f"Generating {num_tickets} synthetic tickets for UAE context...")
        
        tickets = []
        
        # Ensure balanced distribution
        tickets_per_category = num_tickets // len(self.CATEGORIES)
        
        for category in self.CATEGORIES:
            for _ in range(tickets_per_category):
                # Select sentiment with realistic distribution
                sentiment_weights = [0.2, 0.3, 0.5]  # 20% Positive, 30% Neutral, 50% Negative
                sentiment = random.choices(self.SENTIMENTS, weights=sentiment_weights)[0]
                
                # Select appropriate entity for category
                if category == "Safety / Emergency":
                    entity = random.choice(["Civil Defense", "DHA", "RTA", "Municipality"])
                elif category == "Technical / IT":
                    entity = random.choice(["Etisalat", "RTA", "Tasheel", "DEWA", "Du"])
                elif category == "Billing":
                    entity = random.choice(["DEWA", "Etisalat", "Du", "RTA"])
                elif category == "Facilities":
                    entity = random.choice(["Dubai Municipality", "RTA", "DEWA", "Sharjah Municipality"])
                else:  # Inquiry
                    entity = random.choice(self.UAE_ENTITIES)
                
                # Generate ticket
                ticket_id = len(tickets) + 1
                text = self.generate_ticket_text(category, sentiment, entity)
                priority = self.determine_priority(category, sentiment)
                
                # Generate PII data (sometimes empty for realism)
                emirates_id = self.generate_emirates_id() if random.random() > 0.3 else ""
                phone_number = self.generate_phone_number() if random.random() > 0.2 else ""
                
                tickets.append({
                    "ticket_id": ticket_id,
                    "text": text,
                    "category": category,
                    "sentiment": sentiment,
                    "priority": priority,
                    "government_entity": entity,
                    "emirates_id": emirates_id,
                    "phone_number": phone_number
                })
        
        # Create DataFrame
        df = pd.DataFrame(tickets)
        
        # Shuffle the data
        df = df.sample(frac=1, random_state=42).reset_index(drop=True)
        
        logger.info(f"Generated {len(df)} synthetic tickets with balanced distribution")
        logger.info("Category distribution:")
        logger.info(df['category'].value_counts().to_string())
        logger.info("\nSentiment distribution:")
        logger.info(df['sentiment'].value_counts().to_string())
        
        return df
    
    def save_to_csv(self, df: pd.DataFrame, filepath: str = "data/tickets_synthetic_v2.csv"):
        """Save generated tickets to CSV file."""
        try:
            df.to_csv(filepath, index=False)
            logger.info(f"Saved {len(df)} tickets to {filepath}")
            return True
        except Exception as e:
            logger.error(f"Error saving tickets: {e}")
            return False


def main():
    """Main function to generate and save synthetic ticket data."""
    generator = TicketDataGenerator(seed=42)
    
    # Generate tickets
    tickets_df = generator.generate_tickets(num_tickets=150)
    
    # Save to CSV
    success = generator.save_to_csv(tickets_df)
    
    if success:
        print("✅ Synthetic data generation completed successfully!")
        print(f"📊 Total tickets generated: {len(tickets_df)}")
        print("\n📈 Distribution Summary:")
        print(tickets_df['category'].value_counts())
        print("\n🎭 Sentiment Distribution:")
        print(tickets_df['sentiment'].value_counts())
    else:
        print("❌ Failed to generate synthetic data")


if __name__ == "__main__":
    main()